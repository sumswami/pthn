import pandas
import json

if __name__ == '__main__':
    with open('content_instruct.json') as json_file:
        json_data = json.load(json_file)

[elem.update({'relatedContentList': [{'value': {'publishedId': None}}]})
 for elem in json_data if 'relatedContentList' not in elem.keys()]
df = pandas.json_normalize(
    json_data, ['relatedContentList'], 'publishedId', errors='ignore')

df.to_csv('data.csv', mode='w')
