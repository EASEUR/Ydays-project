import socket
import time
import json
import psutil


def top_processus(n=10):
    # first pass: initialize cpu measurement
    for p in psutil.process_iter():
        try:
            p.cpu_percent(None)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    time.sleep(1)

    liste = []

    # get information for each process
    for p in psutil.process_iter(["pid", "name", "memory_percent"]):
        try:
            liste.append(
                {
                    "pid": p.info["pid"],
                    "name": p.info["name"],
                    "cpu_percent": p.cpu_percent(None),
                    "memory_percent": round(
                        p.info["memory_percent"] or 0, 2
                    ),
                }
            )
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass  # ignore inaccessible processes

    # sort processes by cpu usage
    return sorted(
        liste,
        key=lambda x: x["cpu_percent"],
        reverse=True
    )[:n]


def collecter():
    # collect system information
    return {
        "hostname": socket.gethostname(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent,
        "top_processes": top_processus(),
    }


# run the monitoring loop
while True:
    try:
        print(collecter())
    except Exception as e:
        print(json.dumps(collecter(), indent=2))

    time.sleep(10)