import socket
import string
import time
import random
import secrets
from Host import Host

FILE_SIZE = 10485760
BUFFER_SIZE = 4096
DEFAULT_PORT = 6633

# h2: basically the CLIENT
class SenderHost(Host):
    def __init__(self, ip, otherIp):
        Host.__init__(self, ip)
        self.otherIp = otherIp

    def establish_connection(self):
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Attempting to establish connection with other host...")
        self.server_sock.connect((self.otherIp, DEFAULT_PORT))

    def send_ping(self, packet_content):
        self.server_sock.send(packet_content)
        self.server_sock.recv(BUFFER_SIZE)

    def latency_test(self):
        for i in range(100):
            self.send_ping(b"\x00" + secrets.token_bytes(62) + b"\x00")
        ping = self.server_sock.recv(BUFFER_SIZE).decode("ascii")
        print("Ping test complete")

        return ping

    def get_network_speed(self):
        print("Network Speed Test")
        upload_file = open("./testFile", "rb")
        buffer = upload_file.read()
        # upload file
        while buffer:
            self.server_sock.send(buffer)
            buffer = upload_file.read()

        upload_file.close()
        speed = self.server_sock.recv(BUFFER_SIZE).decode("ascii")
        return speed

if __name__ == '__main__':
    server = SenderHost("10.0.0.2", "10.0.0.1")
    server.establish_connection()
    print(f"Latency test complete, it took: {server.latency_test()}s")
    print(f"Speed test complete, connection upload and download speed is: {server.get_network_speed()}Mbps")