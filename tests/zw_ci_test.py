import re
from pathlib import Path

# Import from project
import sys
sys.path.append(str(Path("clients").resolve()))
from _zw import zw_encode, zw_split, zw_parse_status

def test_zw_encode_map_and_list():
    doc = {"tool":"lore_query","args":{"topic":"Zara origin","tags":["a","b"]}}
    out = zw_encode(doc)
    assert "tool: lore_query" in out
    assert "args:" in out
    assert re.search(r"\\n\\s+topic:", out)
    assert re.search(r"\\n\\s+- a\\n\\s+- b", out)

def test_zw_split_and_status_ok():
    sample = "ZW-RESULT v0.1\nstatus: ok\nid: xyz\n---\nbody here\n"
    head, body = zw_split(sample)
    assert "status: ok" in head
    assert body.strip() == "body here"
    assert zw_parse_status(head) == "ok"

def test_zw_split_no_sep():
    sample = "ZW-RESULT v0.1\nstatus: error\nid: nope\n"
    head, body = zw_split(sample)
    assert body == ""
    assert zw_parse_status(head) == "error"
