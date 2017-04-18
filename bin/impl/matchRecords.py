from utilityFunctions import hashString,returnStringValueOfRecord
#Compare and Store Matches
#Iterate through all records in Quartet DB to be matched with imported data to mark active clinics
def matchActiveClinics(quartetDb):

    existingListCollection = quartetDb.quartetClinics
    clinicsCollection = quartetDb.clinics
    matchesCollection = quartetDb.matches
    count = 0
    numberRecordsProcessed = 0
    for quartetRecord in existingListCollection.find():
        numberRecordsProcessed += 1
        hashVal = hashString(returnStringValueOfRecord(quartetRecord))
        #Check for match by comparing hashValue of record
        clinicRecord = clinicsCollection.find_one({'hashValue': hashVal})
        if clinicRecord is not None:
            #Create key,value pair string with Ids from both collections
            matchPairIds = str(quartetRecord['_id']) + ',' + str(clinicRecord['_id'])
            #Insert match if it doesn't exist with confidence score 100 since it's an exact match
            matches = matchesCollection.find({'matchPair': matchPairIds})
            if matches.count()==0:
                count += 1
                matchesCollection.insert({'matchPair' : matchPairIds , 'confidenceScore': 100.0})

    print 'Total Number of Records Processed' + str(numberRecordsProcessed)
    return count
