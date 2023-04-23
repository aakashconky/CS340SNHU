from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        if username and password:
            print ("username and password are:", username, password)
            self.client = MongoClient('mongodb://%s:%s@localhost:55829/AAC' % (username, password))
            self.database = self.client['AAC']
            print ("Connection was successful")


    def create(self, data):
        """Inserts a new document into the animals collection"""
        if data:
            # inserts data as new object
            self.database.animals.insert_one(data)  # data should be dictionary
            return True
        else:
            # exception when parameter is empty
            raise Exception("Nothing to save, because data parameter is empty")

     #define read method
    """Returns all documents in the animals collection matching the given query"""
    def read_all(self, data):
        cursor = self.database.animals.find(data, {"_id" : False} ) #return a cursor which points to documents
        return cursor 
        
    def read(self,data):
        return self.database.animals.find(data) # return a document as a dictionary 

    def update(self, data, update_data):
        """Updates one or more documents matching the given query"""
        if data:
            result = self.database.animals.update_many(data, {"$set": update_data})
            print("Data Updated")
            return result.raw_result
        else:
            return "{}"

    def delete(self, data):
        """Deletes one or more documents matching the given query"""
        if data:
            result = self.database.animals.delete_many(data)
            print("Data Deleted")
            return result.raw_result
        else:
            return "{}"

    