# Save Snippets from Google Chrome
import json
import re
from pprint import pprint

# Begin
def main():
    pref_obj = openFile("Preferences")
    #getSnippets(pref_obj)
    testJSON(pref_obj)
    closeFile(pref_obj)

# TEST GETTING JSON INFORMATION
def testJSON(pref_obj):
    data = json.load(pref_obj)
    snippets = data['devtools']['preferences']['scriptSnippets']
    #print(snippets)
    data['devtools']['preferences']['scriptSnippets'] = ''
    print('New snippets')
    print(data['devtools']['preferences']['scriptSnippets'])
    data['devtools']['preferences']['scriptSnippets'] = snippets
    print('Old snippets')
    print(data['devtools']['preferences']['scriptSnippets'])
    #for e in data['devtools']:
        #print(e)

# Try to open the file
# Note:  for "easy mode" use "with open" statement
#        this will close the file automatically
def openFile(prefName):
    print('opening: ' + prefName)
    try:
        pref_obj = open(prefName, "r")
        return pref_obj
    except IOError as e:
        print e.errno, e.strerror
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
def getSnippets(pref_obj):
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
    print prefText
    closeFile(pref_obj)

def formatSnippets(snippets):
    newLineSnippets = snippets.replace('\\n', '\n').replace('\\','')
    print(newLineSnippets)

main()
