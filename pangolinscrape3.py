#import urllib2
from urllib2 import urlopen as open
from urllib2 import Request as req
from bs4 import BeautifulSoup as soup
import lxmlheaders={
"User-Agent":agent
}
url='https://www.google.com/search?q=pangolin'
#"User-Agent":agent
html=req(url, headers=headers)
try:
    gold=open(html);
    page_soup=soup(gold, "lxml")
    h3s=page_soup.findAll("h3", {"class":"r"})
    for h3 in h3s:
        gold=h3.a
        print gold.text
except urllib2HTTPError, e:
    print "HTTP error:", e.code
    exit(1)
