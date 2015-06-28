import json,jsonobj
from random import randint

files = []

with open('randomnum.txt', 'r') as f:
    for row in f:
        files.append(row.strip())
    print files

# Generate a random file name
def randomfilename():
    rangestart = 10
    rangeend = 99
    randnum = randint(rangestart, rangeend)
    print "random file name is :" + str(randnum)
    return randnum

# Check if that number has been used already
def checkNum(num):
    if num in files:
        print "checknum is False"
        return False
    else:
        print "checknum is True"
        return True

# Updates the index (a plaintext file that keeps track of all the maps that have been created)
def updateTxtFile(fileName):
    name = str(fileName) + "\n"
    print name
    with open("randomnum.txt", "a") as outfile:
        print "Text file updated"
        outfile.write(name)
        print " After Text file updated"

# Creates a JSON file with the object inside
def writeFile(fileName, jsonObj):
    fileName = str(fileName) + ".json"
    with open(fileName, "w") as outfile:
        json.dump(jsonObj, outfile, indent=4)
    print "Json file created"

#To-do: Create a function that takes their JSON and creates an array



if __name__ == "__main__": # this needs to be a function and be called from map()
    while True:
        filename = randomfilename()
        if checkNum(filename):
            writeFile(filename, jsonobj.jsonObj)
            updateTxtFile(filename)
            break
        else:
            pass
