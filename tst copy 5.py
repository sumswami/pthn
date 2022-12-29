from simple_salesforce import Salesforce
import pandas
import json

sf = Salesforce(username='sumswami@deloitte.com.km',
                password='tst@2234', security_token='EQ9dfheUarRI8qj4o8NN391B')

data = sf.bulk.Knowledge__kav.query(
    "SELECT Id, prn__c FROM Knowledge__kav where publishStatus = 'Draft'")
df = pandas.DataFrame.from_dict(
    data, orient='columns').drop('attributes', axis=1)
df.rename(columns={'prn__c': 'publishedId'}, inplace=True)

if __name__ == '__main__':
    with open('content_instruct.json') as json_file:
        json_data = json.load(json_file)

[elem.update({'tagSets': [{'tags': None, 'systemTagName': None, 'displayTagName': None, 'fieldName': None}]})
 for elem in json_data if 'tagSets' not in elem.keys()]
df2 = pandas.json_normalize(
    json_data, ['tagSets', 'tags'], 'publishedId', errors='ignore')

df3 = pandas.merge(df, df2, on='publishedId', how='outer')
df3 = df3.rename(columns={'systemTagName': 'DataCategoryName'})
df3 = df3.assign(DataCategoryGroup='Online')

bulk_data = []
for row in df3.itertuples():
    d = row._asdict()
    bulk_data.append(d)

print(bulk_data)
