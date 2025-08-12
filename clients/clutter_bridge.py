#!/usr/bin/env python3
import os, sys
from _zw import zw_call
def main():
    if len(sys.argv)<2:
        print("Usage: python3 clients/clutter_bridge.py file_open warroom/file.txt"); return
    tool=sys.argv[1]; base=os.environ.get("WARROOM_URL","http://127.0.0.1:6060")
    auth=os.environ.get("AUTH_BEARER","") or None
    if tool=="file_open":
        payload={"path": sys.argv[2]}
    elif tool=="file_save_staged":
        payload={"path": sys.argv[2], "content": sys.argv[3] if len(sys.argv)>3 else ""}
    elif tool=="diff_preview":
        payload={"path": sys.argv[2], "content": sys.argv[3] if len(sys.argv)>3 else ""}
    elif tool=="promote_artifact":
        payload={"path": sys.argv[2]}
    else:
        print("unknown tool:", tool); return
    head, body, raw = zw_call(base, tool, payload, accept="text/zw", auth=auth)
    print(body or raw)
if __name__=="__main__": main()
