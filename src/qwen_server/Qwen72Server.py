from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig
import asyncio
import websockets
import json
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3"


tokenizer = AutoTokenizer.from_pretrained("/home/jeriffli/Qwen_Chat", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("/home/jeriffli/Qwen_Chat", device_map="auto", trust_remote_code=True).eval()

async def handle(websocket, path):
    async for message in websocket:
        data = json.loads(message)
        query = data.get('query', '')
        system = data.get('system', '')
        if not system:
            response, history = model.chat(tokenizer, query = query, history=None, system=system)
        else:
            response, history = model.chat(tokenizer, query = query, history=None)
        print('query: ' + query)
        print('response: ' + response)
        print('-' * 20)
        await websocket.send(json.dumps({'response': response}))

start_server = websockets.serve(handle, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()