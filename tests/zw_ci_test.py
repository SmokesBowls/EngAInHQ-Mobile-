import re, sys
from pathlib import Path
sys.path.append(str(Path("clients").resolve()))
from _zw import zw_encode, zw_split, zw_parse_status
def test_encode():
    out = zw_encode({"tool":"x","args":{"topic":"Zara","tags":["a","b"]}})
    assert "tool: x" in out and "args:" in out and "- a" in out and "- b" in out
def test_split_status_ok():
    head, body = zw_split("ZW-RESULT v0.1\nstatus: ok\nid: x\n---\nbody\n")
    assert zw_parse_status(head)=="ok" and body.strip()=="body"
def test_split_no_sep():
    head, body = zw_split("ZW-RESULT v0.1\nstatus: error\nid: x\n")
    assert body=="" and zw_parse_status(head)=="error"
