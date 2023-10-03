#!/usr/bin/env python3
""" 
    #Halloween Tales (a spooky spoof of madlibs (don't sue me, lol) 
    #This program asks the user to enter some words, then returns a fun story!
    Author ~ Chance Bailey
    Created ~ 02/10/2023
"""

"""
    #TODO
    #On Read Saved Stories, list the name of the stories and ask the user to pick one, then display the story.
    #Ensure proper return and exit values.
"""

from sys import exit, platform
from os import system, path
from random import choice

def main():
    clear = ''
    user = ''
    if platform == "Linux": #Thanks Stack Overflow: https://stackoverflow.com/questions/8220108/how-do-i-check-the-operating-system-in-python and Section.io: https://www.section.io/engineering-education/how-to-execute-linux-commands-in-python/
        clear = 'clear'
        chmod = 'chmod 755 ./halloweenTales.py'
        system(chmod)
        user = system('whoami')
        pathToStories = f'/home/{user}/stories/'
        if not path.exists(pathToStories):
            system(f'mkdir /home/{user}/stories/')
            system(f'chmod 744 /home/{user}/stories/')
    else:
        clear = 'cls'
        pathToStories = path.expanduser('~\\Documents\\stories')
        if path.exists(path.expanduser('~\\OneDrive\\Documents\\')): #Checking if the user is using OneDrive to backup Documents. We'll put the stories in there if they are.
            if not path.exists(path.expanduser('~\\OneDrive\\Documents\\stories')):
                pathToStories = path.expanduser('~\\OneDrive\\Documents\\stories')
                print(pathToStories)
                system(f'md {pathToStories}')
        elif not path.exists('~\\Documents\\stories'): #Otherwise, we're saving them in the old Documents folder.
            pathToStories = path.expanduser('~\\Documents\\stories')
            system(f'md {pathToStories}')
    
    storyList = {
        '1': {
            'title':'The Case of the Missing Candy',
            'body':'lorem ipsum PH1 PH2 PH3 PH4 PH5 PH6 PH7 PH8 PH9',
            'inputs': {'PH1':'text','PH2':'text','PH2':'text','PH3':'text','PH4':'text','PH5':'text','PH6':'text','PH7':'text','PH8':'text','PH9':'text'}
            },
        '2': {
            'title':'The Best Costume of the Night',
            'body':'lorem ipsum',
            'inputs': {'PH1':'text','PH2':'text','PH2':'text','PH3':'text','PH4':'text','PH5':'text','PH6':'text','PH7':'text','PH8':'text','PH9':'text'}
        },
        '3': {
            'title':'Family Pumpkin Carving',
            'body':'lorem ipsum',
            'inputs': {'PH1':'text','PH2':'text','PH2':'text','PH3':'text','PH4':'text','PH5':'text','PH6':'text','PH7':'text','PH8':'text','PH9':'text'}
        },
        '4': {
            'title':'Scary Story Night',
            'body' : 'lorem ipsum',
            'inputs': {'PH1':'text','PH2':'text','PH2':'text','PH3':'text','PH4':'text','PH5':'text','PH6':'text','PH7':'text','PH8':'text','PH9':'text'}
        },
        '5': {
            'title':'Baking Ghosts?!?',
            'body':'lorem ipsum',
            'inputs': {'PH1':'text','PH2':'text','PH2':'text','PH3':'text','PH4':'text','PH5':'text','PH6':'text','PH7':'text','PH8':'text','PH9':'text'}
        }
    }
    menu = 'Welcome to Halloween Tales\n\n1. Choose a Story.\n2. Start a Random Story.\n3. Read a Finished Story.\n4. Exit\n'
    menuRange = range(1,5)
    userChoice = 0
    while int(userChoice) not in menuRange: #while the user hasn't chose a number between 1 and 4, keep reprinting the menu
        system(clear) #clears the screen. Make sure you start without debugging or it doesn't work.
        print(menu)
        try:
            userChoice = int(input('Please choose an option from the menu: ')) #Any value here not a number throws the error we're catching below.
        except:
            continue #Sends the user back to the menu until they enter a number on the menu.
    if userChoice == 1:
        print(clear)
        system(clear)
        storyMenu(storyList, clear)
    elif userChoice == 2:
        system(clear)
        getUserText(storyList[choice(list(storyList))], clear)
    elif userChoice == 3:
        system(clear)
        storyList(clear)
    elif userChoice == 4:
        print('Goodbye!')
        exit(0)
    return 0

def storyMenu(storyList, clear):
    stories = storyList
    storyRange = range(1,(len(stories)+1))
    storyChoice = 0
    print('Available Stories\n')
    while int(storyChoice) not in storyRange:
        system(clear)
        for story in stories:
            print(story + '. ' + str(stories[story]['title']))
        try:
            storyChoice = int(input('\nPlease choose a story: '))
        except:
            continue
    return getUserText(stories[str(storyChoice)], clear)
    
def storyList(clear):
    system(clear)
    print('You made it to the story list!')

def getUserText(story, clear):
    userStoryTitle = story['title']
    userStoryBody = story['body']
    userDictionary = story['inputs']
    replacementList = {}
    system(clear)
    print('Your story is: ' + userStoryTitle + '\n')

    for key in userDictionary:
        tempInput = input(f'Please enter ' + key + ": ")
        replacementList[key] = tempInput
        
    return(replaceText(userStoryTitle, userStoryBody, replacementList, clear))

def replaceText(storyTitle, storyBody, userInputs, clear):
    newStoryBody = storyBody
    replacementWords = userInputs
    for key in replacementWords:
        newStoryBody = newStoryBody.replace(key, replacementWords[key])
    system(clear)
    print(newStoryBody)
    saveRequest = ''
    while not saveRequest.lower == 'yes' or 'y' or 'no' or 'n':
        system(clear)
        saveRequest = input('Do you want to save? ')
        match saveRequest.lower():
            case 'yes' | 'y':
                print('you saved!')
            case 'no' | 'n':
                print('you didn\'t save!')

main()

exit(0)