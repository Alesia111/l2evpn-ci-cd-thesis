#!/usr/bin/env python3
import pathlib, time, subprocess, shlex
from utils import run
NODES = {
  "clab-evpn01-spine1": "configs/spine1.cli",
  "clab-evpn01-leaf1" : "configs/leaf1.cli",
  "clab-evpn01-leaf2" : "configs/leaf2.cli",
}
def wait_ready(node, timeout=90):
  t0=time.time()
  while time.time()-t0<timeout:
    r=run(f"docker exec {node} sr_cli -e 'show interface brief'", check=False)
    if r.returncode==0 and "Port" in r.stdout: return
    time.sleep(3)
  raise SystemExit(f"[FAIL] {node} not ready")
def apply_cli(node, file):
  assert pathlib.Path(file).exists(), f"Missing {file}"
  cmd=f"docker exec -i {node} sr_cli -ed"
  with open(file,"rb") as f:
    p=subprocess.Popen(shlex.split(cmd), stdin=f)
    p.communicate()
    if p.returncode!=0: raise SystemExit(f"[FAIL] apply {file} -> {node}")
def main():
  for n,f in NODES.items():
    wait_ready(n); apply_cli(n,f)
if __name__=="__main__": main()
