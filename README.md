# Ping Sweep Script

A simple Python script to perform a **ping sweep** to check the status of multiple IP addresses. This script allows users to scan a range of IP addresses or a list of IPs to determine which ones are active or reachable.

### Features
- Ping multiple IP addresses (either range or list).
- Prints the status of each IP (active or not reachable).
- Includes a simple and clean output.
- User-friendly interface to input IPs or ranges.

### Prerequisites
- Python 3.x
- `subprocess` module (Python's standard library)
- `platform` module (Python's standard library)

### How to Use
1. Clone or download the repository.
2. Open a terminal and navigate to the folder containing the script.
3. Run the script:
   ```bash
   python ping_sweep.py
   ```
4. The script will prompt you to input a range of IPs or a list of IPs separated by commas. After inputting the IPs, the script will perform the ping sweep and display the status of each IP.

### Example

```bash
Enter the IPs you want to scan.
1. Enter a range (e.g., 192.168.1.1-192.168.1.10)
2. Enter multiple IPs separated by commas (e.g., 192.168.1.1,192.168.1.2,192.168.1.3)
Choose an option (1 or 2): 1
Enter the range: 192.168.1.1-192.168.1.5

Starting ping sweep on 5 IP(s)...

192.168.1.1 is active
192.168.1.2 is not reachable
192.168.1.3 is active
192.168.1.4 is active
192.168.1.5 is not reachable

Ping sweep complete.
Active hosts: ['192.168.1.1', '192.168.1.3', '192.168.1.4']
```


### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Script made with ❤️ by Bakhtiyar Ahmad