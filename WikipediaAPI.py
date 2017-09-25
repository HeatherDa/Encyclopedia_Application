import wikipedia

# returns the number of results for the search
def getNumberOfResults(query):
    query = input(str("Enter your search"))
    results = wikipedia.search(query,suggestion=True)
    return (len(results[0]))
# returns a list of suggestions for the search
def getSuggestions(query):
    suggestions = wikipedia.suggest(query)
    return suggestions
#Returns the title of the article
def getTitle(query):
    page = wikipedia.page(query)
    return page.title
#returns the summary of the article
def getSummary(query):
    summary = wikipedia.summary(query)
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