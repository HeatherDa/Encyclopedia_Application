import WikipediaAPI
import requests
from bs4 import BeautifulSoup
import StarWarsAPI
import ImageAPI
def getWikiInfo(word):
    wlist = []
    url = 'https://en.wikipedia.org/wiki/'
    if " " in word:
        word = word.replace(" ", "_")
        url = url + word
    else:
        url = url + word

    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    soup.prettify()

    sum = ""
    try:
        sum = WikipediaAPI.getSummary(word)
    except:
        sum = "Click link to view page"

    wlist.append(word)
    wlist.append(url)
    wlist.append(sum)
    return(wlist)

def getWikipediaList(word):
    return WikipediaAPI.getSearchResults(word)

def getStarWarsList(word):
    x = StarWarsAPI.StarWarsAPI(word).getData()
    print(x)
    return x
def getPicture(search_word):
    image = ImageAPI.ImageSearch()
    picture = image.newImage(search_word)
    print(picture)
    return picture