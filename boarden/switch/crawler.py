
from bs4 import BeautifulSoup
import urllib
from urllib import request

def makeUrl(word):
	return 'https://dictionary.cambridge.org/dictionary/english-chinese-traditional/'+ word


def gethtml(url):
	response = urllib.request.urlopen(url)
	html = response.read()
	return html

def setTagForClass(tag):
	tagc = "."+tag
	return tagc

def setTagForID(tag):
	tagc = "#"+tag
	return tagc

def getSoup(html):
	soup = BeautifulSoup(html, "lxml")
	return soup

def getDefinitions(soup,tag):
	definitions = [de.get_text() for de in soup.select('{}'.format(tag)) ]
	return definitions

def getDefinitionsShortcut(word):
	return getDefinitions(getSoup(gethtml(makeUrl(word))),setTagForClass("trans"))[0]

def is_chinese(uchar):         
    if u'\u4e00' <= uchar<=u'\u9fff':
        return True
    else:
        return False

def getExamp(word):
 	examp = getDefinitions(getSoup(gethtml(makeUrl(word))),'.examp')[0][1:-1]
 	examped = ''
 	for c in examp:
 		if is_chinese(c):
 			print(c)
 			break
 		else:
 			examped+=c
 	return examped


#getDefinitions(getSoup(gethtml(makeUrl('abstemious'))),setTagForClass("trans"))


print(getDefinitionsShortcut('bathroom'))

print(getExamp('cry'))















