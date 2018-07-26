import requests, bs4, re


link='http://www.dictionary.com/list/a/54'
dic=requests.get(link)
dic.raise_for_status()
soup=bs4.BeautifulSoup(dic.text, "lxml")
letterlist=soup.select('.letter-navigation a')

f=open('dictionary.txt','w')

for j in range(0,26):
	link=letterlist[j+1].get('href')
	while 1>0:
		dic=requests.get(link)
		dic.raise_for_status()
		soup=bs4.BeautifulSoup(dic.text, "lxml")

		warmsoup=soup.select('.word a')
		for i in range(0,len(warmsoup)):
			x=warmsoup[i].text.find('|')	
			if x>=0:
				warmsoup[i].text=warmsoup[i].text[:x-2]
			if bool(re.match('^[a-zA-Z]+$',warmsoup[i].text)):
				f.write(warmsoup[i].text+'\n')
				print(warmsoup[i].text) 

		Nextpage=soup.select('.pagination a')
		n=len(Nextpage)
		if Nextpage[n-1].text=='>' or Nextpage[n-2].text=='>':
			if Nextpage[n-1].text=='>':
				n=n-1
			else:
				n=n-2
			link=Nextpage[n].get('href')
		else:
			break		

f.close()