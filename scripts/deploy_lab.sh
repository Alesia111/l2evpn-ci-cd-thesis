#!/usr/bin/env bash
set -euo pipefail
containerlab destroy -t ./evpn01.yml -c || true
containerlab deploy -t ./evpn01.yml --reconfigure
containerlab inspect -t ./evpn01.yml --all
