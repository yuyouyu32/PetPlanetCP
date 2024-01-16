import pandas as pd
import websocket
import json
from langchain.prompts import PromptTemplate
from tqdm import tqdm

SystemPrompt = PromptTemplate.from_template("请你帮我整理或生成指定旅行地点的描述性文字")
AskPrompt = PromptTemplate.from_template("下面是我提供的一个旅行地点{place}描述：\n{des}\n 其中可能有一些无关旅行的信息，请你帮我整理一个旅行地点{place}的描述，剔除无关的信息，如占地面积，高度等与旅游无关的信息。如果你了解该地点有趣的描述也可以添加，最后不要用“总之{place}是一个值得一游的旅行目的地”这种没有信息的描述。")
GenPrompt = PromptTemplate.from_template("下面是我提供的一个旅行地点{place}, 请你根据你的相关旅行知识，请你帮我生成一个旅行地点{place}的描述，剔除无关的信息，如占地面积，高度，等等与旅游无关的信息，最后不要用“总之{place}是一个值得一游的旅行目的地”这种没有信息的描述。")
SummaryPrompt = PromptTemplate.from_template("下面是我提供的一个旅行地点{place}描述：\n{des}\n 请你用一两句话帮我总结一下这个旅行地点{place}的特色描述，大约200字左右。")

def chat(query):
    ws = websocket.create_connection("ws://localhost:8765")
    ws.send(json.dumps({'query': query, 'system': ''}))
    response = json.loads(ws.recv())
    # print(response['response'])
    ws.close()
    return response['response']

def process_describe(dataframe, save_path):
    for index, row in tqdm(dataframe.iterrows(), total=dataframe.shape[0]):
        place = row['name_cn']

        if str(row['city_name']) not in place:
            place = str(row['city_name']) + place
        if row['province_name'] not in place:
            place = row['province_name'] + place

        if row['des'] == '' or str(row['des']) == 'None' or '百度百科' in str(row['des']):
            query = GenPrompt.format(place=place)
            dataframe.loc[index, 'des'] = chat(query)
        else:
            des = row['des']
            query = AskPrompt.format(place=place, des=des)
            dataframe.loc[index, 'des'] = chat(query)
        with pd.ExcelWriter(save_path) as writer:
            dataframe.to_excel(writer, sheet_name=sheet_name, index=False)

def summary_describe(dataframe, save_path):
    for index, row in tqdm(dataframe.iterrows(), total=dataframe.shape[0]):
        place = row['name_cn']

        if str(row['city_name']) not in place:
            place = str(row['city_name']) + place
        if row['province_name'] not in place:
            place = row['province_name'] + place

        des = row['des']
        query = SummaryPrompt.format(place=place, des=des)
        dataframe.loc[index, 'des_s'] = chat(query)
        with pd.ExcelWriter(save_path) as writer:
            dataframe.to_excel(writer, sheet_name=sheet_name, index=False)

if __name__ == '__main__':
    file_path = '/home/jeriffli/PetPlanetCP/src/data/Scenery_des.xlsx'
    with pd.ExcelFile(file_path) as xls:
        sheet_names = xls.sheet_names

    for sheet_name in sheet_names:
        print(sheet_name, 'Start Summary...')
        dataframe = pd.read_excel(file_path, sheet_name=sheet_name)
        dataframe = dataframe.replace({None: ''})
        save_path = f'/home/jeriffli/PetPlanetCP/src/data/Scenery_des_{sheet_name}.xlsx'
        summary_describe(dataframe, save_path)
        print(sheet_name, 'Finished!')