#!/usr/bin/env python3
""" 
    #Halloween Tales (a spooky spoof of madlibs (don't sue me, lol) 
    #This program asks the user to enter some words, then returns a fun story!
    Author ~ Chance Bailey
    Created ~ 02/10/2023
"""

"""
    #TODO
    #Create menu to choose a story, start a random story, read saved stories, or exit.
    #Ask the user to choose menu option, clear the screen, then open menu, based on option choice.
    #On Choose a Story, List some general ideas of the story (not the full story), then let the user pick one.
    #On Start a Random Story, use random.choice() to pick a story, then start asking the user for inputs.
    #On Read Saved Stories, list the name of the stories and ask the user to pick one, then display the story.
    #On Exit, exit with a 0 status.
    #Ensure proper return and exit values.
    #Wrap anything that can break in try/except to catch errors.
"""

import random
from re import T
from sys import exit
from os import system
from random import choice

def main():
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
        system('cls') #clears the screen. Make sure you start without debugging or it doesn't work.
        print(menu)
        try:
            userChoice = int(input('Please choose an option from the menu: ')) #Any value here not a number throws the error we're catching below.
        except:
            continue #Sends the user back to the menu until they enter a number on the menu.
    if userChoice == 1:
        system('cls')
        storyMenu(storyList)
    elif userChoice == 2:
        system('cls')
        getUserText(storyList[choice(list(storyList))])
    elif userChoice == 3:
        system('cls')
        storyList()
    elif userChoice == 4:
        print('Goodbye!')
        exit(0)
    return 0

def storyMenu(storyList):
    stories = storyList
    storyRange = range(1,(len(stories)+1))
    storyChoice = 0
    print('Available Stories\n')
    while int(storyChoice) not in storyRange:
        system('cls')
        for story in stories:
            print(story + '. ' + str(stories[story]['title']))
        try:
            storyChoice = int(input('\nPlease choose a story: '))
        except:
            continue
    return getUserText(stories[str(storyChoice)])
    
def storyList():
    print('You made it to the story list!')

def getUserText(story):
    userStoryTitle = story['title']
    userStoryBody = story['body']
    userDictionary = story['inputs']
    replacementList = {}
    print('Your story is: ' + userStoryTitle + '\n')

    for key in userDictionary:
        tempInput = input(f'Please enter ' + key + ": ")
        replacementList[key] = tempInput
        
    return(replaceText(userStoryBody, replacementList))

def replaceText(story, userInputs):
    originalText = story
    replacementWords = userInputs
    for key in replacementWords:
        originalText = originalText.replace(key, replacementWords[key])
    return print(originalText)

main()

exit(0)
