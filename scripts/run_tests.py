#!/usr/bin/env python3
from utils import sr_exec
def ping(node, dst): sr_exec(node, f"ping {dst} network-instance default")
def show(node, ifn): sr_exec(node, f"show interface {ifn} detail")
def main():
  for n in ["clab-evpn01-spine1","clab-evpn01-leaf1","clab-evpn01-leaf2"]:
    show(n,"ethernet-1/1")
  show("clab-evpn01-spine1","ethernet-1/2")
  ping("clab-evpn01-spine1","192.168.10.1")
  ping("clab-evpn01-spine1","192.168.10.3")
  ping("clab-evpn01-leaf1","192.168.10.0")
  ping("clab-evpn01-leaf2","192.168.10.2")
if __name__=="__main__": main()
