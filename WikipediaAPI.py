import wikipedia

# returns the number of results for the search
def getNumberOfResults(query):
    #query = input(str("Enter your search"))
    results = wikipedia.search(query,suggestion=True)
    return (len(results[0]))

# returns a list of suggestions for the search if a word is spelled wrong
def getSuggestions(query):
    suggestions = wikipedia.suggest(query)
    return suggestions

#returns full list of all possible results
def getSearchResults(query):
    suggestions = wikipedia.search(query)
    return suggestions

#Returns the title of the article
def getTitle(query):
    page = wikipedia.page(query)
    return page.title
#returns the summary of the article
def getSummary(query):
    summary = wikipedia.summary(query, sentences=1)
    return summary

#returns a list of image links for the search
def getImages(query):
    page = wikipedia.page(query)
    images = page.images
    return images

#Returns the URL of the page
def getURL(query):
    page = wikipedia.page(query)
    url = page.url
    return url

def getPage(query):
    page = wikipedia.page(query)
    return page