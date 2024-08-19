import socket
import nmap

class IoTScanner:
    def __init__(self, network_ip):
        self.network_ip = network_ip
        self.scanner = nmap.PortScanner()

    def scan_network(self):
        scan_results = {}
        try:
            self.scanner.scan(hosts=self.network_ip, arguments='-p 1-65535')
            for host in self.scanner.all_hosts():
                scan_results[host] = self.scanner[host]['tcp']
        except Exception as e:
            scan_results['error'] = str(e)
        return scan_results
