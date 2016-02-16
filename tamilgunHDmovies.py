from bs4 import BeautifulSoup
import unicodedata
import urllib2, sys
from tabulate import tabulate



def load_website(site):
    header = {'User-Agent': 'Mozilla/5.0'}
    request = urllib2.Request(site,headers=header)
    page = urllib2.urlopen(request)
    soup = BeautifulSoup(page,'html.parser')
    return soup



def get_list(page):
	
	formatted = []

	soup = load_website(page)
	movie_metas = soup.find("div",{"class":"row video-section meta-maxwidth-230"}).findAll("div",{"class":"col-sm-4"})

	for movie in movie_metas:
		details = movie.getText().split('\n')
		details.sort()
		mName = details[-1]
		details.remove(mName)
		mName = unicodedata.normalize('NFKD', mName).encode('ascii','ignore')
		m_time = "(not available)"
		
		for x in details:
			if " ago" in x :
				m_time = x
				break

		formatted.append([mName,m_time])

	return formatted


def get_all_pages(soup):
	all_pages = []
	uls = soup.find("ul",{"class":"pagination"})

	lis = uls.findAll("li")
	for page in lis :
		
		if len(page.attrs['class'])> 1 :
			try :
				all_pages.append(unicodedata.normalize('NFKD', page.find("a")["href"]).encode('ascii','ignore'))

			except :
				comma=1

	return all_pages
	    

if __name__ == '__main__':
	
	url = "http://tamilgun.com/categories/hd-movies/"
	
	soup = load_website(url)

	all_pages = get_all_pages(soup)

	print "Total %s pages found"%(str(len(all_pages)))

	table = []

	for url in all_pages:
		table.extend(get_list(url))

	print tabulate(table)




