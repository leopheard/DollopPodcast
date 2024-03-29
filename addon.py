from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://rss.art19.com/the-dollop"
url2 = "https://dollopengland.libsyn.com/rss"
@plugin.route('/')
def main_menu():
    items = [
      {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://content.production.cdn.art19.com/images/8e/72/72/44/8e727244-6c7d-424f-bcf4-e5ff2ab5cab7/9f27657af86c0f796164eca0c1d3ed8b9ddddee8ba4105dfa37dc60c92b611753de791c55e46120e0f5a88207981c2546677e6806bcdd0e455a185e54a42e57d.jpeg"},
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://content.production.cdn.art19.com/images/8e/72/72/44/8e727244-6c7d-424f-bcf4-e5ff2ab5cab7/9f27657af86c0f796164eca0c1d3ed8b9ddddee8ba4105dfa37dc60c92b611753de791c55e46120e0f5a88207981c2546677e6806bcdd0e455a185e54a42e57d.jpeg"},
        {
            'label': plugin.get_string(30002), 
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://is1-ssl.mzstatic.com/image/thumb/Podcasts113/v4/11/58/64/1158643e-230b-e9b2-955d-387fc1422d2e/mza_5441154048432550917.jpg/600x600bb.jpg"},
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
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items
@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items
if __name__ == '__main__':
    plugin.run()
