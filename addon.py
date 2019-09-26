from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
URL = "http://thedollop.libsyn.com/"
@plugin.route('/')
def main_menu():
    items = [
      {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "http://static1.squarespace.com/static/5cae25d58dfc8c9bbc638a9b/t/5d1237d497f79e0001145c49/1561475041378/The+Dollop+2018+logo+nameless.png"},
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('episodes'),
            'thumbnail': "http://static1.squarespace.com/static/5cae25d58dfc8c9bbc638a9b/t/5d1237d497f79e0001145c49/1561475041378/The+Dollop+2018+logo+nameless.png"},
   ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup = mainaddon.get_soup(URL)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes():
    soup = mainaddon.get_soup(URL)
    playable_podcast = mainaddon.get_playable_podcast(soup)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()
