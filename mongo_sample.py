import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Choose a database and a collection
db = client["mydatabase"]
collection = db["mycollection"]

# Define a JSON object
my_json = {
    "name": "John Doe",
    "age": 35,
    "city": "New York"
}

# Insert the JSON object into the collection
collection.insert_one(my_json)

# Check that the JSON object has been inserted
print("JSON object saved:", collection.find_one({"name": "John Doe"}))

# Close the connection
client.close()
