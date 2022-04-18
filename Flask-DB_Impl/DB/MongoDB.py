import pymongo


def getStudentData():
    client = pymongo.MongoClient("mongodb+srv://vyaramwar:Saptgiri12@vaibhavycluster.llbsh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db2=client['mongotest']
    ineuron_collection = db2["ineuron_collection"]
    result=[]
    for i in ineuron_collection.find():
        result.append(i)

    return result