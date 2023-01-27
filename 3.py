import os
import time


def get_connected_ips():
    ips = []
    output = os.popen("arp -a").read()
    for line in output.split("\n"):
        if "dinƒmico" in line:
            line_parts = line.split()
            ip = line_parts[0]
            mac = line_parts[1]
            ips.append({'ip': ip, 'mac': mac})
    return ips


def check_new_devices():
    connected_ips = get_connected_ips()
    with open("regulardevices.txt", "r") as f:
        regular_devices = [line.strip().split(',') for line in f.readlines()]
    regular_devices = [{'ip': device[0], 'mac': device[1]} for device in regular_devices]
    for device in connected_ips:
        if device not in regular_devices:
            print(f"WARNING: {device['ip']} - {device['mac']} is not a regular device.")


while True:
    check_new_devices()
    time.sleep(30)
