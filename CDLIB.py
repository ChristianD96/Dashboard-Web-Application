# Python library code

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
   # """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, aacuser, CSrules):
        # Initializing the MongoClient. This helps to access the MongoDB databases and collections. 
        # Init connect to mongodb without authentication
        # self.client = MongoClient('mongodb://localhost:54503'):
        # Init connect to mongodb with authentication
        #self.client = MongoClient('mongodb://%s:%s@localhost:54503/?authMechanism+DEFAULT&authSource=AAC'%(aacuser, CSrules))
        self.client = MongoClient('mongodb://localhost:54503')
        self.database = self.client['AAC']

# Method to implement the C(create) in CRUD
    def create(self, data):
        
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary  
            return True
        else:
            print("Nothing to save, because data parameter does not exist/empty")
            return False

# Method to implement the R(read) in CRUD
    def read(self, data):
        if data is not None:
            return self.database.animals.find_one(data) # returns only one document as a python dictionary
        else:
            print("Nothing to read, because data parameter is empty")
            return False
    
    def read_all(self, data):
        cursor = self.database.animals.find(data, {'_id':False} ) # return a curson whith a pointer to a list of results (Documents)
        return cursor
        
# Method to implement the U(update) in CRUD
    def update(self, data, newData):
        query = self.database.animals.find_one(data)
        
        if data is not None:
            if newData is not None:
                return self.database.animals.update_one(query, {"$set" : newData})
            else:
                raise Exception("Nothing to save, because new data parameter does not exist/empty")
        else:
            raise Exception("Nothing to save, because data parameter does not exist/empty")
            
# Method to implement the D(delete) in CRUD
    def delete_one(self, data):    
        if data is not None:
            self.database.animals.delete_one(data)
            return Exception("Deleted")
        else:
            print("Nothing to delete, because data parameter does not exist/empty")