from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "http://thedollop.libsyn.com/"
url2 = "https://thedollop.libsyn.com/webpage/page/1/size/10000"
@plugin.route('/')
def main_menu():
    items = [
      {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://i1.sndcdn.com/avatars-000114476892-gzl586-large.jpg"},
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://i1.sndcdn.com/avatars-000114476892-gzl586-large.jpg"},
   ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items
@plugin.route('/episodes/')
def episodes():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast = mainaddon.get_playable_podcast(soup2)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items
if __name__ == '__main__':
    plugin.run()
