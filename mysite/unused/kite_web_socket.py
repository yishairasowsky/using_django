import socket
import websockets
import asyncio
import traceback

NAME = socket.gethostname()

print(NAME)

IP = socket.gethostbyname(NAME)

print(IP)


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect(('8.8.8.8',53))
    IP = s.getsockname()[0]

print(IP)

async def register_client(websocket, _):

    async for message in websocket:

        print(message)


if __name__ == '__main__':

    start_server = websockets.serve(register_client, IP, 1111)

    asyncio.get_event_loop().run_until_complete(start_server)

    asyncio.get_event_loop().run_forever()

pass