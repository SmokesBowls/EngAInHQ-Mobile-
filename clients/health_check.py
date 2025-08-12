#!/usr/bin/env python3
import os, sys
from _zw import zw_call, zw_parse_status

OK="✅"; BAD="❌"

def check(name, base, tool, payload, timeout=12):
    if not base: return (name, BAD, "endpoint not set")
    try:
        head, body, _ = zw_call(base, tool, payload, accept="text/zw", auth=(os.environ.get("AUTH_BEARER") or None), timeout=timeout)
        st = zw_parse_status(head)
        return (name, OK if st=="ok" else BAD, st or "no status")
    except Exception as e:
        return (name, BAD, f"{type(e).__name__}: {e}")

def main():
    results = []
    results.append(check("Trae", os.environ.get("CATHEDRAL_URL","").strip(), "prompt_probe", {"model": os.environ.get("MODEL","")}))
    results.append(check("MrLore", os.environ.get("MRLORE_URL","").strip(), "lore_query", {"topic":"healthcheck","scope":"global","strict":False}))
    war = os.environ.get("WARROOM_URL","").strip()
    name, icon, msg = check("Warroom", war, "file_open", {"path": os.environ.get("WARROOM_HEALTH_PATH","warroom/README.md")})
    if icon!=OK:
        name, icon, msg = check("Warroom", war, "diff_preview", {"path": os.environ.get("WARROOM_HEALTH_PATH","warroom/README.md"), "content": ""})
    failures=0
    for n,i,m in results+[ (name,icon,msg) ]:
        print(f"{i} {n}: {m}")
        if i==BAD: failures+=1
    sys.exit(1 if failures else 0)

if __name__=="__main__": main()
