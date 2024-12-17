import subprocess
import platform

def ping_host(ip):
    """
    Pings a single host to check if it is active.
    Returns True if the host responds, otherwise False.
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", ip]
    try:
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return output.returncode == 0
    except Exception as e:
        print(f"Error pinging {ip}: {e}")
        return False

def get_ips_from_user():
    """
    Prompts the user to input a range or list of IPs.
    Returns a list of IP addresses to scan.
    """
    print("Enter the IPs you want to scan.")
    print("1. Enter a range (e.g., 192.168.1.1-192.168.1.10)")
    print("2. Enter multiple IPs separated by commas (e.g., 192.168.1.1,192.168.1.2,192.168.1.3)")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        ip_range = input("Enter the range: ").strip()
        start_ip, end_ip = ip_range.split("-")
        base_ip = ".".join(start_ip.split(".")[:3])
        start = int(start_ip.split(".")[-1])
        end = int(end_ip.split(".")[-1])
        return [f"{base_ip}.{i}" for i in range(start, end + 1)]
    elif choice == "2":
        ip_list = input("Enter the IPs separated by commas: ").strip()
        return [ip.strip() for ip in ip_list.split(",")]
    else:
        print("Invalid option. Please try again.")
        return get_ips_from_user()

def ping_sweep(ips):
    """
    Performs a ping sweep on the specified IPs.
    :param ips: List of IP addresses.
    :return: List of active IP addresses.
    """
    active_hosts = []
    print(f"Starting ping sweep on {len(ips)} IP(s)...\n")
    
    for ip in ips:
        if ping_host(ip):
            print(f"{ip} is active")
            active_hosts.append(ip)
        else:
            print(f"{ip} is not reachable")
    
    print("\nPing sweep complete.")
    print(f"Active hosts: {active_hosts}")
    return active_hosts

if __name__ == "__main__":
    # Get IPs from user
    ips_to_scan = get_ips_from_user()

    # Perform the ping sweep
    active_hosts = ping_sweep(ips_to_scan)

    # Adding the signature line
    print("\nScript made with ❤️  by Bakhtiyar Ahmad ")
