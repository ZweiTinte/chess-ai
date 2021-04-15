# coding: utf-8
import codecs
from random import shuffle, randint
import sys, json, datetime

# load the data from file
def loadData(locationString):
	with codecs.open(locationString, encoding='utf-8') as json_file:
		data = json.load(json_file)
	return data
	
# writes the data to file
def writeData(locationString, data):
	with codecs.open(locationString, "w", encoding='utf-8') as outfile:
		json.dump(data, outfile, ensure_ascii=False)

# get all lines from a file
def getLines(locationString):
	with open(locationString, "r") as f:
		return f.readlines()

# removes all spaces in a file
def removeSpaces(locationString):
	lines = getLines(locationString)
	lines = [line.replace(" ", "") for line in lines]
	with open(locationString, "w") as f:
		f.writelines(lines)
