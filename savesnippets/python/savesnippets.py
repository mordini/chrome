# Rewrite me to use class/OOP stuff

# Save Snippets from Google Chrome
import json
import re
import sys
import platform

class File:
    def __init__(self, profName):
        self.profName = profName
    def getPrefObj():
        pref_obj = openFile("Preferences")
        return pref_obj
    def getProfileName(data):
        profName = data['profile']['name']
        return profName
    def getSnippets(data):
        snippets = data['devtools']['preferences']['scriptSnippets']
        return snippets

# Begin
def main():
    #test = File('Preferences')
    #print(test.profName)
    #testJSON(pref_obj)
    prefPath = getPrefPath()
    fileName = getFileName(prefPath)
    pref_obj = getPrefObj(fileName)
    data = getData(pref_obj)
    writeBackupFile(data)
    closeFile(pref_obj)
def getPlatform():
    thePlatform = platform.system()
    print(thePlatform )
    return thePlatform 
def getPrefPath():
    thePlatform = getPlatform()
    if thePlatform == 'Linux':
        prefPath = '~/.config/google-chrome/'
    elif thePlatform == 'Windows':
        prefPath = '%APPDATALOCAL%\google\chrome'
    else:
        print('What kind of OS are you using man?')
    return prefPath
def getFileName(prefPath):
    fileName = sys.argv[1]
    print(sys.argv[1])
    return fileName
def getPrefObj(fileName):
    pref_obj = openFile(fileName)
    return pref_obj
def getData(pref_obj):
    data = json.load(pref_obj)
    return data
def getProfileName(data):
    profName = data['profile']['name']
    return profName
def getSnippets(data):
    snippets = data['devtools']['preferences']['scriptSnippets']
    return snippets
def writeBackupFile(data):
    profName = getProfileName(data)
    snippets = getSnippets(data)
    backupFile = open(profName, 'w')
    backupFile.write(snippets)
    backupFile.close()

# Try to open the file
# Note:  for "easy mode" use "with open" statement
#        this will close the file automatically
def openFile(prefName):
    print('opening: ' + prefName)
    try:
        pref_obj = open(prefName, "r")
        return pref_obj
    except IOError as e:
        print(e.errno, e.strerror)
        #print(prefName+' does not exist.')
        return

# Close the file
def closeFile(pref_obj):
    print('closing file')
    pref_obj.close()

# Get the text to work with
def getPrefText(pref_obj):
    prefText = pref_obj.read()
    return prefText

# Print the snippet section
def printFileText(pref_obj, prefText):
    print('showing text')
    print(prefText)
    closeFile(pref_obj)

# TEST GETTING JSON INFORMATION
def testJSON(pref_obj):
    data = json.load(pref_obj)
    snippets = data['devtools']['preferences']['scriptSnippets']
    testData = data['profile']['name']
    data['devtools']['preferences']['scriptSnippets'] = ''
    print('New snippets')
    print(data['devtools']['preferences']['scriptSnippets'])
    data['devtools']['preferences']['scriptSnippets'] = snippets
    print('Old snippets')
    print(data['devtools']['preferences']['scriptSnippets'])

    print(testData)
    for e in testData:
        print(e)
main()
