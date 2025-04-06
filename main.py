import pymongo

if __name__ == "__main__":
    print("welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['harry']
    collection = db['mySampleCollectionForHarry']
    dictionary = {'name': 'harry', 'marks':45}
    collection.insert_one(dictionary)

