import re

#rep >= 3
#multiple punc
# <=3 words
# >12 letters
# 1st letter small

regexEliminator = re.compile(r'(^.*(.)\2{2,}.*$)|(^.*[^a-zA-Z0-9 ]{2,}.*$)|(^([\S]+([\s]+)?){1,3}$)|(^.*[\s][^@#][\S]{12,}[\s].*$)|(^[^A-Z].*$)')

def filterTweet(tweet):
	filteredTweet = regexEliminator.sub('', tweet).strip()
	return filteredTweet
	
def filterFile(inputFile, outputFile):
	with open(inputFile) as tweetsFile:
		with open(outputFile, 'w') as filteredTweets:
			for tweet in tweetsFile:
				tweet = filterTweet(tweet)
				if(tweet != ''):
					filteredTweets.write(tweet+'\n')
	

#repitions = re.compile(r'^.*(.)\1{2,}.*$')
#multiplePunc = re.compile(r'^.*[^a-zA-Z0-9 ]{2,}.*$')
#smallTweet = re.compile(r'^([\S]+([\s]+)?){1,3}$')
#longerWords = re.compile(r'^.*[\s][^@#].{12,}[\s].*$')
#capStart = re.compile(r'^[^A-Z].*$')




