import asyncio
import websockets
import json


async def chat():
    async with websockets.connect('ws://localhost:8765') as websocket:
        await websocket.send(json.dumps({'query': '你好', 'system': '请用二次元可爱语气和我说话'}))
        response = await websocket.recv()
        response = json.loads(response)
        print(response['response'])

asyncio.get_event_loop().run_until_complete(chat())