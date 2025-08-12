#!/usr/bin/env python3
import os, uuid, requests

def zw_encode(val, indent=""):
    if isinstance(val, dict):
        out=[]
        for k,v in val.items():
            if isinstance(v,(dict,list)):
                out.append(f"{indent}{k}:"); out.append(zw_encode(v, indent+"  "))
            elif isinstance(v,str):
                q=v if (":" not in v and " " not in v) else f"\"{v.replace('\"','\\\"')}\""
                out.append(f"{indent}{k}: {q}")
            elif v is None: out.append(f"{indent}{k}:")
            else: out.append(f"{indent}{k}: {v}")
        return "\n".join(out)
    if isinstance(val, list):
        out=[]
        for i in val:
            if isinstance(i,(dict,list)):
                out.append(f"{indent}-"); out.append(zw_encode(i, indent+"  "))
            elif isinstance(i,str):
                q=i if (":" not in i and " " not in i) else f"\"{i.replace('\"','\\\"')}\""
                out.append(f"{indent}- {q}")
            else: out.append(f"{indent}- {i}")
        return "\n".join(out)
    return str(val)

def zw_call(base_url, tool, payload, accept="text/zw", auth=None, timeout=60):
    rid=str(uuid.uuid4())
    head=f"ZW-CALL v0.1\ntool: {tool}\nid: {rid}\naccept: {accept}\nreturn: full_file\n"
    if auth: head+=f"auth: bearer {auth}\n"
    head+="---\n"
    body=zw_encode(payload)+"\n"
    r=requests.post(base_url.rstrip('/')+"/zwrpc", data=head+body,
                    headers={"Content-Type":"text/zw"}, timeout=timeout)
    txt=r.text; sep="\n---\n"; i=txt.find(sep)
    return (txt if i==-1 else txt[:i], "" if i==-1 else txt[i+len(sep):], txt)

def zw_split(txt: str):
    sep = "\n---\n"; i = txt.find(sep)
    return (txt if i==-1 else txt[:i], "" if i==-1 else txt[i+len(sep):])

def zw_parse_status(head: str) -> str:
    for ln in head.splitlines():
        if ln.lower().startswith("status:"):
            return ln.split(":",1)[1].strip().lower()
    return ""
