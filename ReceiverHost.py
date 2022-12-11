import socket
import string
import time
from Host import Host
import os

FILE_SIZE = 10485760
BUFFER_SIZE = 4096
DEFAULT_PORT = 6633

# h1: basically the SERVER for our purposes (establishes connection with h2)
class ReceiverHost(Host):

    def start_listening(self):
        self.sock.bind((self.ip, DEFAULT_PORT))
        self.sock.listen(10)

        while True:
            print("Attempting to establish connection. \n")
            other_host_conn, other_host_addr = self.sock.accept()
            print(other_host_addr)
            self.measure_latency(conn=other_host_conn)
            self.speed_test(conn=other_host_conn)
    
    def measure_latency(self, conn):
        print("Beginning Latency Test")
        latency = 0.0
        # Receiving 100 pings from h2 and summing calculated time difference
        for i in range(100):
            latency += self.receive_ping(conn)
            print(latency)
        ping = latency / 200
        conn.send(str(ping).encode("ascii"))

    def receive_ping(self, conn):
        start_time = time.time()

        msg = conn.recv(BUFFER_SIZE)
        conn.send(msg)

        end_time = time.time()
        
        return (end_time - start_time) * 1000

    def speed_test(self, conn):
        start_time = time.time()
        bytes_received = 0
        # Receiving file from h2 and writing locally
        with open("./uploadFile", "wb") as f:
            while True:
                data = conn.recv(BUFFER_SIZE)
                bytes_received += len(data)
                f.write(data)
                if bytes_received >= FILE_SIZE:
                    break

        end_time = time.time()
        speed = round(((FILE_SIZE / (end_time - start_time)) * 0.000001))
        print(f"Speed test complete, network speed is: {speed}Mbps")
        conn.send(str(speed).encode("ascii"))

if __name__ == '__main__':
    server = ReceiverHost("10.0.0.1")
    server.start_listening()