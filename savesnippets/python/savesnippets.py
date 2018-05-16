# Rewrite me to use class/OOP stuff

# Save Snippets from Google Chrome
import json
import re
import sys
import platform
import argparse

# This is floating as a test section
class File:
    def __init__(self, profName):
        self.profName = profName
    def getPrefObj():
        pref_obj = openPref("Preferences")
        return pref_obj
    def getProfFileName(data):
        profName = data['profile']['name']
        return profName
    def getSnippets(data):
        snippets = data['devtools']['preferences']['scriptSnippets']
        return snippets

# Begin
def main():
    options = getOptions()
    prefFileName = options['prefFileName']
    action = options['action']

    print(prefFileName)
    print(action)

    pref_obj = getPrefObj(prefFileName)
    data = getData(pref_obj)

    if action == 'export':
        print('export that junk')
        writeBackupFile(data)
    elif action == 'import':
        print('import that junk')
        importBackupFile(data) 

    # #closePref(pref_obj)

def getPlatform():
    thePlatform = platform.system()
    print(thePlatform)
    return thePlatform 

def getFileNameNew():
    parser = argparse.ArgumentParser(description='Input Preferences filename.')
    parser.add_argument('-f','--file',required=True,\
            help='Put in path to Preferences file')
    parser.add_argument('-x','--export',\
            help='Export Snippets, uses profile name.')
    parser.add_argument('-i','--import',\
            help='Import preveiously exported Snippets.')
    parser.parse_args()
    prefFileName = vars(parser.parse_args())
    print('You chose {} as your filename'.format(prefFileName['file']))
    return prefFileName['file']


def getOptions():
    parser = argparse.ArgumentParser(description='Select Preferences\
            file and Import/Export')
    parser.add_argument('-f','--prefFileName',required=True,\
            help='Put in path to Preferences file')
    parser.add_argument('-a','--action',required=True,\
            choices=['export','import'],help='Choose between Export/Import')
    parser.add_argument('-i','--backFileName',\
            help='Put in path to Backup file')

    parser.parse_args()
    options = vars(parser.parse_args())

    #if options['action'] == 'import' and options['backupFileName'] is None:
    #    print('You need to pick a backup file to import from.')
    #    return;

    print(options)
    print('You chose {} as your filename'.format(options['prefFileName']))

    #return options['file']
    return options

def getPrefObj(prefFileName):
    pref_obj = openPref(prefFileName)
    return pref_obj

def getData(pref_obj):
    data = json.load(pref_obj)
    return data

def getProfFileName(data):
    profName = data['profile']['name']
    return profName

def getSnippets(data):
    snippets = data['devtools']['preferences']['scriptSnippets']
    return snippets

def writeBackupFile(data):
    profName = getProfFileName(data)
    snippets = getSnippets(data)
    backup_obj = open(profName, 'w')
    backup_obj.write(snippets)
    backup_obj.close()

def importBackupFile(data):
    backup_obj = openPref(prefFileName)
    # Note To Self:  Left off here 05/16/2018
    snippets = getSnippets(data)
    print('importing!')
    #print(data)
    backup_obj.close()


# Try to open the file
# Note:  for "easy mode" use "with open" statement
#        this will close the file automatically
def openPref(prefName):
    print('opening: ' + prefName)
    try:
        pref_obj = open(prefName, 'r')
        return pref_obj
    except IOError as e:
        print(e.errno, e.strerror)
        #print(prefName+' does not exist.')
        return

# Close the file
def closePref(pref_obj):
    print('closing file')
    pref_obj.close()

main()

##########################
## Future Implementation #
##########################
#def getPrefPath():
#  thePlatform = getPlatform()
#    if thePlatform == 'Linux':
#      # search for default prefs instead,
#        # get found Prefs, show profile names
#        prefPath = '~/.config/google-chrome/'
#    elif thePlatform == 'Windows':
#      # search for default prefs instead,
#        # get found Prefs, show profile names
#        prefPath = '%APPDATALOCAL%\google\chrome'
#    else:
#      print('What kind of OS are you using man?')
#    return prefPath
#
###################
## OLD TEST STUFF #
###################
#
## Get the text to work with
#def getPrefText(pref_obj):
#  prefText = pref_obj.read()
#    return prefText
#
## Print the snippet section
#def printFileText(pref_obj, prefText):
#  print('showing text')
#    print(prefText)
#    closePref(pref_obj)
#
## TEST GETTING JSON INFORMATION
#def testJSON(pref_obj):
#  data = json.load(pref_obj)
#    snippets = data['devtools']['preferences']['scriptSnippets']
#    testData = data['profile']['name']
#    data['devtools']['preferences']['scriptSnippets'] = ''
#    print('New snippets')
#    print(data['devtools']['preferences']['scriptSnippets'])
#    data['devtools']['preferences']['scriptSnippets'] = snippets
#    print('Old snippets')
#    print(data['devtools']['preferences']['scriptSnippets'])
#
#    print(testData)
#    for e in testData:
#      print(e)
