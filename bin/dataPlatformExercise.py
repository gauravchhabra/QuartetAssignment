import pymongo,urllib2,json
from impl.loadDataFromOpenData import loadAndSyncData,getTotalRecords
from impl.matchRecords import matchActiveClinics
from impl.preProcessData import getEnrichedAndNormalizedRecord
from impl.utilityFunctions import initializeMongoConnection

#Initialize MongoConnection & DB
client = initializeMongoConnection('localhost', 27017)
quartetDb = client.quartet

#Import Json from OpenData NYC
try:
    req = urllib2.Request("https://data.cityofnewyork.us/resource/8nqg-ia7v.json")
    #Check if empty json imported
    if req is None:
        raise IOError('The json containing data could not be found')
    opener = urllib2.build_opener()
    f = opener.open(req)
    json = json.loads(f.read())
except IOError as e:
    print str(e)
else:
    #Load All Records  & Update Data from OpenData NYC
    numOfUpdatedRecs = loadAndSyncData(quartetDb, json)
    numOfTotalRecords = getTotalRecords(quartetDb)
    print 'Number of total records:' + str(numOfTotalRecords)
    print 'Number of records updated:' + str(numOfUpdatedRecs)
    #Pre Process Data
    #record = getEnrichedAndNormalizedRecord(record)

    #Matching with existing records in Quartet to mark Active Clinics
    numberOfMatches = matchActiveClinics(quartetDb)

    print 'Number of records matched:' + str(numberOfMatches)
