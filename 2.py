import os

def get_connected_ips():
    ips = []
    output = os.popen("arp -a").read()
    for line in output.split("\n"):
        if "dinƒmico" in line:
            line_parts = line.split()
            ip = line_parts[0]
            mac = line_parts[1]
            ips.append((ip, mac))
    return ips

connected_ips = get_connected_ips()

with open("regulardevices.txt", "w") as f:
    for ip, mac in connected_ips:
        f.write(f"{ip},{mac}\n")

print(connected_ips)