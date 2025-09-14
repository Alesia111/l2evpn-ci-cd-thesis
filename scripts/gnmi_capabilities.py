#!/usr/bin/env python3
from pygnmi.client import gNMIclient
import json

TARGET = ("172.20.20.3", 57400)  # vendos IP e leaf/spine nga containerlab inspect
USER = "admin"
PASS = "admin"

with gNMIclient(target=TARGET, username=USER, password=PASS, insecure=True) as gc:
    caps = gc.capabilities()
    print(json.dumps(caps, indent=2))
