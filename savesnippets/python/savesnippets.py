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
        exportBackupFile(prefFileName)
    elif action == 'import':
        print('import that junk')
        backupFileName = options['backupFileName']
        importBackupFile(prefFileName, backupFileName) 

    # Close file here?
    #pref_obj.close()

def printEmptyLines(num):
    for i in range(0, num):
        print()

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
def openFile(fileName, mode):
    print('opening: ' + fileName)
    try:
        file_obj = open(fileName, mode, encoding='utf8')
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

def exportBackupFile(prefFileName):

    # Open the preference file
    pref_obj = openFile(prefFileName, 'r')
    data = getData(pref_obj)
    pref_obj.close()

    # Get the actual profilename (google stores generic names)
    profileName = getProfileName(data)

    # Get Snippets from Devtools
    snippets = getSnippets(data)

    # Create backup file using profilename
    backup_obj = openFile(profileName, 'w')
    backup_obj.write(snippets)
    backup_obj.close()

def restoreSnippets(backupData,prefFileName):
    ## Note To Self:  Left off here 05/17/2018
    printEmptyLines(5)
    print('restore snippets to backup, show backupData:')
    printEmptyLines(5)
    print(backupData)
    printEmptyLines(2)
    print('prefFileName is: ')
    print(prefFileName)
    printEmptyLines(2)

    with(prefFileName, 'r') as pref_obj:
        pref_data = json.load(pref_obj)
        for item in pref_data:
          if item['scriptSnippets']:
             print('item scriptsnippets is:')
             print(item['scriptSnippets'])
             item['scriptSnippets'] = backupData
             print('NEW item scriptsnippets is:')
             print(item['scriptSnippets'])

    #with(prefFileName, 'w') as pref_obj:
        #json.dump(pref_data, pref_obj)
    #print('Restore Snippets')
    ## Open Pref File
    #pref_obj = openFile(prefFileName, 'r')
    ## Get ALL Pref Data
    #prefData = getData(pref_obj)

    #print('THIS IS THE CURRENT PREF DATA')
    #print(prefData)

    #print('-------------------------------------------')
    #print('-------------------------------------------')
    #print('THIS IS THE current SNIP DATA')
    #currentSnipData = prefData['devtools']['preferences']['scriptSnippets']
    #print(currentSnipData)

    #print('-------------------------------------------')
    #print('-------------------------------------------')

    ## Put backupData into prefData
    #prefData['devtools']['preferences']['scriptSnippets'] = backupData
    #newSnipData = prefData['devtools']['preferences']['scriptSnippets']
    #print('THIS IS THE NEW SNIP DATA')
    #print(newSnipData)
    #
    ## Close Pref File (we will reopen to write)
    ## to prevent appending
    #pref_obj.close()

    ## may need to walk through items in prefData and replace on key.
    ## Write new Pref Data to Pref file
    ##pref_obj.write(newSnipData)

    ## let's use with for fun
    #with open(prefFileName, 'w') as pref_obj:
    #    json.dump(newSnipData, pref_obj)

    ##json.dump(newSnipData, pref_obj)
    ## Close Pref File
    ## pref_obj.close()

def importBackupFile(prefFileName,backupFileName):
    print('importing!')

    # Open Backup File
    backup_obj = openFile(backupFileName, 'r')
    # Get Backup Data
    backupData = getData(backup_obj)
    print(backupData)
    # Change Pref Data Snippets section to Backup
    restoreSnippets(backupData,prefFileName)

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
