from scapy.all import *


IP_ADD = "127.0.0.1"
START_PORT = 20
END_PORT = 1024
TIMEOUT = 0.5


def scan_ports(start_port, end_port):

    for port in range(start_port, end_port+1):

        syn_packet = IP(dst=IP_ADD)/TCP(dport=port, flags="S")
        response = sr1(syn_packet, timeout=TIMEOUT, verbose=0)
        # If response is none or has RST flag port is closed
        if response is None:
            print(".")
        elif TCP in response and response[TCP].flags & 0x04:
            print(".")
        # If responsehas SYN+ACK flags, port is open
        elif TCP in response and response[TCP].flags & 0x12:
            print(f"Port {port} is open.")
        else:
            print(".")


def main():
    scan_ports(START_PORT, END_PORT)


if __name__ == '__main__':
    main()


