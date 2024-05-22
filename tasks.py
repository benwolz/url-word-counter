# tasks.py
import requests
from init import mongo

def count_words_at_url(url):
    resp = requests.get(url)
    word_count = len(resp.text.split())
    mongo.db.results.insert_one({'url': url, 'word_count': word_count})
    return word_count
