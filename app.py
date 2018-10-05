from typing import *
import socket

def algorithm(n: int) -> int:
    return n + 42

Address = Tuple[str, int]

async def handler(client: socket.socket) -> None:
    while True:
        request: bytes = await async_recv(client, 100)
        if not request.strip():
            client.close()
            return
        number = int(request)
        result = algorithm(number)
        await async_send(client, f'{result}\n'.encode('ascii'))

async def server(address: Address) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = async_accept(sock)
        print(f'Connection from{addr}')
        add_task(handler(client))

Task = TypeVar('Task')
TASKS: Deque[Task] = deque()

def add_task(task: Task) -> None:
    TASKS.append(task)

def run() -> None:
    pass

add_task(server(('localhost', 30303)))
run()
