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
    #Build deeper error handling for bad inputs. For example, check if the entered adjective needs to be preceded with an 'an' instead of an 'a'.
"""

from sys import exit, platform
from os import listdir, system, path
from random import choice

def main():
    clear = ''
    user = ''
    if platform == "Linux": #Thanks Stack Overflow: https://stackoverflow.com/questions/8220108/how-do-i-check-the-operating-system-in-python and Section.io: https://www.section.io/engineering-education/how-to-execute-linux-commands-in-python/
        clear = 'clear'
        chmod = 'chmod 755 ./halloweenTales.py'
        system(chmod)
        user = system('whoami')
        pathToStories = f'/home/{user}/halloweenTales/stories/'
        pathToLogs = f'/home/{user}/halloweenTales/logs'
        if not path.exists(pathToStories):
            system(f'mkdir /home/{user}/halloweenTales/stories/')
            system(f'chmod 744 /home/{user}/halloweenTales/stories/')
        if not path.exists(pathToLogs):
            system(f'mkdir /home/{user}/halloweenTales/logs/')
            system(f'chmod 744 /home/{user}/halloweenTales/logs/')
    else: #Would need an elif to check for Unix-based OS, like Mac. I don't have one, so I wouldn't be able to test this anyway, so only coding for Linux and Windows.
        clear = 'cls'
        if path.exists(path.expanduser('~\\OneDrive\\Documents\\')): #Checking if the user is using OneDrive to backup Documents. We'll put the stories in there if they are.
            try:
                pathToStories = path.expanduser('~\\OneDrive\\Documents\\Halloween_Tales\\stories\\')
                system(f'md {pathToStories}') #This will fail if the directory already exists, so we're catching it and just setting the path to the directory.
            except:
                pathToStories = path.expanduser('~\\OneDrive\\Documents\\Halloween_Tales\\stories\\')
            try:
                pathToLogs = path.expanduser('~\\OneDrive\\Documents\\Halloween_Tales\\logs\\')
                system(f'md {pathToLogs}')
            except:
                pathToLogs = path.expanduser('~\\OneDrive\\Documents\\Halloween_Tales\\logs\\')
        else: #Otherwise, we're saving them in the old Documents folder.
            try:
                pathToStories = path.expanduser('~\\Documents\\Halloween_Tales\\stories\\')
                system(f'md {pathToStories}') #This will fail if the directory already exists, so we're catching it and just setting the path to the directory.
            except:
                pathToStories = path.expanduser('~\\Documents\\Halloween_Tales\\stories\\')
            try:
                pathToLogs = path.expanduser('~\\Documents\\Halloween_Tales\\logs\\')
                system(f'md {pathToLogs}')
            except:
                pathToLogs = path.expanduser('~\\Documents\\Halloween Tales\\logs\\')
    
    #To save time on this project, I've 'gracefully' lifted some stories from Woo Jr. Link: https://woojr.com/halloween-ad-libs/ Note: These are not mine and would be replaced in a final version.
    storyList = {
        '1': { #https://woojr.com/wp-content/uploads/2017/10/mad-scientist-adlib-print.jpg
            'title':'My Substitute Teacher is a Mad Scientist',
            'body':'Today we had a substitute teacher for science class, with a color hair that a verb (past tense) straight up a number inches high. His name was Mr. an animal and he said he\'d show us why science was the most an adjective class. First, he used a a tool and a a vegetable to make a a container of water turn another color. Then he made a a noun of the solar system using a a fruit, a a candy, and a another noun. When the principal walked by and saw the substitute teacher using a a third noun to a verb the some furniture into a third color a plural noun, she asked him to show the class a movie about another plural noun instead. The next day, we had a different substitute teacher.',
            'inputs': {'a color':'PH1','a verb (past tense)':'PH2','a number':'PH3','an animal':'PH4','an adjective':'PH5','a tool':'PH6','a vegetable':'PH7','a container':'PH8','another color':'PH9','a noun':'PH10','a fruit':'PH11','a candy':'PH12','another noun':'PH13','a third noun':'PH14','a verb':'PH15','some furniture':'PH16','a third color':'PH17','a plural noun':'PH18','another plural noun':'PH19'}
            },
        '2': { #https://woojr.com/wp-content/uploads/2017/10/skeletons-ad-libs-for-kids.jpg
            'title':'Best Halloween Costume Contest',
            'body':'This year a place is having an adjective Halloween Costume Contest. I hope I win; I\'m going to dress up as a another adjective a noun. My best friend is going to be a a third adjective a color an animal and my cousin is going to be a a fourth adjective another noun. They have a a fifth adjective party and everyone in town shows up to a verb all of the a sixth adjective costumes. We play games, like bobbing for apples and another verbing a plural noun and it is so much fun!',
            'inputs': {'a place':'PH1','an adjective':'PH2','another adjective':'PH3','a noun':'PH4','a third adjective':'PH5','a color':'PH6','an animal':'PH7','a fourth adjective':'PH8','another noun':'PH9','a fifth adjective':'PH0','a verb':'PH11','a sixth adjective':'PH12','another verb':'PH13','a plural noun':'PH14'}
        },
        '3': { #https://woojr.com/wp-content/uploads/2017/10/ad-libs-for-Halloween.jpg
            'title':'My School Gets Pretty Weird at Halloween',
            'body':'My school is pretty an adjective for most of the year, except in late October, when another adjective cobwebs appear in the hallway, with really a third adjective an animals hanging from them. The lunch room has orange and black a plural noun everywhere, and they serve roasted a part of the body for lunch. Someone told me that a giant a fourth adjective another animal took over the principal\'s office. All of the teachers look different; one is a zombie with a color hair, another is a a fifth adjective a noun, and I think my school subject teacher is a a vehicle now. Tombstones line the hallways, and one says "Here lies a name of someone in the room, who died of a verbing."',
            'inputs': {'an adjective':'PH1','another adjective':'PH2','a third adjective':'PH3','an animal':'PH4','a plural noun':'PH5','a part of the body':'PH6','a fourth adjective':'PH7','another animal':'PH8','a color':'PH9','a fifth adjective':'PH10','a noun':'PH11','school subject':'PH12','a vehicle':'PH13','a name of someone in the room':'PH14','a verb':'PH15'}
        },
        '4': { #https://woojr.com/wp-content/uploads/2017/10/scary-halloween-ad-lib.jpg
            'title':'A Scary Halloween Story',
            'body':'They say my school is haunted; my an adjective friend a first name says she saw a another adjective a noun floating at the end of the hall near the cafeteria. Some say if you a verb down the hallway at night, you\'ll hear an animal another verbing an adverb. My a third adjective friend another first name saw a fourth adjective another noun a thrid verbing under one of the tables once. I hope I never see any a plural noun a forth verbing; eating lunch is scary enough!',
            'inputs': {'an adjective':'PH1','a first name':'PH2','another adjective':'PH3','a noun':'PH4','a verb':'PH5','an animal':'PH6','another verb':'PH7','an adverb':'PH8','a third adjective':'PH9','another first name':'PH10','a fourth adjective':'PH11','another noun':'PH12','a third verb':'PH13','a plural noun':'PH14','a fourth verb':'PH15'}
        },
        '5': { #https://woojr.com/wp-content/uploads/2017/10/halloween-adlibs.jpg
            'title':'Halloween Treats',
            'body':'Halloween is the best time to a verb. the weather is an adjective and another adjective and you go door to door, saying "Trick or Treat!" and people give you a plural noun and another plural noun to eat. This year, I will dress up as a a noun, a a third adjective a color another noun, or maybe a a fourth adjective an animal. If someone says "Trick!" instead of giving you a treat, you might have to another verb or a third verb to try and scare them into giving you a a fifth adjective a food or a a sixth adjective another food as a treat.',
            'inputs': {'a verb':'PH1','an adjective':'PH2','another adjective':'PH3','a plural noun':'PH4','another plural noun':'PH5','a noun':'PH6','a third adjective':'PH7','a color':'PH8','another noun':'PH9','a fourth adjective':'PH10','an animal':'PH11','another verb':'PH12','a third verb':'PH13','a fifth adjective':'PH14','a food':'PH15','a sixth adjective':'PH16','another food':'PH17'}
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
        storyMenu(storyList, clear, pathToStories, pathToLogs)
    elif userChoice == 2:
        system(clear)
        getUserText(storyList[choice(list(storyList))], clear, pathToStories, pathToLogs)
    elif userChoice == 3:
        system(clear)
        readStories(storyList, clear, pathToStories, pathToLogs)
    elif userChoice == 4:
        return 0
    return 0

def storyMenu(storyList, clear, pathToStories, pathToLogs):
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
    return getUserText(stories[str(storyChoice)], clear, pathToStories, pathToLogs)
    
def readStories(storyList, clear, pathToStories, pathToLogs):
    system(clear)
    storiesToRead = listdir(pathToStories)
    userChoice = ''
    if len(listdir(pathToStories)) == 0: #Checks to see if the directory is empty. We can read stories that haven't been written.
        while not (userChoice.lower() == 'yes' or userChoice.lower() == 'y' or userChoice.lower() == 'no' or userChoice.lower() == 'n'):
            userChoice = input('Oh, it looks like you don\'t have any stories. Would you like to start a random story? ')
            match userChoice.lower(): #Python 3.10+ feature. Make sure you have the correct version before running this script.
                case 'yes' | 'y':
                    system(clear)
                    getUserText(storyList[choice(list(storyList))], clear, pathToStories, pathToLogs)
                case 'no' | 'n':
                    userChoice = input('Are you sure you don\'t want to start a story? Enter no or n again to confirm: ')
                    if userChoice.lower() == 'no' or userChoice.lower() == 'n':
                        break
                    else:
                        continue
                case _: #Wildcard. Not really needed here as we're looping if the user doesn't enter yes, y, no, or n, but a match case statement feels incomplete without it.
                    continue
    else:
        storyRange = range(1, (len(listdir(pathToStories))+1))
        while not userChoice in storyRange:
            counter = 1
            system(clear)
            for story in listdir(pathToStories): #Thanks Builtin: https://builtin.com/data-science/python-list-files-in-directory
                print(f'{counter}. {story}'.removesuffix('.txt')) #Thanks Visual Studio for the suggestion to remove the suffix!
                counter += 1
            try:
                userChoice = int(input('\nPlease choose a story to read: '))
            except:
                continue
        system(clear)
        with open(rf'{pathToStories}{storiesToRead[(int(userChoice)-1)]}') as readStory:
            print(readStory.read())
            userChoice = '' #resetting userChoice for next menu
            while not (userChoice == '1' or userChoice == '2' or userChoice == '3'):
                userChoice = input('\n\n1. Read another story.\n2. Return to main menu.\n3. Exit\n\nPlease choose an option: ')    
                match userChoice:
                    case '1':
                        readStories(storyList, clear, pathToStories, pathToLogs)
                    case '2':
                        main()
                    case '3':
                        return 0
                    case _:
                        system(clear)
                        continue
    return 0    

def getUserText(story, clear, pathToStories, pathToLogs):
    userStoryTitle = story['title']
    userStoryBody = story['body']
    userDictionary = story['inputs']
    replacementList = {}
    system(clear)
    print('Your story is: ' + userStoryTitle + '\n')

    for key in userDictionary:
        tempInput = input(f'Please enter ' + key + ": ")
        replacementList[key] = tempInput
        
    return(replaceText(userStoryTitle, userStoryBody, replacementList, clear, pathToStories, pathToLogs))

def replaceText(storyTitle, storyBody, userInputs, clear, pathToStories, pathToLogs):
    newStoryBody = storyBody
    replacementWords = userInputs
    for key in replacementWords:
        newStoryBody = newStoryBody.replace(key, replacementWords[key])
    system(clear)
    print(f'{newStoryBody}\n\n')
    
    return (saveStory(storyTitle, newStoryBody, clear, pathToStories, pathToLogs))

def saveStory(storyTitle, newStoryBody, clear, pathToStories, pathToLogs):
    saveRequest = ''
    while not (saveRequest.lower() == 'yes' or saveRequest.lower() == 'y' or saveRequest.lower() == 'no' or saveRequest.lower() == 'n'):
        saveRequest = input('Do you want to save? Enter yes or y to save, and no or n to not save: ')
        match saveRequest.lower(): #Python 3.10+ feature. Make sure you have the correct version before running this script.
            case 'yes' | 'y':
                try:
                    with open(rf'{pathToStories}{storyTitle}.txt', 'x') as saveStory:
                        saveStory.write(f'{storyTitle}\n\n{newStoryBody}')
                        print(f'You saved "{storyTitle}" to {storyTitle}.txt\n')
                    break #I don't know why I need this break, as the value of saveRequest should break the user out of the loop, but here we are....
                except:
                    saveRequest = input('Oh, it looks like you\'ve aready completed this story. Would you like to keep your new version instead? ')
                    if saveRequest.lower() == 'yes' or saveRequest.lower() == 'y':
                        if platform == 'Linux':
                            system(f'mv {pathToStories}{storyTitle}.txt {pathToLogs}{storyTitle}.bak')
                        with open(rf'{pathToStories}{storyTitle}.txt', 'w') as saveStory:
                            saveStory.write(f'{storyTitle}\n\n{newStoryBody}')
                            print(f'You replaced the old story of {storyTitle} with your new version.')
                        break #I don't know why I need this break, as the value of saveRequest should break the user out of the loop, but here we are....
                    elif saveRequest.lower() == 'no' or saveRequest.lower() == 'n':
                        tempInput = input('We\'ll keep the original, then. Press enter to continue.')
                        break
            case 'no' | 'n':
                saveRequest = input('Are you sure you don\'t want to save your story? Enter no or n again to confirm: ')
                if saveRequest.lower() == 'no' or saveRequest.lower() == 'n':
                    break
                else:
                    continue
            case _: #Wildcard. Not really needed here as we're looping if the user doesn't enter yes, y, no, or n, but a match case statement feels incomplete without it.
                continue
    menuChoice = ''
    while not (menuChoice.lower() == '1' or menuChoice.lower() == '2'):
        #system(clear)
        print('1. Return to main menu.\n2. Exit\n\n')
        menuChoice = input('Please choose an option from above: ')
        match menuChoice.lower():
            case '1':
                main()
            case '2':
                return 0
    return 0

main()
print('Goodbye!')
exit(0)