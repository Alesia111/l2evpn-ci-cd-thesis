# scripts/utils.py
import subprocess, shlex

def run(cmd: str, check=True, timeout=60):
    """
    Executes a shell command and returns a CompletedProcess object.
    - If check=True and the command fails, it raises SystemExit with the exit code.
    - Captures both stdout and stderr for logging/debugging.
    """
    print(f"+ {cmd}")
    res = subprocess.run(shlex.split(cmd), capture_output=True, text=True, timeout=timeout)
    if res.stdout:
        print(res.stdout)
    if res.returncode != 0:
        if res.stderr:
            print(res.stderr)
        if check:
            raise SystemExit(res.returncode)
    return res

def sr_exec(node: str, cli_cmd: str, check=True, timeout=60):
    """
    Executes a command on a Nokia SR Linux container using `sr_cli`.
    Returns the CompletedProcess object with .stdout/.stderr/.returncode.

    Notes:
    - Uses `-e` to execute the command and exit (preferred for modern SR Linux).
    - If needed, you can replace `-e` with `-c` (both are supported).
    """
    cmd = f"docker exec {node} sr_cli -e \"{cli_cmd}\""
    return run(cmd, check=check, timeout=timeout)

def sr_exec_out(node: str, cli_cmd: str, timeout=60):
    """
    Simplified version of sr_exec() that only returns stdout as a string.
    Useful when you only care about the command output, not exit code or stderr.
    """
    res = sr_exec(node, cli_cmd, check=False, timeout=timeout)
    return (res.stdout or "").strip()


