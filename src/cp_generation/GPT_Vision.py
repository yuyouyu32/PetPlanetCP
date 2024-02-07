import base64
import requests
import os
import re
import pandas as pd
import glob
# from promts.post import *
# from prompts.A_scenery import *
from prompts.figure_des import *
import time
from tqdm import tqdm
import random

api_key = os.getenv('OPENAI_KEY')



def calculate_token_price(prompt_tokens, completion_tokens):
    return 7.13 * (0.01 * prompt_tokens / 1000 + 0.03 * completion_tokens / 1000)

def get_vision_cp(sys_prompt, task_prompt, image_path, n=3):
    # Function to encode the image to base64
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # Getting the base64 string for the image
    base64_image = encode_image(image_path)

    # Headers for the OpenAI API request
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Payload for the OpenAI API request
    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "system", 
                "content": sys_prompt
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": task_prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 100,
        "n": n
    }



    # Sending the request to the OpenAI API
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload).json()
    cost = calculate_token_price(response['usage']['prompt_tokens'], response['usage']['completion_tokens'])
    cp = [choice['message']['content'] for choice in response['choices']]
    # cp = '\n'.join(cp)

    # Returning the response
    return cp, cost


def scenery_post():
    scenery_path = '/home/jeriffli/PetPlanetCP/data/RightSceneryID.xlsx'
    img_root_path = '/home/jeriffli/PetPlanetCP/postcard'
    data = pd.read_excel(scenery_path)
    all_files = glob.glob(os.path.join(img_root_path, '*'))
    all_cost = 0 
    # Loop through each row in the DataFrame
    for index, row in tqdm(data.iterrows(), total=data.shape[0]):
        # Construct the prompt
        title = f"{row['province_name']} {row['name_cn']}"

        # Construct Prompt
        content_prompt = ContentPromptTemplate.format(content_req=content_req)
        random_examples = random.sample(examples, 3)
        examples_prompt = ExamplesPromptTemplate.format(examples="\n".join(random_examples))
        task_prompt = TaskPromptTemplate.format(content_prompt=content_prompt, examples_prompt=examples_prompt, title=title)
        sys_prompt = SystemPromptTemplate.format()
        # Create the regular expression pattern for image file name
        image_pattern = fr"r_{row['pid']}_{row['sid']}_[0-9]+\.(png|jpg|jpeg|bmp)"

        match_files = []
        for file_path in all_files:
            file_name = os.path.basename(file_path)
            if re.match(image_pattern, file_name):
                match_files.append(file_path)

        cps = ''
        for file_path in match_files:
            cp, cost = get_vision_cp(sys_prompt=sys_prompt, task_prompt=task_prompt, image_path=file_path)
            cp = '\n'.join(cp)
            cps += cp + '\n'
            all_cost += cost
        data.loc[index, 'cp'] = cps
        data.to_excel(scenery_path, index=False)
        time.sleep(1)


def scenery_chat():
    scenery_path = '/home/jeriffli/PetPlanetCP/data/{choice}.xlsx'
    img_root_path = '/home/jeriffli/PetPlanetCP/postcard'
    save_path = '/home/jeriffli/PetPlanetCP/data/LeftScenery_A.xlsx'
    data = pd.read_excel(scenery_path)
    all_files = glob.glob(os.path.join(img_root_path, '*'))
    all_cost = 0 
    # Loop through each row in the DataFramed
    sys_prompt = SystemPromptTemplate.format()
    for index, row in tqdm(data.iterrows(), total=data.shape[0]):
        # Construct the prompt
        local = row['province_name']
        name = row['name_cn']
        # Construct Prompt
        content_req_prompt = content_req.format(local=local, name=name)
        content_prompt = ContentPromptTemplate.format(content_req=content_req_prompt)
        random_examples = random.sample(examples, 3)
        examples_prompt = ExamplesPromptTemplate.format(examples="\n".join(random_examples))
        task_prompt = TaskPromptTemplate.format(content_prompt=content_prompt, name=name, local=local, examples_prompt=examples_prompt)
        # Create the regular expression pattern for image file name
        image_pattern = fr"l_{row['pid']}_{row['sid']}_[0-9]+\.(png|jpg|jpeg|bmp)"

        match_files = []
        for file_path in all_files:
            file_name = os.path.basename(file_path)
            if re.match(image_pattern, file_name):
                match_files.append(file_path)

        cps = ''
        for file_path in match_files:
            cp, cost = get_vision_cp(sys_prompt=sys_prompt, task_prompt=task_prompt, image_path=file_path)
            cp = '\n'.join(cp)
            cps += cp + '\n'
            all_cost += cost
        data.loc[index, 'cp'] = cps
        data.to_excel(save_path, index=False)
        time.sleep(random.randint(2, 3))


def scenery_des():
    choice = 'RightScenery'
    scenery_path = f'/home/jeriffli/PetPlanetCP/data/{choice}.xlsx'
    img_root_path = '/home/jeriffli/PetPlanetCP/postcard'
    save_path = f'/home/jeriffli/PetPlanetCP/data/{choice}_des.xlsx'
    data = pd.read_excel(scenery_path)
    all_files = glob.glob(os.path.join(img_root_path, '*'))
    all_cost = 0 
    # Loop through each row in the DataFramed
    sys_prompt = SystemPromptTemplate.format()
    for index, row in tqdm(data.iterrows(), total=data.shape[0]):
        # Construct the prompt
        local = row['province_name']
        name = row['name_cn']
        # Construct Prompt
        content_req_prompt = content_req.format()
        content_prompt = ContentPromptTemplate.format(content_req=content_req_prompt)
        task_prompt = TaskPromptTemplate.format(content_prompt=content_prompt, name=name)

        # Create the regular expression pattern for image file name
        image_pattern = fr"r_{row['pid']}_{row['sid']}_[0-9]+\.(png|jpg|jpeg|bmp)"

        match_files = []
        for file_path in all_files:
            file_name = os.path.basename(file_path)
            if re.match(image_pattern, file_name):
                match_files.append(file_path)

        cps = ''
        for file_path in match_files:
            cp, cost = get_vision_cp(sys_prompt=sys_prompt, task_prompt=task_prompt, image_path=file_path, n=3)
            cp = '\n'.join(cp)
            cps += cp + '\n'
            all_cost += cost
        data.loc[index, 'des'] = cps
        data.to_excel(save_path, index=False)
        time.sleep(random.randint(2, 3))
    print('Cost: ', all_cost)

if __name__ == '__main__':
    # scenery_post()
    # scenery_chat()
    scenery_des()
    
