import pandas as pd
import Feature
from tqdm import tqdm
import warnings
import time
import requests

normal = pd.read_csv('majestic_million.csv')
normal = normal[:2500]
phishing = pd.read_csv('data.csv')
url_list = []

for i in normal["Domain"]:
    url_list.append(f'https://{i}')
    
normal['url'] = url_list
normal['label'] = 1
normal = normal[['url','label']]
df = pd.concat([normal, phishing], axis = 0)
data_list = []

for url in tqdm(df['url']):
    try:
        data = Feature.total_feature(url)
    except Exception as e:
        data = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
    
    for list_value in data:
        data_list.append(list_value)

data = pd.DataFrame(data_list, df['label'])

data.to_csv('c:\workspace\Data-pipeline\ml_data.csv')