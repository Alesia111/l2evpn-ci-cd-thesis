import subprocess, shlex
def run(cmd: str, check=True):
    print(f"+ {cmd}")
    res = subprocess.run(shlex.split(cmd), capture_output=True, text=True)
    print(res.stdout)
    if res.returncode != 0 and check:
        print(res.stderr); raise SystemExit(res.returncode)
    return res
def sr_exec(node: str, cli_cmd: str):
    return run(f"docker exec {node} sr_cli -e '{cli_cmd}'")
