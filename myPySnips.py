# Print Names Right Justified, taking maximum name length as padding length 
mynames = ['Abhinay', 'Rakesh', 'Santosh', 'Rama Krishna', 'Bhaskar', 'Venu']
print '\n'.join([x.rjust(max(map(len,mynames))) for x in mynames])

# Hacker News : Title - URL
from urllib import urlopen
from BeautifulSoup import BeautifulSoup
print 'Hacker News\n-----------'
soup = BeautifulSoup(urlopen('http://news.ycombinator.com/').read())
classTitle = soup.findAll(attrs={'class' : 'title'})
for td in classTitle:
    if getattr(td.find('a'),'string',None) not in (None, 'More'):
        print getattr(td.find('a'),'string',None)
	print td.find('a')['href'] 
	print '-' * 130
