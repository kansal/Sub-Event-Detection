from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.nlp.stemmers.english import stem_word
from extractURL import findURLS
import urllib, re
import sys
LANGUAGE = "english"
SENTENCES_COUNT_1 = 3
SENTENCES_COUNT_2 = 2
IMAGE_COUNT = 1


    # Make a function to take input as file
    # extract all urls using extractURL.findURLS
    # select a random url and get url content by first part (below)
    # read content of file (file.read())
    # append content of URL in the above string
    # execute the below
    #parser = PlaintextParser.from_string(file+urlsummary content, Tokenizer(LANGUAGE))
def summarizeFile(inputFile):
	summarizer = LsaSummarizer(stem_word)
	summarizer.stop_words = get_stop_words("english")
	url = findURLS(inputFile)
	if url != None:
		if url[-1] == '.':
			url = url[0:-1]
		#print (url)
		#urlContent = 'Summary from URL ['+url+']: \n'
		urlContent = ''
		try:
			parser = HtmlParser.from_url(url, Tokenizer("english"))		
			for sentence in summarizer(parser.document, 3):
				urlContent = urlContent + str(sentence) + '\n'
		except:
			#print (sys.exc_info()[0])
			urlContent = ''
	content = inputFile.read()
	parser = PlaintextParser.from_string(content, Tokenizer(LANGUAGE))
	#summarizer = LsaSummarizer(stem_word)
	#summarizer.stop_words = get_stop_words(LANGUAGE)
	#summary = 'Event Summary: \n'
	summary = ''
	try:
		for sentence in summarizer(parser.document, SENTENCES_COUNT_1):
			summary = summary + str(sentence) + '\n'
	except AssertionError:
		return None
	if url != None:
		return summary + urlContent
	return summary
