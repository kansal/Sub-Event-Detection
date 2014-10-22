import re
import random

urlPattern = re.compile(r'https?:[\S]+')

def findURLS(eventFile):
	urls = []
	content = eventFile.read()
	eventFile.seek(0,0)
	urls = urlPattern.findall(content)
	if urls == []:
		return None
	index = random.randint(0, len(urls) - 1)
	url = urls[index]
	return url
	

	
