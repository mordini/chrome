# Save Snippets from Google Chrome
import json
import re
import sys

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
    pref_obj = getPrefObj()
    data = getData(pref_obj)
    writeBackupFile(data)
    closeFile(pref_obj)

#rewrite me to use class/OOP stuff
def getPrefObj():
    pref_obj = openFile("Preferences")
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

# Get the snippets section from Chrome prefs
def getSnippetsOLD(pref_obj):
    prefText = getPrefText(pref_obj)

    if prefText:
        closeFile(pref_obj)

    openTag = 'scriptSnippets'
    closeTag = '","scriptSnippets_lastIdentifier'
    #snippets = '{"' + openTag + prefText.split(openTag)[1].split(closeTag)[0]+'}' 
    #snippets = prefText.split(openTag)[1].split(closeTag)[0]
    snippets = re.search(openTag+'(.*)'+closeTag, prefText)
    formatSnippets(snippets.group(1))

# Print the snippet section
def printFileText(pref_obj, prefText):
    print('showing text')
    print(prefText)
    closeFile(pref_obj)

def formatSnippets(snippets):
    newLineSnippets = snippets.replace('\\n', '\n').replace('\\','')
    print(newLineSnippets)

main()
