import requests
import re
from bs4 import BeautifulSoup

def get_soup1(url1):
    page = requests.get(url1)
    soup1 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup1))
    return soup1
get_soup1("http://thedollop.libsyn.com/")
def get_soup2(url2):
    page = requests.get(url2)
    soup2 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup2))
    return soup2
get_soup2("https://thedollop.libsyn.com/webpage/page/1/size/10000")

def get_playable_podcast(soup2):
    subjects = []
    for content in soup2.find_all('td'):
        try:        
            link = content.find('a')
            link = link.get('href')
            print("\n\nLink: ", link)
            title = content.find('a', class_="postTitle")
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'href': link,
                'title': title,
                'thumbnail': "http://static1.squarespace.com/static/5cae25d58dfc8c9bbc638a9b/t/5d1237d497f79e0001145c49/1561475041378/The+Dollop+2018+logo+nameless.png",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast(playable_podcast):
    items = []
    for podcast in playable_podcast:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['href'],
            'is_playable': True,
    })
    return items

def get_playable_podcast1(soup1):
    subjects = []
    for content in soup1.find_all('td', limit='10'):
        try:        
            link = content.find('a')
            link = link.get('href')
            print("\n\nLink: ", link)
            title = content.find('a', class_="postTitle")
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'href': link,
                'title': title,
                'thumbnail': "http://static1.squarespace.com/static/5cae25d58dfc8c9bbc638a9b/t/5d1237d497f79e0001145c49/1561475041378/The+Dollop+2018+logo+nameless.png",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['href'],
            'is_playable': True,
    })
    return items
