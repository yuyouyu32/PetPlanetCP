from promts.kuma import *
import random
import pandas as pd
import websocket

from tqdm import tqdm
import json


def get_copywriter_from_Qwen(user_prompt, sys_prompt):
    ws = websocket.create_connection("ws://localhost:8765")
    ws.send(json.dumps({'query': user_prompt, 'system': sys_prompt}))
    response = json.loads(ws.recv())
    ws.close()
    return response['response']

def generate_cp(dataframe, save_path):
    sys_prompt = SystemPromptTemplate.format()
    content_prompt = ContentPromptTemplate.format(content_req=content_req)
    for index, row in tqdm(dataframe.iterrows(), total=dataframe.shape[0]):
        province = str(row['province_name'])
        city = str(row['city_name'])
        place = str(row['name_cn'])
        description = str(row['des_s'])
        if not place or place == '' or place is None:
            dataframe.loc[index, 'cp'] = None
            continue
        title = place
        if city not in title: title = city + title
        if province not in title: title = province + title
        random_examples = random.sample(examples, 3)
        examples_prompt = ExamplesPromptTemplate.format(examples="\n".join(random_examples))
        task_prompt = TaskPromptTemplate.format(title=title, description=description, content_prompt=content_prompt, examples_prompt=examples_prompt)
        copywriters = get_copywriter_from_Qwen(sys_prompt=sys_prompt, user_prompt=task_prompt)
        dataframe.loc[index, 'kuma'] = copywriters
        # Save the dataframe to excel
        with pd.ExcelWriter(save_path) as writer:
            dataframe.to_excel(writer, sheet_name=sheet_name, index=False)


        

if __name__ == '__main__':
    file_path = '/home/jeriffli/PetPlanetCP/src/data/Scenery_des_s.xlsx'
    with pd.ExcelFile(file_path) as xls:
        sheet_names = xls.sheet_names

    for sheet_name in sheet_names:
        print(sheet_name, 'Start Generation...')
        dataframe = pd.read_excel(file_path, sheet_name=sheet_name)
        dataframe = dataframe.replace({None: ''})
        save_path = f'/home/jeriffli/PetPlanetCP/src/data/Scenery_CP_{sheet_name}.xlsx'
        generate_cp(dataframe, save_path)
        print(sheet_name, 'Finished!')       