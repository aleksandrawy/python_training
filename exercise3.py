#iterowac po adresach url, wyslac requesty do tych stron, zliczy wystapienia slowa jakiegos, pokazac jako slownik

import requests
import pprint

def count_words_on_website(url, words):
    dict = {}
    r = requests.get(url, verify=False)
    for i in words:
        #dict[i] = len(re.findall(i, str(r.text)))
        dict[i] = r.text.count(i)
    #print(dict)

    return dict


urls = ["http://google.com", "http://onet.pl", "http://wp.pl"]
words = ["za", "przeciw", "prawda"]
d = {}
for i in urls:
    d[i] = count_words_on_website(i, words)

pprint.pprint(d)




