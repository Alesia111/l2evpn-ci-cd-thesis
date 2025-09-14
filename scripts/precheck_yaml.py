#!/usr/bin/env python3
import sys, yaml, pathlib
p = pathlib.Path("evpn01.yml")
try:
    data = yaml.safe_load(p.read_text(encoding="utf-8"))
except Exception as e:
    print(f"[FAIL] YAML parse error: {e}"); sys.exit(1)
if "topology" not in data: print("[FAIL] Missing topology"); sys.exit(1)
topo = data["topology"]
for k in ("nodes","links"):
    if k not in topo: print(f"[FAIL] Missing topology.{k}"); sys.exit(1)
for n in ("spine1","leaf1","leaf2"):
    if n not in topo["nodes"]: print(f"[FAIL] Missing node {n}"); sys.exit(1)
print("[OK] evpn01.yml precheck passed.")
