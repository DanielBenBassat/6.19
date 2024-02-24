import socket

IP = '127.0.0.1'
START_PORT = 20
END_PORT = 1024


def scan_ports(remote_host, start_port, end_port):
    open_ports = []
    timeout = 0.5

    for port in range(start_port, end_port+1):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((remote_host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports


def main():
    open_ports = scan_ports(IP, START_PORT, END_PORT)
    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(port)
    else:
        print("No open ports found.")


if __name__ == '__main__':
    main()

