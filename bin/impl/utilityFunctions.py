import hashlib

#Function for Hashing/Fingerprinting record string
def hashString(record):
	hashVal = hashlib.md5(record.encode('utf-8'))
	return hashVal.hexdigest()


#Initialize Mongo Client with host & port
def initializeMongoConnection(host, port):
	from pymongo import MongoClient
	client = MongoClient(host, port)
	return client

#Return a combination String containing name,address,phone,website,lat,long values for hashing a record
def returnStringValueOfRecord(record):
	recordString=''
	recordString.encode('utf-8')
	if 'name_1' in record:
		recordString += record['name_1']
	if 'name_2' in record:
		recordString += record['name_2']
	if 'street_1' in record:
		recordString += record['street_1']
	if 'street_2' in record:
		recordString += record['street_2']
	if 'city' in record:
		recordString += record['city']
	if 'zip' in record:
		recordString += record['zip']
	if 'phone' in record:
		recordString += record['phone']
	if 'website' in record:
		recordString += record['website']
	if 'latitude' in record:
		recordString += record['latitude']
	if 'longitude' in record:
		recordString += record['longitude']
	return recordString

#Function to NormalizedRecord
def getNormalizedRecord(record):
	#Perform Steps Mentioned in Technical Document
	return record

#Function to compare two records by comparing the hashValue of their normalized versions
def compareRecords(record1, record2):
	if hashString(getNormalizedRecord(record1))==hashString(getNormalizedRecord(record2)):
		return true
	else:
		return false
