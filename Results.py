import StarWarsAPI
import WikipediaAPI

def getWikipedia(word):
    wikiList = WikipediaAPI.getSearchResults("hello")
    wikiDict = dict.fromkeys(wikiList)
    print(wikiDict)
    for key, value in wikiDict.items():
        try:
            word = WikipediaAPI.getPage(key)
            wikiDict[key] = [word.pageid, word.url, word.content]
        except:
            wikiDict[key] = "delete"
    return(wikiDict)


def getList(word):
    wikiList = WikipediaAPI.getSearchResults(word)
    starList = StarWarsAPI.StarWarsAPI(word).getData()
    final_list = set(starList + wikiList)
    return (final_list)

print (getWikipedia("hello"))