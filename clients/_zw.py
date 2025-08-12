#!/usr/bin/env python3
import uuid, requests

def _q(s: str) -> str:
    """Quote only when needed; escape \" and \\ inside quotes."""
    if (":" in s) or (" " in s):
        return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
    return s

def zw_encode(val, indent=""):
    if isinstance(val, dict):
        lines=[]
        for k,v in val.items():
            if isinstance(v, (dict, list)):
                lines.append(f"{indent}{k}:")
                lines.append(zw_encode(v, indent + "  "))
            elif isinstance(v, str):
                lines.append(f"{indent}{k}: {_q(v)}")
            elif v is None:
                lines.append(f"{indent}{k}:")
            else:
                lines.append(f"{indent}{k}: {v}")
        return "\n".join(lines)

    if isinstance(val, list):
        lines=[]
        for item in val:
            if isinstance(item, (dict, list)):
                lines.append(f"{indent}-")
                lines.append(zw_encode(item, indent + '  '))
            elif isinstance(item, str):
                lines.append(f"{indent}- {_q(item)}")
            else:
                lines.append(f"{indent}- {item}")
        return "\n".join(lines)

    return str(val)

def zw_call(base_url, tool, payload, accept="text/zw", auth=None, timeout=60):
    rid = str(uuid.uuid4())
    head = (
        "ZW-CALL v0.1\n"
        f"tool: {tool}\n"
        f"id: {rid}\n"
        f"accept: {accept}\n"
        "return: full_file\n"
    )
    if auth:
        head += f"auth: bearer {auth}\n"
    head += "---\n"
    body = zw_encode(payload) + "\n"

    resp = requests.post(
        base_url.rstrip("/") + "/zwrpc",
        data=head + body,
        headers={"Content-Type": "text/zw"},
        timeout=timeout,
    )
    txt = resp.text
    sep = "\n---\n"
    i = txt.find(sep)
    head_out = txt if i == -1 else txt[:i]
    body_out = "" if i == -1 else txt[i + len(sep) :]
    return head_out, body_out, txt

def zw_split(txt: str):
    sep = "\n---\n"
    i = txt.find(sep)
    return (txt if i == -1 else txt[:i], "" if i == -1 else txt[i + len(sep) :])

def zw_parse_status(head: str) -> str:
    for ln in head.splitlines():
        if ln.lower().startswith("status:"):
            return ln.split(":", 1)[1].strip().lower()
    return ""
