from urllib2 import urlopen as ureq
from bs4 import BeautifulSoup as soup
import lxml
url='http://deschulz.net/plaincontent.html'
html=ureq(url)
page_soup=soup(html, "lxml")
body1=page_soup.body
print(body1.text.strip())
