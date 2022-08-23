import pandas
import json

if __name__ == '__main__':
    with open('content_instruct.json') as json_file:
        json_data = json.load(json_file)

[elem.update({'tagSets': [{'tags': None, 'systemTagName': None, 'displayTagName': None, 'fieldName': None}]})
 for elem in json_data if 'tagSets' not in elem.keys()]
df = pandas.json_normalize(
    json_data, ['tagSets', 'tags'], 'publishedId', errors='ignore')

df.to_csv('data.csv', mode='w')
