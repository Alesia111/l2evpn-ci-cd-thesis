# scripts/utils.py
import subprocess, shlex, time

LOG_FILE = "results.log"

def log_to_file(message: str):
    """Append a message to results.log with a timestamp."""
    with open(LOG_FILE, "a") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

def run(cmd: str, check=True, timeout=60):
    """
    Executes a shell command and returns a CompletedProcess object.
    - Measures execution time and logs command, duration, and result.
    - If check=True and the command fails, it raises SystemExit with the exit code.
    """
    print(f"+ {cmd}")
    start = time.time()
    res = subprocess.run(shlex.split(cmd), capture_output=True, text=True, timeout=timeout)
    duration = time.time() - start

    # Print outputs to console
    if res.stdout:
        print(res.stdout)
    if res.returncode != 0 and res.stderr:
        print(res.stderr)

    # Log results to file
    log_msg = f"CMD: {cmd} | Exit: {res.returncode} | Time: {duration:.2f}s"
    log_to_file(log_msg)

    if res.returncode != 0 and check:
        raise SystemExit(res.returncode)
    return res

def sr_exec(node: str, cli_cmd: str, check=True, timeout=60):
    """
    Executes a command on a Nokia SR Linux container using `sr_cli`.
    Logs command execution time and result.
    """
    cmd = f"docker exec {node} sr_cli -e \"{cli_cmd}\""
    return run(cmd, check=check, timeout=timeout)

def sr_exec_out(node: str, cli_cmd: str, timeout=60):
    """
    Simplified version of sr_exec() that only returns stdout as a string.
    Still logs command execution time to results.log.
    """
    res = sr_exec(node, cli_cmd, check=False, timeout=timeout)
    return (res.stdout or "").strip()
