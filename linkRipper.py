import re, urllib

i = 1
BASE_URL = 'http://sheger.ertale.com/'
PAGE_URL = 'http://sheger.ertale.com/index.php/category/yechewata-engida'
#http://sheger.ertale.com/index.php/category/sheger-buffe/
#http://sheger.ertale.com/index.php/category/sheger-cafe/
#http://sheger.ertale.com/index.php/category/yechewata-engida/

with open("sheger_buffe_links.txt", 'w') as myFile:
	myFile.write('')

def createFullLink(links):
	with open("sheger_buffe_links.txt", 'a') as myFile:
		for link in links:
			myFile.write(BASE_URL+link+'\n')

def getLinks():
	global BASE_URL,PAGE_URL, i

	if i > 1:
		data = urllib.urlopen(PAGE_URL +"/page/" + str(i) +"/").read()
	else:
		data = urllib.urlopen(PAGE_URL).read()

	links = re.findall('(?=audio.php)(.*mp3)', data)
	if len(links) == 0:
		print "finished!!"
		return

	createFullLink(links)
	i = i + 1
	getLinks()

print "loading links ..."	
getLinks()

	
			


