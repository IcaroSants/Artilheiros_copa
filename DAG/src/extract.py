from bs4  import BeautifulSoup
from urllib.request import urlopen


class Extract(object):
    def __init__(self,url):
        self.url = url
    
    def getPage(self):
        page = urlopen(self.url)
        return BeautifulSoup(page,"html.parser")

    def getTag(self,tag):
        html = self.getPage()
        return html.find_all(tag)
    
