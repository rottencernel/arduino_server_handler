import asyncio
import websockets


async def send_signal_to_server():
    async with websockets.connect("ws://localhost:8000/a") as websocket:
        with open('data.txt', 'r') as file:
            mess = file.read()
            await websocket.send(mess)
        await websocket.recv()


while True:
    try:
        asyncio.run(send_signal_to_server())
    except:
        print('ups')