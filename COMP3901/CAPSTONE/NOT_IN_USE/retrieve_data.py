from pymongo import MongoClient

# Connect to MongoDB
uri = "mongodb+srv://SICI_ADMIN:JykKRTankchklZhJ@cluster0.nputgqm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
database = client.SICI_DATA
collection = database.Records
score=0

coordinates_to_check = [
    [67, 121, 193, 277],
    [167, 142, 231, 256],
    [168, 141, 231, 257]
]

query = {"$or": [{"V_Coordinates": coord} for coord in coordinates_to_check]}#Checking if the coordinates we want are in the database

# Retrieve the most recent ten entries
recent_entries = collection.find().sort([("_id", -1)]).limit(10)

# Find documents matching any of the specified coordinates
matching_entries = collection.find(query)

# Count the number of matching documents
matching_entries_count = collection.count_documents(query)

# Check if any matching documents were found
if matching_entries_count > 0:
    score+=1
    print(matching_entries)
