from classifier import filterFile
from subprocess import call
from utilities import *

print "\n\n\tWelcome to Sub-event detection from Twitter"
print "\t-------------------------------------------\n"

def menu():
	print "\n    Select operation:\n"
	print "  1. Extract Tweets"
	print "  2. Build Dictionary"
	print "  3. Build Corpus"
	print "  4. Event Identification"
	print "  5. Summarization"
	print "  6. Exit"
	

def main():
	while True:
		menu()
		try:
			choice = input("Enter Here: ")
			if (choice == 6):
				""" GoodBye! """
				print "Exiting system.. Have a nice day!"
				exit(0)
			elif (choice == 1):
				""" execute shell script to extract tweets """
				inputFile = raw_input("Input File: ")
				outputFile = raw_input("Output File: ")
				call(['./build.sh', inputFile, outputFile+"temp"])
				filterFile(outputFile+"temp", outputFile)
				call(['rm', outputFile+"temp"])
				print "Please use the output file", outputFile,"for further stages"
			elif (choice == 2):
				"""Build dictionary and save for future use"""
				inputFile = raw_input("Tweet File (The output of tweet extraction): ")
				outputFile = raw_input("Dictionary output File: ")
				buildDictionary(inputFile, outputFile)
			elif (choice == 3):
				"""Build corpora and save for future use"""
				inputFile = raw_input("Tweet File (The output of tweet extraction): ")
				dictionaryFile = raw_input("Dictionary File (The output of Dictionary Generation): ")
				corpusFile = raw_input("Corpus output file (with .mm extension): ")
				buildCorpus(inputFile, dictionaryFile, corpusFile)
			elif (choice == 4):
				dictionaryFile = raw_input("Dictionary File (The output of Dictionary Generation): ")
				corpusFile = raw_input("Corpus file (The output of Corpus Generation): ")
				inputFile = raw_input("Tweet File (The output of tweet extraction): ")
				outputFile = raw_input("Prefix for OutputFiles: ")
				eventIdentification(dictionaryFile, corpusFile, outputFile)
				getEventTweets(inputFile, outputFile, outputFile)
			elif (choice == 5):
				inputFile = raw_input("Event file prefix (output in Event Identification): ")
				no = raw_input("No of files (output in Event Identification): ")
				outputFile = raw_input("Output File: ")
				summarize(inputFile, int(no), outputFile)	
			else:
				print "Invalid Choice!"
		except (NameError, SyntaxError, ValueError) as e:
			print "Invalid Choice!"
		except IOError:
			print "Please enter valid (existing) file names"

# start the program
main()
		
