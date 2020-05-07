import paramiko


class SSH:

    def __init__(self, host: str, ip_addr: str):
        self.host = host
        self.address = ip_addr

    def ssh_connection(self):
