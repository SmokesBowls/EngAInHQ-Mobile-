#!/usr/bin/env python3
import os, sys
from _zw import zw_call
def main():
    if len(sys.argv)<2:
        print("Usage: python3 clients/mrlore_bridge.py lore_query \"topic\""); return
    tool=sys.argv[1]; arg=" ".join(sys.argv[2:]) if len(sys.argv)>2 else ""
    base=os.environ.get("MRLORE_URL","http://127.0.0.1:7070")
    auth=os.environ.get("AUTH_BEARER","") or None
    if tool=="lore_query":
        payload={"topic":arg, "scope":"character", "strict":True}
    else:
        print("unknown tool:", tool); return
    head, body, raw = zw_call(base, tool, payload, accept="text/zw", auth=auth)
    print(body or raw)
if __name__=="__main__": main()
