import json
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client['flight_status_db']
collection = db['flights']

# Load data from JSON file
data_file_path = os.path.join(os.path.dirname(__file__), '../data/flight_data.json')
with open(data_file_path, 'r') as file:
    data = json.load(file)

# Insert data into MongoDB
collection.insert_many(data)

print("Data inserted successfully")
