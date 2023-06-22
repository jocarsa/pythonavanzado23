import asyncio
import websockets
import json

connected_clients = set()

async def handle_connection(websocket, path):
    connected_clients.add(websocket)
    try:
        await websocket.send('Welcome to the server!')
        async for message in websocket:
            json_message = json.loads(message)
            print('Received message:', json_message)
            await broadcast_message(json_message)
    finally:
        connected_clients.remove(websocket)

async def broadcast_message(message):
    json_message = json.dumps(message)
    for client in connected_clients:
        await client.send(json_message)

start_server = websockets.serve(handle_connection, '192.168.1.74', 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
