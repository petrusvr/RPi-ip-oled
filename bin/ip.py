#!/usr/bin/env python3

import socket
import psutil

class IpReader:
    
    @staticmethod
    def getIps():
        addrs = psutil.net_if_addrs()
        ips = {}
        for name, addrs in addrs.items():
            if name == "lo":
                continue
            ips[name] = ""
            
            for addr in addrs:
                if addr.family == socket.AddressFamily.AF_INET:
                    ips[name] = addr.address
        return ips


def main():
    print('Currently assigned IPs:')
    ips = IpReader.getIps()
    for interface, ip in ips.items():
        print(interface,":",ip)


if __name__ == "__main__":
    main()