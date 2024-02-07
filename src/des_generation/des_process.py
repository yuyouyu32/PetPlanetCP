import pandas as pd
import websocket
import json
from tqdm import tqdm

from prompts.Humanities import SystemPrompt, AskPrompt, GenPrompt, SummaryPrompt



def chat(query, sys: str=''):
    ws = websocket.create_connection("ws://localhost:8765")
    ws.send(json.dumps({'query': query, 'system': sys}))
    response = json.loads(ws.recv())
    # print(response['response'])
    ws.close()
    return response['response']

def process_describe(dataframe, save_path):
    for index, row in tqdm(dataframe.iterrows(), total=dataframe.shape[0]):
        key = row['name_cn']

        if str(row['city_name']) not in key:
            key = str(row['city_name']) + key
        if row['province_name'] not in key:
            key = row['province_name'] + key

        if row['des'] == '' or str(row['des']) == 'None' or '百度百科' in str(row['des']):
            query = GenPrompt.format(key=key)
            dataframe.loc[index, 'des'] = chat(query, sys=SystemPrompt.format())
        else:
            des = row['des']
            query = AskPrompt.format(key=key, des=des)
            dataframe.loc[index, 'des'] = chat(query, sys=SystemPrompt.format())
        with pd.ExcelWriter(save_path) as writer:
            dataframe.to_excel(writer, sheet_name=sheet_name, index=False)

def summary_describe(dataframe, save_path):
    for index, row in tqdm(dataframe.iterrows(), total=dataframe.shape[0]):
        key = row['name_cn']

        if str(row['city_name']) not in key:
            key = str(row['city_name']) + key
        if row['province_name'] not in key:
            key = row['province_name'] + key

        des = row['des']
        query = SummaryPrompt.format(key=key, des=des)
        dataframe.loc[index, 'des_s'] = chat(query)
        with pd.ExcelWriter(save_path) as writer:
            dataframe.to_excel(writer, sheet_name=sheet_name, index=False)

if __name__ == '__main__':
    file_path = '/home/jeriffli/PetPlanetCP/src/data/Humanities.xlsx'
    with pd.ExcelFile(file_path) as xls:
        sheet_names = xls.sheet_names

    for sheet_name in sheet_names:
        print(sheet_name, 'Start...')
        dataframe = pd.read_excel(file_path, sheet_name=sheet_name)
        dataframe = dataframe.fillna('')
        save_path = f'/home/jeriffli/PetPlanetCP/src/data/Humanities_s_{sheet_name}.xlsx'
        # process_describe(dataframe, save_path)
        summary_describe(dataframe, save_path)
        print(sheet_name, 'Finished!')