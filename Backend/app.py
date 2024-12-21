from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection string
client = MongoClient("mongodb+srv://matths:bVmVFKxNebbBdn0F@groupprojectmanager.vj2m4.mongodb.net/?retryWrites=true&w=majority&appName=GroupProjectManager")
db = client["GroupProjectManager"]

@app.route('/')
def hello_world():  
    # testing database
    # Reference a collection in your database
    collection = db.get_collection('tasks')
    
    # Check if the collection is empty
    document_count = collection.count_documents({})
    if document_count == 0:
        # Insert a test document if the collection is empty
        test_document = {"task": "Test Task", "description": "This is a test task to check the database connection"}
        collection.insert_one(test_document)
        return "Inserted a test document into the collection!"

    # Retrieve and display a document from the collection
    task = collection.find_one({})
    return f"Database is connected! Retrieved task: {task}"


if __name__ == '__main__':
    app.run()
