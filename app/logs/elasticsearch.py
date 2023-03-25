from elasticsearch import Elasticsearch
from flask import Flask, jsonify, request


es = Elasticsearch([{'host': 'elasticsearch', 'port': '9200', "scheme": "http"}], basic_auth=('root', 'pass'))

def log_request():
    data = {
        'url': request.url,
        'method': request.method,
        'headers': dict(request.headers),
        'data': request.get_data(as_text=True),
        'remote_addr': request.remote_addr
    }
    es.index(index='api-logs', body=data)


def all_logs():
    results = es.search(index='api-logs')
    logs = [hit['_source'] for hit in results['hits']['hits']]
    
    return jsonify(logs)
