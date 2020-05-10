import paramiko

# ssh-keygen -t rsa
# Enter file path in which to save key
#ssh-copy-id -i ~/.ssh/mykey name@host.org


class SSH:

    def __init__(self, host: str, ip_addr: str):
        self.host = host
        self.address = ip_addr

    def ssh_connection(self):
