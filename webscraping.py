from urllib.request import urlopen
from bs4 import BeautifulSoup
# url = "file:///C:/Users/rajutraveller/Desktop/blog/index.html"
url = "https://www.nytimes.com/"
html = urlopen(url)
soup = BeautifulSoup(html,"lxml")
print(soup)

print(soup.h1)
print(soup.h1.get_text())
print(soup.p)
print(soup.p.get_text())

for link in soup.find_all("a"):
    print(link.get_text())
