import socket

'''
General class for a Host in the network.
'''

FILE_SIZE = 10485760

class Host:
    def __init__(self, ip):
        self.ip = ip
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.create_test_file()

    def create_test_file(self):
        with open("./testFile", "wb") as file:
            file.seek(10485760 - 1)
            file.write(b"\0")
            file.close()