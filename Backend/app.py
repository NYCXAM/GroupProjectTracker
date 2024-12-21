from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
import os
from dotenv import load_dotenv
import certifi

load_dotenv('config.env')

app = Flask(__name__)
CORS(app)

# MongoDB connection string
MONGODB_URL = os.getenv('MONGODB_URL')
client = MongoClient(MONGODB_URL, tlsCAFile=certifi.where())
db = client["GroupProjectManager"]

@app.route('/create_project', methods=['POST'])
def create_project():
    # Get project data from request
    project_data = request.json

    # Insert project data into database
    project = {
        "name": project_data["name"],
        "deadline":  project_data["deadline"],
        "num_members": project_data["num_members"],
        "tasks": []
    }

    result = db.projects.insert_one(project)

    # Return success message with project ID
    return jsonify({"message": "Project created successfully!", "project_id": str(result.inserted_id)}), 201



if __name__ == '__main__':
    app.run(debug = True, host='localhost', port=5000)
