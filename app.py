from typing import *
import socket

def algorithm(n: int) -> int:
    return n + 42

Address = Tuple[str, int]

def handler(client: socket.socket) -> None:
    pass

def server(address: Address) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print(f'Connection from{addr}')
        handler(client)
