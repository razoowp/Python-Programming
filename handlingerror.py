from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def information(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        soup = BeautifulSoup(html,"lxml")
        total_info = soup.p
    except AttributeError as e:
        return None
    return total_info

link = ""

about_info = information(link)

if about_info is None:
    print("No information found !!!")
else:
    print(about_info.get_text())
