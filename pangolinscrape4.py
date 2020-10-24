from urllib2 import urlopen as ureq
from urllib2 import Request as req
from bs4 import BeautifulSoup as soup
import lxml
agent='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19'
headers={
"User-Agent":agent
}
url='https://www.google.com/search?q=pangolin'
#"User-Agent":agent
html=req(url, headers=headers)
try:
    gold=ureq(html);
#url.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19')
#page_soup=open('html')
    page_soup=soup(gold, "lxml")
    divs=page_soup.findAll("div", {"class":"rc"})
    for div in divs:
        gold=div.h3.a
        print gold.text
except urllib2HTTPError, e:
    print "HTTP error:", e.code
    exit(1)
