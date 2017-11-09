import requests
import ujson as json

#function that gets the api key from api.txt
#do NOT upload api.txt to GitHub
def getKey():
       file = open("api.txt","r")
       key = file.readline()
       file.close()
       return key


#ImageSearch class that returns the first image link found depending on query
class ImageSearch:
    def __init__(self):
              self.key = getKey()
        #the actual function to call for an image link, with a query
    def newImage(self,query):
            formatedURL = "https://www.googleapis.com/customsearch/v1?key={0}" \
                     "&cx=017800523099077225978:er15x8rnv_i&q={1}&searchT" \
                     "ype=image&fileType=jpg&imgSize=medium&alt=json".format(self.key,query)

            request = requests.get(formatedURL)
            json_data = json.loads(request.content)
            print(json_data)
            picture = ""
            pictureList = []
            try:
                count = 0
                while count <9:
                    picture = json_data["items"][count]["link"]
                    count+=1
                    print(picture)
                    pictureList.append(picture)

            except KeyError:
                    print("Something went wrong try again")
                    picture = "Something went wrong,try again."

            return pictureList


#Test Code
#image = ImageSearch()
#picture = image.newImage("Potatoes")
#for i in picture:
#    print(i)
#print(len(picture))
#print(picture[1])
#print(picture[2])
#print(picture[3])