import StarWarsAPI
import WikipediaAPI

def getList(word):
    wikiList = WikipediaAPI.getSearchResults(word)
    starList = StarWarsAPI.StarWarsAPI(word).getData()
    final_list = set(starList + wikiList)
    return (final_list)

print (getList("dark"))