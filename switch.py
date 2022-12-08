import socket
import string
import random
import time
from _thread import start_new_thread

class Switch:
    def __init__(self, ip_addr, port):
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_addr = ip_addr

  