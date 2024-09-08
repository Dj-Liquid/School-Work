#PREMATURE DANGER SCORE ALGORITHM
import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]
detections = []
attributes = []

def AttribToDB(attributes):
	#attributes will be an array consisting of an ID and two separate arrays,
    #[0] being the ID
	#[1] being the colour of the top then bottom of the person
	#[2] being the location values of the individual
    if attributes:
        if collection.find_one({"ID": attributes[0]}):
            collection.update_one({"ID": attributes[0]}, {"$set": {"ClothingColours": attributes[1], "LastSeen": attributes[2]}})
        else:
            collection.insert_one({"ID": attributes[0], "ClothingColours": attributes[1], "LastSeen": attributes[2]})
        
        
        
def CalcScore(detections):
    #detections will be an array containing what is detected on the person
    #and how many
    if not detections:
        danger_score = 0
    else:
        if detections[0]==0:
            danger_score = 10
        elif detections[0] ==1:
            danger_score = 7
        #weapons give an automatic score
        #This score is then acted on by a factor of distance from a specified area
        #so the score will be multiplied by a number from .1-1/1+
        #It will also be acton on by how long they stay in a particular area
        pass


    return danger_score
    

   