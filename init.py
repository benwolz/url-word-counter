from flask import Flask
from flask_pymongo import PyMongo
from redis import Redis
from rq import Queue
import os

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://mongo:27017/jobqueue")
mongo = PyMongo(app)
redis_conn = Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)
q = Queue(connection=redis_conn)
