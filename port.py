import socket
import threading
from queue import Queue
import time
from useful import ConsoleTool   # your helper

# Global
open_ports = []
q = Queue()

# Scan function (safe, won't hang forever)
def portscan(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)   # hard timeout (1 second max)
        result = s.connect_ex((target, port))  # returns 0 if connected
        s.close()
        return result == 0
    except Exception:
        return False

# Worker
def worker(target):
    while True:
        port = q.get()
        if port is None:  # poison pill to stop thread
            break
        if portscan(target, port):
            open_ports.append(port)
            print(f"Port {port} is Open")
        q.task_done()

def main():
    target = input("Enter the target IP address: ").strip()
    time.sleep(1)
    ConsoleTool.clear()

    # Fill queue
    for port in range(1, 1025):   # 1–1024
        q.put(port)

    # Thread pool
    thread_list = []
    num_threads = 1024
    for _ in range(num_threads):
        t = threading.Thread(target=worker, args=(target,))
        t.start()
        thread_list.append(t)

    # Wait for queue to empty
    q.join()

    # Stop workers
    for _ in range(num_threads):
        q.put(None)
    for t in thread_list:
        t.join()

    print("\nScan complete!")
    print("Open ports:", open_ports if open_ports else "None found")

if __name__ == "__main__":
    main()
