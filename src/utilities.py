from classifier import filterTweet
from regexWordFilter import *
from gensim import corpora
from lshash import LSHash
import math
import nltk
from nltk import FreqDist
import linecache
from content_url import summarizeFile

stopwords = ['http', 'www', 'com', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
threshold=1.0;

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

def eventIdentification(dictionaryFile, corpusFile, outputFile):
	outputVector = []
	tempDict = {}
	
	corpus = corpora.MmCorpus(corpusFile)
	dictionary = corpora.Dictionary.load(dictionaryFile)
	#print "Unique Tokens:", dictionary.__len__()
	lsh = LSHash(20, dictionary.__len__())
	index = 0
	for index in range(len(corpus)):
		denseVector = getDenseVector(corpus[index], lsh.input_dim)
		result = lsh.query(denseVector)
		
		#print denseVector
		
		#no similar tweets
		if(result == []):
			#print "No Similar Tweets for: ", index
			tempDict[tuple(denseVector)] = len(outputVector)
			outputVector.append([index])
			lsh.index(denseVector)
			continue
		
		assigned = False
		for vector in result:
			if(getDistance(vector, denseVector) == True):
				ev = tempDict[tuple(vector[0])]
				outputVector[ev].append(index)
				tempDict[tuple(denseVector)] = ev
				#for ind in range(len(outputVector)):
					#done = False
					#for tweetNo in outputVector[ind]:
						#if (tweetNo == tempDict[tuple(vector[0])]):
							#outputVector[ind].append(index)
							#done = True
							#break
					#if done == True:
						#break
				assigned = True
				break
		
		if assigned == False:
			tempDict[tuple(denseVector)] = len(outputVector)
			outputVector.append([index])
			
		lsh.index(denseVector)
		
		
	with open(outputFile, 'w') as out:
		for vector in outputVector:
			line = ""
			for index in vector:
				line += "," + str(index)
			out.write(line[1:]+"\n")
	
	del outputVector
	del tempDict
	#outputVector = []
	#tempDict = []
	
	#corpus = corpora.MmCorpus(corpusFile)
	#dictionary = corpora.Dictionary.load(dictionaryFile)
	##print "Unique Tokens:", dictionary.__len__()
	#lsh = LSHash(20, dictionary.__len__())
	#index = 0
	#for index in range(len(corpus)):
		#denseVector = getDenseVector(corpus[index], lsh.input_dim)
		##sparseVector = getSparseVector(denseVector)
		#result = lsh.query(denseVector, distance_func="cosine")
		#tempDict.append(denseVector)
		##print denseVector
		
		##no similar tweets
		#if(result == []):
			##print "No Similar Tweets for: ", index
			#outputVector.append([index])
			#lsh.index(denseVector)
			#continue
		
		#minDistance = 1000000
		#i = 0
		#for vector in result:
			#distance = getDistance(vector, denseVector)(list(vector[0]), sparseVector)
			#if (cosine > maxSimilarity):
				#maxSimilarity = cosine
				#i = tempDict.index(list(vector[0]))

		#if (maxSimilarity > threshold):
			#for ind in range(len(outputVector)):
				#done = False
				#for tweetNo in outputVector[ind]:
					#if (tweetNo == i):
						#outputVector[ind].append(index)
						#done = True
						#break
				#if done == True:
					#break
		
		#else:
			#outputVector.append([index])
			#print maxSimilarity
			
		#lsh.index(denseVector)
		
	#with open(outputFile, 'w') as out:
		#for vector in outputVector:
			#line = ""
			#for index in vector:
				#line += "," + str(index)
			#out.write(line[1:]+"\n")
	
	#del outputVector
	#del tempDict
	##print "Please check the output file:", outputFile
			
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
	
def getSparseVector(vector):
	sparseVector = [index for index, value in enumerate(vector) if value == 1]
	return sparseVector
	
def getCosine(vector1, vector2):
     vec1 = getSparseVector(vector1)
     vec2 = getSparseVector(vector2)
     intersection = set(vec1) & set(vec2)
     
     numerator = sum([vec1[x]*vec2[x] for x in intersection])
     sum1 = sum([x**2 for x in vec1])
     sum2 = sum([x**2 for x in vec2])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)
     if not denominator:
        return 0.0 
     else:
        return float(numerator) / denominator
	
#def getEventId(events, index):
	#i = 0
	#for event in events:
		#if(str(index) in event):
			#return i
		#i = i + 1
	#return -1

def getEventTweets(tweetFile, eventFile, outputFile):
	events = []
	eventTweets = []
	with open(eventFile, 'r') as eventsList:
		for event in eventsList:
			eventL = event.strip().split(",")
			if (len(eventL) > 3):
				events.append([int(ev) for ev in eventL])
	#print events
	with open(tweetFile, 'r') as tweets:
		tweetLines = tweets.readlines()
	
	for event in events:
		eventTweets.append([tweetLines[tweet].strip() for tweet in event])
	#with open(tweetFile, 'r') as tweets:
		#index = 0
		#for tweet in tweets:
			#eventId = getEventId(events, index)
			#index = index + 1
			#if (eventId == -1):
				#continue
			#if (eventId in eventTweets):
				#eventTweets[eventId].append(tweet.strip())
			#else:
				#eventTweets[eventId] = [tweet.strip()]
	index = 1
	for eventTweet in eventTweets:
		with open(outputFile+str(index), 'w') as out:
			for tweet in eventTweet:
				out.write(tweet+"\n")
		index = index + 1
	
	print "Total outputFiles(events):", (index-1), "with prefix:", outputFile
		
#print getSparseVector([0,1,0,1])

def summarize(inputFile, no, outputFile):
	with open(outputFile, 'w') as output:
		for i in range(no):
			with open(inputFile+str(i+1), 'r') as eventFile:
				summary = summarizeFile(eventFile)
				if summary != None:
					print summary
					output.write(summary+"\n")
	print "Check output file:", outputFile
			
