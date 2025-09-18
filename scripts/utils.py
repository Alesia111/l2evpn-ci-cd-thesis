# scripts/utils.py
import subprocess, shlex, time

LOG_FILE = "results.log"

def log_to_file(message: str):
    """Append a message to results.log with a timestamp."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

def run(cmd: str, check=True, timeout=60):
    """
    Executes a shell command and returns a CompletedProcess object.
    - Prints stdout/stderr to console.
    - Logs command, exit code, and duration to results.log.
    - If check=True and the command fails, raises SystemExit.
    """
    print(f"+ {cmd}")
    t0 = time.time()
    res = subprocess.run(shlex.split(cmd), capture_output=True, text=True, timeout=timeout)
    dt = time.time() - t0

    if res.stdout:
        print(res.stdout)
    if res.returncode != 0 and res.stderr:
        print(res.stderr)

    log_to_file(f"CMD: {cmd} | Exit: {res.returncode} | Time: {dt:.2f}s")

    if res.returncode != 0 and check:
        raise SystemExit(res.returncode)
    return res

def sr_exec(node: str, cli_cmd: str, check=True, timeout=60):
    """
    Executes an SR Linux CLI command inside a ContainerLab node using sr_cli.
    Uses '-e' to execute the command and exit.
    """
    cmd = f'docker exec {node} sr_cli -e "{cli_cmd}"'
    return run(cmd, check=check, timeout=timeout)

def sr_exec_out(node: str, cli_cmd: str, timeout=60):
    """
    Convenience wrapper that returns only stdout (string) and never raises.
    """
    res = sr_exec(node, cli_cmd, check=False, timeout=timeout)
    return (res.stdout or "").strip()
