import requests
import time
import random
import string


def random_session_id(length=8):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))


# Suppose your provider is "ProxyExample" and requires user:pass
proxy_host = "proxy.example.com"
proxy_port = "8080"
username = "myUsername"
password = "myPassword"

ip_list = set()

while len(ip_list) < 10:
    session_id = random_session_id()

    # Hypothetical scenario: if the provider supports session-based IP
    proxy_auth = f"{username}:{password}_session-{session_id}"
    # If no session parameter is needed, just use user:pass.

    proxy = {
        "http": f"http://{proxy_auth}@{proxy_host}:{proxy_port}",
        "https": f"http://{proxy_auth}@{proxy_host}:{proxy_port}",
    }

    try:
        response = requests.get("https://ifconfig.me", proxies=proxy, timeout=10)
        ip = response.text.strip()

        if ip in ip_list:
            print(f"Duplicate IP {ip}, retrying...")
        else:
            ip_list.add(ip)
            print(f"New IP {ip} added. Total unique IPs: {len(ip_list)}")

        time.sleep(3)

    except Exception as e:
        print(f"Request failed: {e}")
        time.sleep(3)

with open("unique_ips.txt", "w") as file:
    for ip in ip_list:
        file.write(ip + "\n")

print(f"Saved {len(ip_list)} unique IPs to unique_ips.txt")
