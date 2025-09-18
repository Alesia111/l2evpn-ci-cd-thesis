#!/usr/bin/env python3
"""
Automated network validation script for ContainerLab testbed.
This script uses the helper function `sr_exec` (imported from utils.py)
to run commands on specific network nodes inside the topology.
"""

from utils import sr_exec

def ping(node, dst):
    """
    Executes a ping command from a given node to a destination IP address.
    node: the container/node name inside ContainerLab
    dst:  destination IP address to ping
    """
    sr_exec(node, f"ping {dst} network-instance default")

def show(node, ifn):
    """
    Executes a 'show interface detail' command on a given node.
    node: the container/node name inside ContainerLab
    ifn:  the interface name (e.g., ethernet-1/1)
    """
    sr_exec(node, f"show interface {ifn} detail")

def main():
    """
    Main function that validates the topology by:
    1. Checking interface details on spine and leaf nodes
    2. Running ping tests between nodes
    """
    # Loop through key nodes and check ethernet-1/1 interfaces
    for n in ["clab-evpn01-spine1", "clab-evpn01-leaf1", "clab-evpn01-leaf2"]:
        show(n, "ethernet-1/1")

    # Additional interface check for spine1
    show("clab-evpn01-spine1", "ethernet-1/2")

    # Connectivity tests (ping between hosts in the topology)
    ping("clab-evpn01-spine1", "192.168.10.1")
    ping("clab-evpn01-spine1", "192.168.10.3")
    ping("clab-evpn01-leaf1", "192.168.10.0")
    ping("clab-evpn01-leaf2", "192.168.10.2")

if __name__ == "__main__":
    main()


