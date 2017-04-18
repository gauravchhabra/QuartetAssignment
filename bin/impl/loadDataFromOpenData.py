from utilityFunctions import hashString,returnStringValueOfRecord

#Iterate through each record in OpenData and insert if it does not exist in our data store
def loadAndSyncData(quartetDb, json):
    clinicsCollection = quartetDb.clinics
    count = 0
    for record in json:
    	hashVal = hashString(returnStringValueOfRecord(record))
    	if clinicsCollection.find({'hashValue': hashVal}).count()==0:
            count += 1
            result = clinicsCollection.insert_one(record)
            clinicsCollection.update({'_id' : result.inserted_id}, {'$set': {'hashValue': hashVal}})

    return count

def getTotalRecords(quartetDb):
    return quartetDb.clinics.find().count()
