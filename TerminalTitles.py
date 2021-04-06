#!/usr/bin/python3
# -*- coding: utf-8 -*- 

"""
Make a comment title for source code. 
Adds two rows of equals signs and a title centred in uppercase.

Example:

<!-- ======================================================================= -->
<!--                              HELLO, WORLD!                              -->
<!-- ======================================================================= -->

"""
# std libs
import os
import json
# site-packages
try: 
	import pyperclip as clipboard
except:
	print("Please install the dependancies \"pip3 install -r requirements.txt\"")
	exit(1)


# ==============================================================================
#                                GLOBAL VARIABLES
# ==============================================================================

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
LANG_CONF = "languages.json"

# ==============================================================================
#                              LANGUAGES MANAGEMENT
# ==============================================================================

def config_load():
	"""Load the json containing languages comments characters definitions."""

	confPath = os.path.join(SCRIPT_PATH, LANG_CONF)

	if not os.path.exists(confPath):
		print("ERROR - " + confPath + " doesn\'t exist.")
		print("Bye.")
		exit(1)

	with open(os.path.join(SCRIPT_PATH, LANG_CONF)) as f:
		return json.load(f)

# ==============================================================================
#                                  USER INPUTS
# ==============================================================================

def set_language():
	"""Ask for user input to choose a language."""

	langs = config_load()
	# generate the question
	msg = str("Please choose a language:\n")
	for k in range(len(langs)):
		msg += str(k) + " - " + langs[str(k)]["name"] + "\n"
	msg += str(len(langs)) + " - other\n"

	# parse the input	
	choice = input(msg)
	if choice == str(len(langs)):
		comment, commentEnd = set_comment()
	else:
		try:
			comment, commentEnd = langs[choice]["beginComment"],\
								langs[choice].get("endComment", None)
		except KeyError:
			print("Incorrect input")
			return set_language()
	return comment, commentEnd


def set_comment():
	"""Ask for user inputs for comments characters"""
	comment = input("Enter the comment characters\n" + \
					"Start of line characters:\n")
	commentEnd = input("End of line characters:\n")

	return comment, commentEnd


def set_title():
	"""Ask for user input for the title"""	
	title = input("Title:\nq to quit\n")

	if title.lower() in ('q', ''):
		print("Bye.")
		exit(0)

	return title


		
# ==============================================================================
#                                      MAIN
# ==============================================================================

def gen_comment(title, comment, commentEnd, l=80):
	"""Generate the title commented"""

	comment += " "
	if commentEnd: commentEnd = " " + commentEnd
	else: commentEnd = ""
	endLen = len(commentEnd) if commentEnd else 0
	# lignes
	hr = '=' * ( l - len(comment) - endLen )
	sep = f"{comment}{hr}{commentEnd}\n"
	# spaces before the title
	spaces = " " * (( l - len(title) - len(comment) - endLen )//2)
	# spaces after the title
	# handle uneven titles
	if commentEnd:
		lenFirstPart = len(title) + len(comment)
		if ( lenFirstPart & 1) != 0:
			spacesEnd = spaces + " "
		else:
			spacesEnd = spaces
		# Generate title part
		txt = f"{comment}{spaces}{title.upper()}{spacesEnd}{commentEnd}\n"
	else:
		txt = f"{comment}{spaces}{title.upper()}\n"
	# generate the all block
	result = f"{sep}{txt}{sep}"

	return result


if __name__ == "__main__":
	
	try:
		comment, commentEnd = set_language()
		title = set_title()
		while True:
			clipboard.copy(gen_comment(title, comment, commentEnd))
			print("Title copied to clipboard")
			title = set_title()
	except KeyboardInterrupt:
		print("\nBye.")
		exit(0)
