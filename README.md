# Business Card Parser

## Entegra Systems Programming Challenge

author: Brian McDevitt

email: briandmcdevitt@gmail.com

language: Python 3.6

## How to Build/Run

I used Python 3.6 for this program. [Download](https://www.python.org/downloads/release/python-366/)

## [Virtualenv Setup](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
### 1. Installing Virtualenv
	* On macOS and Linux: (in cmd)
		- $python3 -m pip install --user virtualenv
	* On Windows:
		- $py -m pip install --user virtualenv
### 2. Creating Virtualenv (in some directory)
	* On macOS and Linux:
		- $python3 -m virtualenv env
	* On Windows:
		- $py -m virtualenv env
### 3. Activating Virtualenv
	* On macOS and Linux:
		- source env/bin/activate
	* On Windows:
		- .\env\Scripts\activate
		
## Setup Project
### 1. Make new directory
	- $mkdir project
	- $cd project
### 2. Clone repo (or download zip file)
	- $git clone https://github.com/brianmcdevitt/Business_Card_Parser.git
### 3. Install Requirements (will take a minute)
	* On macOS and Linux: (in cmd)
		- $pip install -r requirements.txt
	* On Windows:
		- $python -m pip install -U pip setuptools
	* Then on both Systems run this command:
		- $python -m spacy download en
		
## Run Project
### 1. Go to python files
	- $cd python_files
### 2. Run main.py
	- $python main.py ../examples/example1.txt
	- (I have provided a number of example inputs, but it can be run on other input .txt files)
### 3. Run unit tests
	- $python test_basic.py
		

## PROMPT

We’ve created a new smartphone app that enables users to snap a photo of a business card and have the information from the card automatically extracted and added to their contact list. We need you to write the component that parses the results of the optical character recognition (OCR) component in order to extract the name, phone number, and email address from the processed business card image. We have provided you with a basic specification [1] and a series of example inputs [2] and would like you to provide the implementation.
