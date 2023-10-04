# halloweenTales
#
# Script Information
#
# Script Name: halloweeenTales.py
#
# Date Created: October 2nd, 2023
#
# Author: Chance Bailey
#
#
# Purpose:
# This script allows users to pick a Halloween-themed story and fill in various words, like an adjective, noun, or color, then generates a story with their words replacing the placeholder text. The user can also read saved stories. Minor logging of saved files is available, but only one back up of the replaced saved file is currently kept.
#
# Known Errors or Exits:
#
# Note: this script does use a match/case block, which requires Python 3.10 or higher.
#
# Note; the script should check if the user is running Linux and set the directories and commands accordingly, but testing this in WSL doesn't seem to work. I've not tried it on a VM.
#
# While not an error or exit, the script does little to check if the user puts in inappropriate words (such as a noun in place of a verb, or explicit words). This won't break the script, but the story isn't grammatically correct.
#
# The script should finally exit with a 0 status once the user is done.
#
# FAQ:
#
#
# Technical Documentation
#
# Supporting Files:
#
# Linux:
#
# stories/ /home/user/halloweenTales/stories/
#
#   stores the saved stories from the user.
#
# logs/ /home/user/halloweenTales/logs/
#
#    currently stores a backup of the replaced story (only the latest backup), and a log for each day, with a record that a story was saved.
#
# Windows
#
# stories\ ~\OneDrive\Documents\Halloween_Tales\stories\ if using OneDrive, or ~\Documents\Halloween_Tales\stories\ 
#
#    stores the saved stories from the user.
#
# logs/ ~\OneDrive\Documents\Halloween_Tales\logs\ if using OneDrive, or ~\Documents\Halloween_Tales\logs\
#
#    currently stores a backup of the replaced story (only the latest backup), and a log for each day, with a record that a story was saved.
#
# Global Variables:
#
# Technically none, as python doesn't really support that, but the main function does pass the following variables through most of the script;
#
#    clear - holds the command that clears the screen, as it varies between OS
#    chmod - stores the command to set the permissions, currently set to 755
#    user - saves the value of the whoami command, if in Linux (this is handled by path.expanduser() instead in Windows).
#    pathToStories - used to hold the path of the stories directory (see above for possible values).
#    pathToLogs - used to hold the path of the log directory (see above for possible values).
#
# Functions:
#
# main
#
#    Checks and sets above variables, then ensures needed directories or files are generated, along with proper permissions. Then builds a list of stories for the user, and finally generates a menu to choose a story, start a random story, read saved stories, or exit.
#
# storyMenu
#
#    Generates a list of the stories available to the user, from the dictionary in main. Once the user chooses a story, they are sent to getUserText
#
# readStories
#
#    Generates a list of the saved stories to the user, from the stories directory. Once the user chooses a story, they are presented with the saved version of that story and asked if they want to read another (will send them back to readStories), to return to the main menu, or to exit. If no stories are saved, it will ask if the user wants to start one. If they say yes or y, they will be given a random story, otherwise they exit. Any input other than yes, y, no, n (or the variants with capitalization) will cause the user to be prompted.
#
# getUserText
#
#   Prints out the title of the chosen story, then starts prompting the user for various words (these are specific to the chosen story). Once the last word is entered the user is sent to replaceText
#    Note, while multi-word inputs are valid, no checks are in place for inappropriate words (see Known Errors or Exits).
#
# replaceText
#
#    Replaces the placeholder words in the user's chosen story with their inputs from getUserText, prints the completed story, then sends the user to saveStory
#
# saveStory
#
#    Prompts the user to save the story or not. If the user opts to save the story, the script will check if the story already exists, and asked if the user wants to replace it. If so, the old story is moved to the logs directory (with a .bak extension), and the new version is saved. If the user doesn't want to save, the script informs them it will keep the old story. If a story is saved, a log is created or amended for the saved stories of that day. 
