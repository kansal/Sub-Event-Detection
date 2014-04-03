from classifier import filterTweet
from regexWordFilter import *
from gensim import corpora
from lshash import LSHash

stopwords = ['http', 'www', 'com', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']

def buildDictionary(fileName, dictionaryFile):
	with open(fileName) as filteredTweets:
		dictionary = corpora.Dictionary([word for word in filterSpecialChar(filterHash(tweet)).lower().split() if word not in stopwords] for tweet in filteredTweets)
	if(dictionaryFile.endswith(".dict") != True):
		dictionaryFile += ".dict"
	dictionary.save(dictionaryFile)
	print "\n  Dictionary serialized to: ", dictionaryFile
def buildCorpus(fileName, dictionaryFile, corpusFile):
	dictionary = corpora.Dictionary.load(dictionaryFile)
	with open(fileName) as filteredTweets:
		corpus = [dictionary.doc2bow(filterSpecialChar(filterHash(tweet)).lower().split()) for tweet in filteredTweets]
	if(corpusFile.endswith(".mm") != True):
		corpusFile += ".mm"
	corpora.MmCorpus.serialize(corpusFile, corpus)
	print "\n  Corpus serialized to: ", corpusFile
def getDenseVector(vector, length):
	denseVector = [0]*length
	for i in vector:
		denseVector[i[0]] = 1
	return denseVector

def subEventDetection(dictionaryFile, corpusFile, outputFile):
	outputVector = []
	tempDict = {}
	corpus = corpora.MmCorpus(corpusFile)
	dictionary = corpora.Dictionary.load(dictionaryFile)
	lsh = LSHash(30, dictionary.__len__())
	index = 0
	for index in range(len(corpus)):
		denseVector = getDenseVector(corpus[index], lsh.input_dim)
		result = lsh.query(denseVector, num_results = 50, distance_func = "cosine")
		#no similar tweets
		if(result == []):
			outputVector.append([index])
			continue
		assigned = False
		for vector in result:
			if(getDistance(vector, denseVector) == True):
				for ind in range(len(outputVector)):
					done = False
					for tweetNo in outputVector[ind]:
						if (tweetNo == tempDict[vector]):
							outputVector[ind].append(index)
							done = True
							break
					if done == True:
						break
				assigned = True
				break
		if assiged == False:
			outputVector.append([index])
		lsh.index(denseVector)
		tempDict[tuple(denseVector)] = index
	with open(outputFile, 'w') as out:
		for vector in outputVector:
			line = ""
			for index in vector:
				line += ", " + str(index)
			out.write(line[2:]+"\n")
	print "Please check the output file:", outputFile
def getDistance(vectorA, vectorB):
	match = 0
	index = 0
	for index in range(len(vectorA)):
		if (vectorB[index] == vectorB[index]):
			match = match + 1
	length = min (vectorA.count(1), vectorB.count(1))
	if(match > length/2):
		return True
	return False
