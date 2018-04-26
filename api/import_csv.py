import elasticsearch
from elasticsearch import helpers
import pandas as pd


def bulk_load(filename='./isrc_lookup.csv'):
    df1 = pd.read_csv(filename, sep='\t', chunksize=1000)
    es = elasticsearch.Elasticsearch('http://localhost:9200', cluster='docker-cluster')
    for chunk in df1:
        tmp = chunk.to_dict(orient="records")
        actions = [{
            '_index': 'isrcs',
            '_type': 'track',
            '_source': doc
        } for doc in tmp]
        helpers.bulk(es, actions)


if __name__ == '__main__':
    bulk_load()
