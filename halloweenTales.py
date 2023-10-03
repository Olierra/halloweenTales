#!/usr/bin/env python3
""" 
    #Halloween Tales (a spooky spoof of madlibs (don't sue me, lol) 
    #This program asks the user to enter some words, then returns a fun story!
    Author ~ Chance Bailey
    Created ~ 02/10/2023
    
    #Note - this script uses a match/case block that requires Python 3.10 or higher.
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
        if path.exists(path.expanduser('~\\OneDrive\\Documents\\')): #Checking if the user is using OneDrive to backup Documents. We'll put the stories in there if they are.
            try:
                pathToStories = path.expanduser('~\\OneDrive\\Documents\\stories\\')
                system(f'md {pathToStories}') #This will fail if the directory already exists, so we're catching it and just setting the path to the directory.
            except:
                pathToStories = path.expanduser('~\\OneDrive\\Documents\\stories\\')
        else: #Otherwise, we're saving them in the old Documents folder.
            try:
                pathToStories = path.expanduser('~\\Documents\\stories\\')
                system(f'md {pathToStories}') #This will fail if the directory already exists, so we're catching it and just setting the path to the directory.
            except:
                pathToStories = path.expanduser('~\\Documents\\stories\\')
    
    storyList = {
        '1': {
            'title':'The Case of the Missing Candy',
            'body':'lorem ipsum PH1 PH2 PH3 PH4 PH5 PH6 PH7 PH8 PH9',
            'inputs': {'PH1':'text','PH2':'text','PH2':'text','PH3':'text','PH4':'text','PH5':'text','PH6':'text','PH7':'text','PH8':'text','PH9':'text'}
            },
        '2': {
            'title':'The Best Costume of the Night',
            'body':'lorem ipsum PH1 PH2 PH3 PH4 PH5 PH6 PH7 PH8 PH9',
            'inputs': {'PH1':'text','PH2':'text','PH2':'text','PH3':'text','PH4':'text','PH5':'text','PH6':'text','PH7':'text','PH8':'text','PH9':'text'}
        },
        '3': {
            'title':'Family Pumpkin Carving',
            'body':'lorem ipsum PH1 PH2 PH3 PH4 PH5 PH6 PH7 PH8 PH9',
            'inputs': {'PH1':'text','PH2':'text','PH2':'text','PH3':'text','PH4':'text','PH5':'text','PH6':'text','PH7':'text','PH8':'text','PH9':'text'}
        },
        '4': {
            'title':'Scary Story Night',
            'body':'lorem ipsum PH1 PH2 PH3 PH4 PH5 PH6 PH7 PH8 PH9',
            'inputs': {'PH1':'text','PH2':'text','PH2':'text','PH3':'text','PH4':'text','PH5':'text','PH6':'text','PH7':'text','PH8':'text','PH9':'text'}
        },
        '5': {
            'title':'Baking Ghosts?!?',
            'body':'lorem ipsum PH1 PH2 PH3 PH4 PH5 PH6 PH7 PH8 PH9',
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
        storyMenu(storyList, clear, pathToStories)
    elif userChoice == 2:
        system(clear)
        getUserText(storyList[choice(list(storyList))], clear, pathToStories)
    elif userChoice == 3:
        system(clear)
        storyList(clear, pathToStories)
    elif userChoice == 4:
        print('Goodbye!')
        exit(0)
    return 0

def storyMenu(storyList, clear, pathToStories):
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
    return getUserText(stories[str(storyChoice)], clear, pathToStories)
    
def storyList(clear, pathToStories):
    system(clear)
    return print('You made it to the story list!')

def getUserText(story, clear, pathToStories):
    userStoryTitle = story['title']
    userStoryBody = story['body']
    userDictionary = story['inputs']
    replacementList = {}
    system(clear)
    print('Your story is: ' + userStoryTitle + '\n')

    for key in userDictionary:
        tempInput = input(f'Please enter ' + key + ": ")
        replacementList[key] = tempInput
        
    return(replaceText(userStoryTitle, userStoryBody, replacementList, clear, pathToStories))

def replaceText(storyTitle, storyBody, userInputs, clear, pathToStories):
    newStoryBody = storyBody
    replacementWords = userInputs
    for key in replacementWords:
        newStoryBody = newStoryBody.replace(key, replacementWords[key])
    system(clear)
    print(f'{newStoryBody}\n\n')
    
    return (saveStory(storyTitle, newStoryBody, clear, pathToStories))

def saveStory(storyTitle, newStoryBody, clear, pathToStories):
    saveRequest = ''
    while not (saveRequest.lower() == 'yes' or saveRequest.lower() == 'y' or saveRequest.lower() == 'no' or saveRequest.lower() == 'n'):
        saveRequest = input('Do you want to save? Enter yes or y to save, and no or n to not save: ')
        match saveRequest.lower(): #Python 3.10+ feature. Make sure you have the correct version before running this script.
            case 'yes' | 'y':
                try:
                    with open(rf'{pathToStories}{storyTitle}.txt', 'x') as saveStory:
                        saveStory.write(f'{storyTitle}\n\n{newStoryBody}')
                        print(f'You saved {storyTitle} to {storyTitle}.txt')
                    break #I don't know why I need this break, as the value of saveRequest should break the user out of the loop, but here we are....
                except:
                    saveRequest = input('Oh, it looks like you\'ve aready completed this story. Would you like to keep your new version instead? ')
                    if saveRequest == 'yes' or saveRequest == 'y':
                        with open(rf'{pathToStories}{storyTitle}.txt', 'w') as saveStory:
                            saveStory.write(f'{storyTitle}\n\n{newStoryBody}')
                            print(f'You replaced the old story of {storyTitle} with your new version.')
                        break #I don't know why I need this break, as the value of saveRequest should break the user out of the loop, but here we are....
                    elif saveRequest == 'no' or saveRequest == 'n':
                        tempInput = input('We\'ll keep the original, then. Press any key to return to exit.')
                        break
            case 'no' | 'n':
                saveRequest = input('Are you sure you don\'t want to save your story? Enter no or n again to confirm: ')
                if saveRequest.lower == 'no' or 'n':
                    break
                else:
                    continue
            case _: #Wildcard. Not really needed here as we're looping if the user doesn't enter yes, y, no, or n, but a match case statement feels incomplete without it.
                continue
    menuChoice = ''
    while not (menuChoice.lower() == '1' or menuChoice.lower() == '2'):
        system(clear)
        print('1. Return to main menu.\n2. Exit\n\n')
        menuChoice = input('Please choose an option from above: ')
        match menuChoice.lower():
            case '1':
                main()
            case '2':
                return 0
    return 0

main()

exit(0)