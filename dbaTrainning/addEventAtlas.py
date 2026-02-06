from pymongo import MongoClient
from flask import Flask
app = Flask(__name__)

client = MongoClient('mongodb+srv://khan786aakib92_db_user:95480akib@cluster0.fmme27p.mongodb.net/?appName=Cluster0')

eventdb = client['eventdb']

# addEvent collection 

addEvent = eventdb['addEvent']  

# add the single event to the collection
addEvent.insert_one({
    "eventName": "Tech Conference 2024",
    "eventDate": "2024-09-15",
    "eventLocation": "San Francisco, CA"
})