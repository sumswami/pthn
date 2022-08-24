import pandas
import json

if __name__ == '__main__':
    with open('content_instruct.json') as json_file:
        json_data = json.load(json_file)

df = pandas.json_normalize(
    json_data)

df.to_csv('data.csv', mode='w')
