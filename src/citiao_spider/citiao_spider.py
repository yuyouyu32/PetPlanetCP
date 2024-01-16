import pandas as pd
from config import *

from bs4 import BeautifulSoup
import requests

from tqdm import tqdm
import math

def get_summary(url: str):
    response = requests.get(url, headers=headers, cookies=cookies)
    if response.status_code != 200:
        return '', False
    html_cont = response.text
    if '抱歉，百度百科尚未收录词条' in html_cont or 'baike.baidu.com/error.html' in html_cont:
        return '', False
    soup = BeautifulSoup(html_cont, 'lxml')

    # title = soup.title.string
    try:
        description = soup.find('meta', attrs={'name': 'description'})['content']
    except:
        return '', False
    return description, True


def get_describe(dataframe):
    for index, row in tqdm(dataframe.iterrows(), total=dataframe.shape[0]):
        possible_name = [row['name_cn'], row['province_name']+row['name_cn'], str(row['city_name'])+row['name_cn'], row['province_name'] + str(row['city_name']) + row['name_cn']]
        for name in possible_name:
            name = row['name_cn']
            if (isinstance(name, float) and math.isnan(name)) or  (isinstance(name, str) and name.strip()) == '' or name is None:
                dataframe.loc[index, 'des'] = None
                continue
            url = 'https://baike.baidu.com/item/' + name
            description, flag = get_summary(url)
            if flag:
                dataframe.loc[index, 'des'] = description
                break
        if not flag:
            print('未找到', row['name_cn'])
    return dataframe


if __name__ == "__main__":
    file_path = './data/Scenery.xlsx'
    save_path = './data/Scenery_des.xlsx'
    with pd.ExcelFile(file_path) as xls:
        sheet_names = xls.sheet_names

    with pd.ExcelWriter(save_path) as writer:
        for sheet_name in sheet_names:
            if sheet_name not in {'RightScenery'}: continue
            print(sheet_name, '开始爬取')
            dataframe = pd.read_excel(file_path, sheet_name=sheet_name)
            dataframe = get_describe(dataframe)
            dataframe.to_excel(writer, sheet_name=sheet_name, index=False)
            print(sheet_name, '爬取完成')