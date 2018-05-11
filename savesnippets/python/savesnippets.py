# Save Snippets from Google Chrome

# Begin
def main():
    pref_obj = openFile("Preferences")
    getSnippets(pref_obj)

# Try to open the file
# Note:  for "easy mode" use "with open" statement
#        this will close the file automatically
def openFile(prefName):
    print('opening: ' + prefName)
    try:
        pref_obj = open(prefName, "r")
        return pref_obj
    except IOError:
        print(prefName+' does not exist.')
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
    closeTag = 'scriptSnippets_lastIdentifier'
    snippets = prefText.split(openTag)[1].split(closeTag)[0]
    formatSnippets(snippets)

# Print the snippet section
def printFileText(pref_obj, prefText):
    print('showing text')
    print prefText
    closeFile(pref_obj)

def formatSnippets(snippets):
    newLineSnippets = snippets.replace('\\n', '\n')
    print(newLineSnippets)

main()
