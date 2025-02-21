
# Proxy IP Collector

This repository contains a Python script that demonstrates how to fetch and store multiple unique IP addresses by making requests through a proxy service. The example is tailored to a hypothetical proxy provider (`proxy.example.com`), but you can easily adapt it for any other service by changing the relevant parameters.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Overview

This script:
1. Uses the [requests](https://pypi.org/project/requests/) library to make HTTP requests via a specified proxy.
2. Dynamically generates session IDs to help you attempt to obtain different IPs.
3. Checks for duplicates to ensure each stored IP is unique.
4. Exports the results (unique IPs) to a text file (`unique_ips.txt`).

---

## Features

- **Random Session IDs**: Helps rotate the proxy session (if the provider supports it).
- **Duplicate IP Check**: Prevents storing the same IP address more than once.
- **Configurable Proxy Credentials**: Easily change to any proxy host, port, username, or password.
- **Simple Output**: Saves the unique IP addresses to a text file.

---

## Prerequisites

1. **Python 3.7+** (any recent Python version should work).
2. **pip** (Python’s package manager).

---

## Installation

1. **Clone** or **Download** the repository:
   ```bash
   git clone https://github.com/ashishkprasad/proxies-tester
   cd proxies-tester
   ```
2. **Install Dependencies**:
   ```bash
   pip install requests
   ```

---

## Usage

1. **Open the Script** (`collect_unique_ips.py` or similar name) and **Update Proxy Credentials**:
   ```python
   proxy_host = "proxy.example.com"
   proxy_port = "8080"
   username = "myUsername"
   password = "myPassword"
   ```
   - If your provider doesn’t require session-based parameters, you can remove `_session-{session_id}` from the authentication string.

2. **Run the Script**:
   ```bash
   python collect_unique_ips.py
   ```
   - The script will attempt to retrieve 10 unique IP addresses.  
   - As it runs, you’ll see messages in the console indicating whether a new IP has been discovered or if a duplicate IP was found.

3. **Check the Results**:
   - After completion, `unique_ips.txt` will contain the final list of unique IP addresses.

---

## Customization

- **Number of IPs**: Edit the line `while len(ip_list) < 10:` to increase or decrease the number of IPs collected.
- **Session ID Length**: Adjust the `random_session_id(length=8)` function if you prefer a shorter or longer random string.
- **Timeout and Retry Delay**: Change `timeout=10` or `time.sleep(3)` to suit your network conditions.

---

## Troubleshooting

1. **Duplicate IPs**  
   - If you frequently get duplicates, consider increasing the delay between requests (`time.sleep(3)` to something larger).
   - Check with your proxy provider if they offer a larger pool or location-based rotation.

2. **Request Failures**  
   - Commonly due to incorrect credentials, invalid proxy host/port, or network issues.
   - Ensure your subscription or account with the proxy provider is active and configured correctly.

3. **Script Hangs or Times Out**  
   - Increase the `timeout=10` to a higher value if your connection is slow.

---

## License

This project is licensed under the [MIT License](LICENSE). You’re free to use, modify, and distribute it for personal or commercial purposes.

---

**Happy Coding!**  
Feel free to open an issue or submit a pull request if you have any improvements or suggestions.
