import socket

def scan(targets, ports):
    for port in range(1, ports):
        scan_port(targets, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print('[+]port-open' + str(port));
        sock.close();
    except:
        print('[-]port-closed' +str(port))

targets = input("[*] Enter target to scan: (split them by , ): ")
ports = input("[*] Enter How many ports you want to scan: ")
if ',' in targets:
    print("[*] Scanning multiple targets")
    for ip_address in targets.split(','):
        scan(ip_address.strip(' '), ports)
else:
    scan(target, ports)