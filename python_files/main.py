#!/usr/bin/env python3

"""
Brian McDevitt
email: briandmcdevitt@gmail.com

Business Card Parser

This program parses the results of an optical character recognition (OCR) component 
in order to extract the name, phone number, and email address from the processed 
business card image.

RUN FORMAT:
$python main.py ../examples/example1.txt

"""

import sys
import re
import spacy #natural language processing module
nlp = spacy.load('en')

"""
ContactInfo(String name, String phoneNumber, String email)

    String getName() : returns the full name of the individual (eg. John Smith, Susan Malick)
    String getPhoneNumber() : returns the phone number formatted as a sequence of digits
    String getEmailAddress() : returns the email address

"""
class ContactInfo:

	def __init__(self, name, phoneNumber, email):
		self.name = name
		self.phoneNumber = phoneNumber
		self.email = email

	def getName(self):
		return self.name

	def getPhoneNumber(self):
		return self.phoneNumber

	def getEmailAddress(self):
		return self.email

"""
parseFile(FilePath ocrfile): returns ContactInfo

Takes input of the ocrfile and returns the ContactInfo object it represents

"""

def parseFile(ocrfile):

	document = readFile(ocrfile)

	return getContactInfo(document)

"""
readFile(FilePath ocrfile): returns String

Takes the file path and reads the entire file as a string and returns it

"""

def readFile(ocrfile):

	with open(ocrfile) as f:
		document = f.read()

	return document

"""
getContactInfo(String document): returns ContactInfo

Takes the document string and parses the name, phone number, and email
address from it. It then creates a new instance of ContactInfo with these
values as input and returns it.

"""

def getContactInfo(document):

	name = parseName(document)
	phoneNumber = parsePhoneNumber(document)
	email = parseEmail(document)

	contactInfo = ContactInfo(name, phoneNumber, email)

	return contactInfo

"""
parseName(String document): String

Takes in the document string and returns the name on the business card if there
is one and returns "not found" if there isn't.

Module: spacy (natural language processing)
documentation: https://spacy.io/api/

We pass the document line by line to nlp()- the natural language processor.
This determines the entities in the string. We check if any of these entity has
a label of PERSON. If so, we assume that is the person's name.

Issues: Can't allows find the name or sometimes includes other words with the full
name. Returns after first occurence of PERSON. This wouldn't work if it makes a
mistake and the actual name is farther down. 

"""

def parseName(document):

	lines = document.split('\n')
	#Iterate through each line of the business card
	for line in lines:
		parsedLine = nlp(line)
		
		#Search all the entities found to see if there is a name
		for ent in parsedLine.ents:
			if ent.label_ == "PERSON":
				return ent.text

	return "not found"

"""
parseName(String document): return String

Takes in the document string and returns the telephone number of the person if there
is one and "not found" if there isn't

Utilized Regular Expressions to find telephone numbers of various formats
regex source: https://stackoverflow.com/questions/16699007/regular-expression-to-match-standard-10-digit-phone-number

Supported formats:
18005551234
1 800 555 1234
+1 800 555-1234
+86 800 555 1234
1-800-555-1234
1 (800) 555-1234
(800)555-1234
(800) 555-1234
(800)5551234
800-555-1234
800.555.1234
800 555 1234x5678
8005551234 x5678
1    800    555-1234
1----800----555-1234

Also it will ignore numbers with fax in front of it.

"""

def parsePhoneNumber(document):

	phoneregex = r'(^(?!(fax\s*:?))\D*\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$)'
	r = re.compile(phoneregex, re.M|re.I)
	formatedPhoneNumber = r.search(document)
	if formatedPhoneNumber:
		unformatedPhoneNumber = re.sub("\D", "", formatedPhoneNumber.group()) #get rid of the formating of the number
		return unformatedPhoneNumber
	else:
		return "not found"

"""
parseEmail(String document): return String

Takes in the document string and returns the email address of the person if there
is one and "not found" if there isn't.

Utilized Regular Expressions to find email addresses of various formats.
regex source: http://emailregex.com

"""

def parseEmail(document):

	emailregex = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
	r = re.compile(emailregex, re.M)
	email = r.search(document)
	if email:
		return email.group()
	else:
		return "not found"


"""Main function"""

def main(argv=None):
    ocrfile = sys.argv[1]

    contactInfo = parseFile(ocrfile)

    print("Name: ", contactInfo.getName())
    print("Phone: ", contactInfo.getPhoneNumber())
    print("Email: ", contactInfo.getEmailAddress())

if __name__ == "__main__":
    main(sys.argv)