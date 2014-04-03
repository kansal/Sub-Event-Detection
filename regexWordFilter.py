from re import compile

removeUseless = compile(r'([\s]@[\S]*)|([\s]#[\S]*)|(^#[\S]*])|(^@[\S]*)|(\b[\S]{1}\b)')
specialChar = compile('[^a-zA-Z0-9 ]+')

#remove # and @ references
def filterHash(tweet):
	return removeUseless.sub('', tweet)

#remove special characters
def filterSpecialChar(tweet):
	return specialChar.sub(' ', tweet)
