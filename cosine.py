import re, math
from collections import Counter

WORD = re.compile(r'\w+')
event= []
eventlist=[]
threshold=1.0;
def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0 
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

def subEvent(vector,num):
	global event, eventlist, threshold
	if len(event) == 0:
		event.append(vector)
		eventlist.append([num])
	else:
		maxnum=0
		for i in range(len(event)):
			cosine = get_cosine(vector,event[i]);
			if cosine > maxnum:
				tweetno=i
				maxnum=cosine
		if maxnum >= threshold:
			eventlist[tweetno].append(num)
		else:
			event.append(vector)
			eventlist.append([num])
#print eventlist

f=open("kshitij",'r')
array=[]
for line in f:
	array.append(line)
f.close()
#print array

'''
text1 = 'So sick of seeing celebs tweets  woo voted  who cares if you voted we all want  Barack Obama to win hands down Obama ........'
text2 = 'America  If you only vote for one President this year  make it  Barack Obama'
text3 = 'Come on America  this is your chance to be intelligent'
'''
'''
vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)
'''
vector = []
for i in range(len(array)):
	subEvent(text_to_vector(array[i]),i)
#vector.append(text_to_vector(i))
#print vector[0].values()
#print vector[1].values()
#cosine = get_cosine(vector1, vector2)
print eventlist
#print 'Cosine:', cosine

