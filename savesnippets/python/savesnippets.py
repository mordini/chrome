# Rewrite me to use class/OOP stuff

# Save Snippets from Google Chrome
import json
import re
import sys
import platform
import argparse

# This is floating as a test section
class File:
    def __init__(self, profileName):
        self.profileName = profileName
    def openFile():
        pref_obj = openFile("Preferences")
        return pref_obj
    def getProfileName(data):
        profileName = data['profile']['name']
        return profileName
    def getSnippets(data):
        snippets = data['devtools']['preferences']['scriptSnippets']
        return snippets

# Begin
def main():
    options = getOptions()
    prefFileName = options['prefFileName']
    action = options['action']

    # Open file here?
    #pref_obj = openFile(prefFileName)

    if action == 'export':
        print('export that junk')
        writeBackupFile(prefFileName)
    elif action == 'import':
        print('import that junk')
        backupFileName = options['backupFileName']
        importBackupFile(prefFileName, backupFileName) 

    # Close file here?
    #pref_obj.close()

def getPlatform():
    thePlatform = platform.system()
    print(thePlatform)
    return thePlatform 

def getFileNameNew():
    parser = argparse.ArgumentParser(description=\
        'Input Preferences filename.')
    parser.add_argument('-f','--file',required=True,\
            help='Put in path to Preferences file')
    parser.add_argument('-x','--export',\
            help='Export Snippets, uses profile name.')
    parser.add_argument('-i','--import',\
            help='Import previously exported Snippets.')
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
    parser.add_argument('-i','--backupFileName',\
            help='Put in path to Backup file')

    parser.parse_args()
    options = vars(parser.parse_args())

    #if options['action'] == 'import' and options['backupFileName'] is None:
    #    print('You need to pick a backup file to import from.')
    #    return;

    print(options)
    print('Preferences file is: {}'.format(options['prefFileName']))
    print('Action is: {}'.format(options['action']))

    return options

# Try to open the file
# Note:  for "easy mode" use "with open" statement
#        this will close the file automatically
def openFile(fileName):
    print('opening: ' + fileName)
    try:
        file_obj = open(fileName, 'r')
        return file_obj
    except IOError as e:
        print(e.errno, e.strerror)
        #print(fileName+' does not exist.')
        return

def getData(data_obj):
    data = json.load(data_obj)
    return data

def getProfileName(data):
    profileName = data['profile']['name']
    return profileName

def getSnippets(data):
    snippets = data['devtools']['preferences']['scriptSnippets']
    print(snippets)
    return snippets

def restoreSnippets():
    # Open Pref File
    pref_obj = openFile(prefFileName)
    # Get ALL Pref Data
    prefData = getData(pref_obj)
    # Write new Pref Data to Pref file
    snippets = getSnippets(data)
    # Close Pref File
    pref_obj.close()
    print('Save Snippets')

def writeBackupFile(prefFileName):

    # Open the preference file
    pref_obj = openFile(prefFileName)
    data = getData(pref_obj)
    pref_obj.close()

    # Get the actual profilename (google stores generic names)
    profileName = getProfileName(data)

    # Get Snippets from Devtools
    snippets = getSnippets(data)

    # Create backup file using profilename
    backup_obj = open(profileName, 'w')
    backup_obj.write(snippets)
    backup_obj.close()

def importBackupFile(prefFileName,backupFileName):
    print('importing!')
    # Note To Self:  Left off here 05/17/2018

    # Open Backup File
    backup_obj = openFile(backupFileName)
    # Get Backup Data
    backupData = getData(backup_obj)
    print(backupData)
    # Change Pref Data Snippets section to Backup
    #restoreSnippets(backupData)

    # Close Backup File
    backup_obj.close()

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
#    pref_obj.close()
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
