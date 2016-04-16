from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os
import sys


def get_soup(url,header):
  return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'lxml')

searches = ["boy","girl","man","woman","person","human","guy","gal","facial expression"]

for search in searches:
    qname = sys.argv[-1] + " " + search
    # you can change the query for the image  here  
    query= '+'.join(qname.split())
    url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
    print url
    header = {'User-Agent': 'Mozilla/5.0'} 
    soup = get_soup(url,header)

    images = [a['src'] for a in soup.find_all("img", {"src": re.compile("gstatic.com")})]
    directory = "./" + sys.argv[-1]
    if not os.path.exists(directory):
        os.mkdir(directory)
    #print images
    for i in range(len(images)):
      raw_img = urllib2.urlopen(images[i]).read()

      f = open(directory + "/" + qname +str(i)+".jpg", 'wb')
      f.write(raw_img)
      f.close()
