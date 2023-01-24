import json
from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch(['http://localhost:9200'])

# Open the JSON data file
with open('pop2.json', 'r') as f:
    data = json.load(f)

# Iterate through the data and index each document
for doc in data:
    es.index(index='my_index', body=doc)

print("Data loaded into Elasticsearch successfully!")
