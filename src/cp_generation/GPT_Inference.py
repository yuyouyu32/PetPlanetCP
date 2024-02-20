from openai import OpenAI
# from prompts.A_food import *
# from prompts.A_humanities import *
from prompts.BandC import *

import random
import pandas as pd
from tqdm import tqdm
import time

import os

Client = OpenAI(api_key = os.getenv('OPENAI_KEY'))
N = 3
Cost = 0



# GPT-4
def calculate_token_price(prompt_tokens, completion_tokens):
    return 7.13 * (0.01 * prompt_tokens / 1000 + 0.03 * completion_tokens / 1000)

def get_copywriter_from_GPT(sys_prompt: str, user_prompt: str, n: int = 1):
    """
    Description: 
        Get copywriter from GPT-4
    Args:
        sys_prompt (str): System prompt
        user_prompt (str): User prompt
        n (int, optional): Number of copywriters to generate. Defaults to 1.
    Returns:
        copywriters (list): List of copywriters
        cost (float): Cost price(￥) of generating copywriters
    """
    response = Client.chat.completions.create(
    model="gpt-4-0125-preview",
    messages=[
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt},
    ],
    n = n
    ).model_dump()
    cost = calculate_token_price(response['usage']['prompt_tokens'], response['usage']['completion_tokens'])
    copywriters = []
    for choice in range(n):
        copywriters.append(response['choices'][choice]['message']['content'])
    return copywriters, cost


def A_Generation():
    # file_path = '/home/jeriffli/PetPlanetCP/data/Food.xlsx'
    # save_path = '/home/jeriffli/PetPlanetCP/data/Food_A_{sheet_name}.xlsx'
    file_path = '/home/jeriffli/PetPlanetCP/data/Humanities.xlsx'
    save_path = '/home/jeriffli/PetPlanetCP/data/Humanities_A_{sheet_name}.xlsx'
    xlsx = pd.read_excel(file_path, sheet_name=None)
    sheet_names = xlsx.keys()

    for sheet_name in sheet_names:
        if sheet_name != 'RightHumanities': continue
        print(sheet_name, 'Start...')
        sys_prompt = SystemPromptTemplate.format()
        dataframe = xlsx[sheet_name]
        save_path_sheet = save_path.format(sheet_name=sheet_name)

        for index, row in tqdm(dataframe.iterrows(), total=dataframe.shape[0]):
            local = row['province_name']
            name = row['name_cn']
            description = row['des_s']
            content_req_result = content_req.format(local=local, name=name)
            content_prompt = ContentPromptTemplate.format(content_req=content_req_result)
            # random_examples = random.sample(examples, 3)
            # examples_prompt = ExamplesPromptTemplate.format(examples="\n".join(random_examples))
            task_prompt = TaskPromptTemplate.format(name=name, description=description, content_prompt=content_prompt, local=local)
            copywriters, cost = get_copywriter_from_GPT(sys_prompt=sys_prompt, user_prompt=task_prompt, n=3)
            copywriters = '\n'.join(copywriters)
            Cost += cost
            time.sleep(random.randint(1, 2))
            dataframe.loc[index, 'A_humanities'] = copywriters
            # Write your DataFrame to an Excel file and save
            dataframe.to_excel(save_path_sheet, sheet_name=sheet_name, index=False)
        print(sheet_name, 'Done!')
    print('Cost: ', Cost)

def BandC_Generation():
    key_point = "Left"
    scenery_path = f'/home/jeriffli/PetPlanetCP/data/{key_point}Scenery_A_kuma.xlsx'
    save_path = f'/home/jeriffli/PetPlanetCP/data/{key_point}Scenery_kuma_BandC.xlsx'
    data = pd.read_excel(scenery_path)
    data.fillna({'A': ""}, inplace=True)
    sys_prompt = SystemPromptTemplate.format()

    save_df = pd.DataFrame()
    all_cost = 0
    for index, row in tqdm(data.iterrows(), total=data.shape[0]):
        local = f"{row['province_name']} {row['name_cn']}"
        A = row['A']
        if A == '': continue
        content_req_prompt = content_req.format()
        content_prompt = ContentPromptTemplate.format(content_req=content_req_prompt)
        random_examples = random.sample(examples, 3)
        examples_prompt = ExamplesPromptTemplate.format(examples="\n".join(random_examples))
        task_prompt = TaskPromptTemplate.format(content_prompt=content_prompt, local=local, examples_prompt=examples_prompt, content=A)

        BandCs, cost = get_copywriter_from_GPT(sys_prompt=sys_prompt, user_prompt=task_prompt,  n=15)
        for BandC in BandCs:
            save_df = save_df._append({'local': local, 'A': A, 'QA': BandC}, ignore_index=True)
            save_df.to_excel(save_path, index=False)
        all_cost += cost
        time.sleep(random.randint(1, 2))
    print('Cost: ', all_cost)

