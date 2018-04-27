import elasticsearch
from elasticsearch import helpers
import pandas as pd

import fire

def bulk_load(filename='./isrc_lookup.csv', indexname='isrc', typename='track'):
    """
    Import csv data into ES
    """
    df1 = pd.read_csv(filename, sep='\t', chunksize=1000, encoding='utf-8')
    es = elasticsearch.Elasticsearch('http://elasticsearch:9200', cluster='docker-cluster')
    for chunk in df1:
        tmp = chunk.to_dict(orient="records")
        actions = [{
            '_index': indexname,
            '_type': typename,
            '_source': doc
        } for doc in tmp]
        helpers.bulk(es, actions)


if __name__ == '__main__':
    fire.Fire(bulk_load)
