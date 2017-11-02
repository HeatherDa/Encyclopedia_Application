import requests
import ujson as json

#Declare class with the search string
#Currently can only search people in the star wars Universe
#anything else will return a "NA" response
class StarWarsAPI:
    def __init__(self,search):
        self.search = search
        self.baseURL = "http://swapi.co/api"
#call the getData method to get information on the person searched for
#Currently returns a list of data that contains: name, gender,date of birth,starships piloted, movie appearances, race, planet of origin
# in that particular order
    def getData(self):
        list = []
        formatedUrl = requests.get("{0}/{1}/?search={2}".format(self.baseURL, "people", self.search))
        try:
            json_data =json.loads(formatedUrl.content)
            results = json_data["results"]



            if len(results) == 0:
                list.append("NA")
                return list
            else:
                ships = ""
                films = ""
                specie = ""
                world = ""
                list.append(results[0]["name"])
                list.append(results[0]["gender"])
                list.append(results[0]["birth_year"])
                if len(results[0]["starships"]) > 0:
                    for ship in results[0]["starships"]:
                        ships += self.getStarShip(ship) +", "
                    ships = ships[:-2]
                    list.append(ships)
                else:
                    ships = "NA"
                    list.append(ships)
                if len(results[0]["films"]) > 0:
                    for film in results[0]["films"]:
                        films += self.getFilms(film) +", "
                    films = films[:-2]
                    list.append(films)
                else:
                    films = "NA"
                    list.append(films)
                if len(results[0]["species"]) > 0:
                    for species in results[0]["species"]:
                        specie += self.getSpecies(species) + ", "
                    specie = specie[:-2]
                    list.append(specie)
                else:
                    specie = "NA"
                    list.append(specie)
                if results[0]["homeworld"] != 0:
                    world += self.getHomeWorld(results[0]["homeworld"]) + ", "
                world = world[:-2]
                list.append(world)
        except (Exception):
            list.append("Too many requests today; please try again tomorrow!")
            return list
        finally:
            return list



#Below are helper methods for the getData method, please ignore
    def getStarShip(self,ships):
        formatedUrl = requests.get(ships)
        json_data = json.loads(formatedUrl.content)
        name = json_data["name"]
        return name

    def getFilms(self,film):
        formatedUrl = requests.get(film)
        json_data = json.loads(formatedUrl.content)
        name = json_data["title"]
        return name

    def getSpecies(self,species):
        formatedUrl = requests.get(species)
        json_data = json.loads(formatedUrl.content)
        name = json_data["name"]
        return name

    def getHomeWorld(self,world):
        formatedUrl = requests.get(world)
        json_data = json.loads(formatedUrl.content)
        name = json_data["name"]
        return name


#TEST CODE
#search = input(str("Enter search: "))
#api = StarWarsAPI(search)
#list = api.getData()
#for element in list:
#    print(element)