def BandC_Generation_vision():
    key_point = "Right"
    scenery_path = f'/home/jeriffli/PetPlanetCP/data/{key_point}Scenery_A_kuma.xlsx'
    save_path = f'/home/jeriffli/PetPlanetCP/data/{key_point}Scenery_V_kuma_BandC.xlsx'
    ###
    from GPT_Vision import get_vision_cp
    import re
    import glob
    img_root_path = '/home/jeriffli/PetPlanetCP/postcard'
    all_files = glob.glob(os.path.join(img_root_path, '*'))
    ###
    data = pd.read_excel(scenery_path)
    data.fillna({'A': ""}, inplace=True)
    sys_prompt = SystemPromptTemplate.format()

    save_df = pd.DataFrame()
    all_cost = 0
    for index, row in tqdm(data.iterrows(), total=data.shape[0]):
        local = f"{row['province_name']} {row['name_cn']}"
        A = row['A']
        if A == '': continue
        content_req_prompt = content_req.format()
        content_prompt = ContentPromptTemplate.format(content_req=content_req_prompt)
        random_examples = random.sample(examples, 3)
        examples_prompt = ExamplesPromptTemplate.format(examples="\n".join(random_examples))
        ###
        task_prompt = TaskPromptTemplate.format(content_prompt=content_prompt, local=local, examples_prompt=examples_prompt)

        image_pattern = fr"r_{row['pid']}_{row['sid']}_[0-9]+\.(png|jpg|jpeg|bmp)"
        match_files = []
        for file_path in all_files:
            file_name = os.path.basename(file_path)
            if re.match(image_pattern, file_name):
                match_files.append(file_path)
        for file_path in match_files:
            BandCs, cost = get_vision_cp(sys_prompt=sys_prompt, task_prompt=task_prompt, image_path=file_path, n=5)
            for BandC in BandCs:
                save_df = save_df._append({'local': local, 'A': A, 'QA': BandC}, ignore_index=True)
                save_df.to_excel(save_path, index=False)
            all_cost += cost
            time.sleep(random.randint(1, 2))
    print('Cost: ', all_cost)

def BandC_Generation_food():
    food_path = '/home/jeriffli/PetPlanetCP/data/Humanities.xlsx'
    for key in ['Left', 'Mid', 'Right']:
        province_food_descriptions = {}
        food_des = pd.read_excel(food_path, sheet_name=f'{key}Humanities')
        for index, row in food_des.iterrows():
            province = row['province_name']
            description = row['des_s']
            
            if province not in province_food_descriptions:
                province_food_descriptions[province] = []
            
            province_food_descriptions[province].append(description)
        scenery_path = f'/home/jeriffli/PetPlanetCP/data/{key}Scenery_A_kuma.xlsx'
        save_path = f'/home/jeriffli/PetPlanetCP/data/{key}Scenery_Humanities_BandC.xlsx'
        data = pd.read_excel(scenery_path)
        data.fillna({'A': ""}, inplace=True)
        sys_prompt = SystemPromptTemplate.format()

        save_df = pd.DataFrame()
        all_cost = 0
        for index, row in tqdm(data.iterrows(), total=data.shape[0]):
            local = f"{row['province_name']} {row['name_cn']}"
            A = row['A']
            if A == '': continue
            content_req_prompt = content_req.format()
            content_prompt = ContentPromptTemplate.format(content_req=content_req_prompt)
            for des_s in province_food_descriptions.get(row['province_name'], []):
                random_examples = random.sample(examples, 3)
                examples_prompt = ExamplesPromptTemplate.format(examples="\n".join(random_examples))
                task_prompt = TaskPromptTemplate.format(content_prompt=content_prompt, local=local, examples_prompt=examples_prompt, des_s=des_s)
                BandCs, cost = get_copywriter_from_GPT(sys_prompt=sys_prompt, user_prompt=task_prompt, n=3)
                for BandC in BandCs:
                    save_df = save_df._append({'local': local, 'A': A, 'QA': BandC}, ignore_index=True)
                    save_df.to_excel(save_path, index=False)
                all_cost += cost
                time.sleep(random.randint(1, 2))
        print('Cost: ', all_cost)





if __name__ == '__main__':
    # A_Generation()
    # BandC_Generation()
    BandC_Generation_food()
    