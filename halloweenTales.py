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

from sys import exit
from os import system

testDictionary = {
    'key1' : 'value1',
    'key2' : 'value2'
}

def main():
    menuRange = range(1,5)
    userChoice = 0

    try:
        while int(userChoice) not in menuRange: #while the user hasn't chose a number between 1 and 4, keep reprinting the menu
            system('cls') #clears the screen. Make sure you start without debugging or it doesn't work.
            print('welcome to Halloween Tales!\n')
            print('1. Choose a Story.')
            print('2. Start a Random Story.')
            print('3. Read a Finished Story.')
            print('4. Exit\n')

            userChoice = int(input('Please choose an option from the menu: ')) #Any value here not a number throws the error we're catching below.
    except:
        system('cls') #clears the screen. Make sure you start without debugging or it doesn't work.
        print('welcome to Halloween Tales!\n')
        print('1. Choose a Story.')
        print('2. Start a Random Story.')
        print('3. Read a Finished Story.')
        print('4. Exit\n')

        userChoice = input('Please enter the number of your option: ')

    if userChoice == 1:
        system('cls')
        print('You chose option 1!')
    elif userChoice == 2:
        system('cls')
        print('You chose option 2!')
    elif userChoice == 3:
        system('cls')
        print('You chose option 3!')
    else:
        exit(0)
    return 0

def replaceText(story, textDictionary):
    originalText = story #'key1 key2'
    replacementWords = textDictionary #{'key1':'value1','key2':'value2'}
    for key in replacementWords:
        originalText = originalText.replace(key, replacementWords[key])
    return print(originalText)

def getUserText():
    userStory = ''
    userDictionary = {
        'a': 'b',
        'c': 'd'
    }
    return(replaceText(userStory, userDictionary))

main()

exit(0)
