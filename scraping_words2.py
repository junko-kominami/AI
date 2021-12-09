import requests
from bs4 import BeautifulSoup

import MeCab
import collections


def get_article(url):
    p_tags = [500]
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    i=1
    flag=1

    words_new = []
    words = []
    while(flag):
        i=i+1            
        p_tags = soup.select('p')
        article=(p_tags[i].get_text())
        if(i>len(p_tags[i].get_text())):
            break            
#        print(article)
        m = MeCab.Tagger ('mecabrc')
        node = m.parseToNode(article)
        while node:
            words.append(node.surface)
            node = node.next
    print(words)
#        words_new = words.append
#    print(words_new)
#        print(i)
    c = collections.Counter(words)
#    print(c.most_common(30))       

    return words

#    m = MeCab.Tagger ('-Owakati')
#    m = MeCab.Tagger ('mecabrc')
#    m = MeCab.Tagger ('-Ochasen')
#    m = MeCab.Tagger ('-Oyomi')


#url = "http://www.archifuture-web.jp/headline/457.html"
url = "https://liginc.co.jp/568003"
#url = "https://liginc.co.jp"
get_article(url)


