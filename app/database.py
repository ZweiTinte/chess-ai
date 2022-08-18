# coding: utf-8
import codecs
import json

# load the data from file
def loadData(locationString):
	with codecs.open(locationString, encoding='utf-8') as json_file:
		return json.load(json_file)
	
# writes the data to file
def writeData(locationString, data):
	with codecs.open(locationString, "w", encoding='utf-8') as outfile:
		json.dump(data, outfile, ensure_ascii=False)
	removeSpaces(locationString)

# removes all spaces in a file
def removeSpaces(locationString):
	lines = getLines(locationString)
	lines = [line.replace(" ", "") for line in lines]
	with codecs.open(locationString, "w", encoding='utf-8') as f:
		f.writelines(lines)

# get all lines from a file
def getLines(locationString):
	with codecs.open(locationString, "r", encoding='utf-8') as f:
		return f.readlines()