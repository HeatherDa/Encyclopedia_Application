
from flask import Flask, render_template, request, g, redirect, url_for, session

import WikipediaAPI, StarWarsAPI, ImageAPI
import Results
import Models
from flask_login import login_user, logout_user, LoginManager, login_required, current_user

# loggedIn = False
import TwitterAPI
import YoutubeAPI

app = Flask(__name__)

# secret key & sqlalchemy database link
app.secret_key = 'tiniest little secrets'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///searches.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# login manager
login_manager = LoginManager()
login_manager.init_app(app)

# for debugging
app.debug = True

# creates database
def init_db():
    Models.db.init_app(app)
    Models.db.app = app
    Models.db.create_all()

# Global variables.
errorMsg = "Please fill in all fields"
# logState = False

# for logging in user and loading them
@login_manager.user_loader
def load_user(user_id):
    print("debug: user id is " + user_id)   # user_id here is returning the username of logged in user
    return Models.User.query.filter_by(user_id=user_id).first()

def load_username(username):
    return Models.User.query.filter_by(username=username).first()


def load_search(description):
    return Models.Search.query.filter_by(description=description).first()

# required for login
@app.route('/protected')
@login_required
def protected():
    return "protected area"


# logs user out
@app.route("/logout")
# @login_required       # With this activated, I get an unauthorized access message.
def logout():
    print("debug: logging out now...")
    logout_user()
    # return "Logged out"
    return render_template("homestyle.html", logState=False)





@app.route('/', methods=['GET', 'POST'])
def index():
    session.pop('username', None)
    # Creates an instance of database.
    # with app.app_context():
    #     cur = get_db().cursor()
    return render_template("homestyle.html")

@app.route('/homestyle', methods=['GET', 'POST'])
def home(logState):
    # Creates an instance of database.
    # with app.app_context():
    #     cur = get_db().cursor()

    # currentuser = session['username']
    #
    # if request.method == 'POST':
    #     search_word = request.form['search']
    #
    #     new_search = Models.Search(search_word, currentuser)
    #     Models.db.session.add(new_search)
    #     Models.db.session.commit()

    return render_template("homestyle.html", logState=logState)




# todo: test to make sure search results are getting stored with correct user_id attachted
@app.route('/searchresults', methods=['GET', 'POST'])
def searchresults():
    words = []
    info = []

    if request.method == 'POST':

        search_word = request.form['search']
        value = request.form['options']

        if 'username' in session:
            message = "you are logged in"
            currentuser = session['username']
            logState = True
            new_search = Models.Search(search_word, currentuser)
            Models.db.session.add(new_search)
            Models.db.session.commit()

            # WIKI API
            if value == 'wiki':
                # For Wikipedia
                info = []
                words = Results.getWikipediaList(search_word)
                if not words:
                    error = "There are no matches. Search again"
                    return render_template("results.html", results=info, checked=value, searched_word=search_word,
                                           logState=logState, words=error)
                else:
                    for w in words:
                        info.append(Results.getWikiInfo(w))
                    return render_template("results.html", results=info, checked=value, searched_word=search_word,
                                           logState=logState)

            # STARWARS API
            elif value == 'sw':
                try:
                    info = Results.getStarWarsList(search_word)
                    test = info[0]
                    if test == 'NA':
                        error = "There are no results for that search. Please try searching again"
                        return render_template("swerror.html", error=error, checked=value,
                                               searched_word=search_word,
                                               logState=logState)
                    else:
                        return render_template("starwars.html", person=info, error="", checked=value,
                                               searched_word=search_word,
                                               logState=logState)
                except:
                    return "too many requests using the StarWarsAPI! Try using something else."


            # IMAGE API
            elif value == 'pic':
                pictures = Results.getPicture(search_word)
                return render_template("picture.html", pictures=pictures, checked=value, searched_word=search_word,
                                       logState=logState)

            # Twitter API
            elif value == 'twit':
                tweets = TwitterAPI.TwitterAPI()
                tweet_list = tweets.getTweets(search_word)
                if not tweet_list:
                    return render_template("twitterError.html")
                else:
                    return render_template("twitter.html", checked=value, searched_word=search_word,
                                           tweetlist=tweet_list,
                                           logState=logState)
            # YouTUBE API
            elif value == 'youtube':
                videos = YoutubeAPI.youtube_search(search_word)
                if not videos:
                    uerror = "No videos found. Try searching something else"
                    return render_template("youtube.html", uerror=uerror, checked=value,
                                               searched_word=search_word,
                                               logState=logState)
                else:
                    return render_template("youtube.html", videos=videos, checked=value,
                                               searched_word=search_word,
                                               logState=logState)


            # ALL APIS
            elif value == 'all':
                list = []
                words = Results.getWikipediaList(search_word)
                for w in words:
                    list.append(Results.getWikiInfo(w))



                pictures = Results.getPicture(search_word)
                picture = pictures[0]
                # picture = ["one","two", "three"]

                info = Results.getStarWarsList(search_word)
                test = info[0]


                tweets = TwitterAPI.TwitterAPI()
                tweet_list = tweets.getTweets(search_word)

                videos = YoutubeAPI.youtube_search(search_word)


                #checks if starwars api is empty
                #if its then
                if test == 'NA':
                    error = "STARWARS API: Nothing found! Try searching again."
                    #check if wikipedia is empty
                    #if wiki is empty
                    if not words:
                        wikierror = "There are no matches. Search again"

                        #if it check if twitter is empty
                        if not tweet_list:
                            terror = "Sorry there are no tweets. Try searching again"

                            if not videos:
                                uerror = "No videos found. Try searching something else"
                                return render_template("allresults.html", error=error, person="", results=list,
                                                           picture=picture,
                                                           checked=value, searched_word=search_word, logState=logState,
                                                           wikierror=wikierror, terror=terror, uerror = uerror)
                            else:
                                return render_template("allresults.html", error=error, person="", results=list,
                                                           picture=picture,
                                                           checked=value, searched_word=search_word, logState=logState,
                                                           wikierror=wikierror, terror=terror, videos = videos)

                        else:
                            if not videos:
                                uerror = "No videos found. Try searching something else"
                                return render_template("allresults.html", person=info, error="", results=list,
                                                       picture=picture,
                                                       checked=value, searched_word=search_word, logState=logState,
                                                       tweetlist=tweet_list[:3], uerror = uerror)
                            else:
                                return render_template("allresults.html", person=info, error="", results=list,
                                                       picture=picture,
                                                       checked=value, searched_word=search_word, logState=logState,
                                                       tweetlist=tweet_list[:3], videos = videos)
                        #if wiki isnt empty
                    else:
                        if not tweet_list:
                            terror = "Sorry there are no tweets. Try searching again"
                            if not videos:
                                uerror = "No videos found. Try searching something else"
                                return render_template("allresults.html", error=error, person="", results=list, picture=picture,
                                           checked=value, searched_word=search_word, logState=logState, terror = terror, uerror = uerror)
                            else:
                                return render_template("allresults.html", error=error, person="", results=list, picture=picture,
                                           checked=value, searched_word=search_word, logState=logState, terror = terror, videos = videos)
                        else:
                            if not videos:
                                uerror = "No videos found. Try searching something else"

                                return render_template("allresults.html", error=error, person="", results=list, picture=picture,
                                           checked=value, searched_word=search_word, logState=logState, tweetlist=tweet_list[:3], uerror = uerror)
                            else:
                                return render_template("allresults.html", error=error, person="", results=list,
                                                       picture=picture,
                                                       checked=value, searched_word=search_word, logState=logState,
                                                       tweetlist=tweet_list[:3], videos=videos)

                #if starwars is not empty
                else:
                    #check wikipedia
                    if not words:
                        wikierror = "There are no matches. Search again"

                        if not tweet_list:
                            terror = "Sorry there are no tweets. Try searching again"
                            if not videos:
                                uerror = "No videos found. Try searching something else"

                                return render_template("allresults.html", person=info, error="", results=list,
                                                   picture=picture,
                                                   checked=value, searched_word=search_word, logState=logState,
                                                   wikierror=wikierror, terror = terror, uerror = uerror)
                            else:
                                return render_template("allresults.html", person=info, error="", results=list,
                                                   picture=picture,
                                                   checked=value, searched_word=search_word, logState=logState,
                                                   wikierror=wikierror, terror = terror, videos = videos)
                        else:
                            if not videos:
                                uerror = "No videos found. Try searching something else"
                                return render_template("allresults.html", person=info, error="", results=list,
                                                   picture=picture,
                                                   checked=value, searched_word=search_word, logState=logState,
                                                   tweetlist=tweet_list[:3], uerror = uerror)
                            else:
                                return render_template("allresults.html", person=info, error="", results=list,
                                                   picture=picture,
                                                   checked=value, searched_word=search_word, logState=logState,
                                                   tweetlist=tweet_list[:3], videos = videos)

                    else:
                        if not tweet_list:
                            terror = "Sorry there are no tweets. Try searching again"
                            if not videos:
                                uerror = "No videos found. Try searching something else"
                                return render_template("allresults.html", person=info, error="", results=list,
                                                   picture=picture,
                                                   checked=value, searched_word=search_word, logState=logState,
                                                   terror = terror, uerorr = uerror)
                            else:

                                return render_template("allresults.html", person=info, error="", results=list,
                                                   picture=picture,
                                                   checked=value, searched_word=search_word, logState=logState,
                                                   terror = terror, videos = videos)
                        else:
                            if not videos:
                                uerror = "No videos found. Try searching something else"

                                return render_template("allresults.html", person=info, error="", results=list, picture=picture,
                                           checked=value, searched_word=search_word, logState=logState, tweetlist = tweet_list[:3], uerror =uerror)
                            else:
                                return render_template("allresults.html", person=info, error="", results=list,
                                                       picture=picture,
                                                       checked=value, searched_word=search_word, logState=logState,
                                                       tweetlist=tweet_list[:3], videos=videos)




        #REGULAR USER
        else:
            logState = False
            message = "you are not logged in"

            # WIKI API
            if value == 'wiki':
                # For Wikipedia
                info = []
                words = Results.getWikipediaList(search_word)
                if not words:
                    error = "There are no matches. Search again"
                    return render_template("results.html", results=info, checked=value, searched_word=search_word,
                                           logState=logState, words=error)
                else:
                    for w in words:
                        info.append(Results.getWikiInfo(w))
                    return render_template("results.html", results=info, checked=value, searched_word=search_word,
                                           logState=logState)

            #STARWARS API
            elif value == 'sw':
                try:
                    info = Results.getStarWarsList(search_word)
                    test = info[0]
                    if test == 'NA':
                        error = "There are no results for that search. Please try searching again"
                        return render_template("swerror.html", error=error, checked=value,
                                               searched_word=search_word)
                    else:
                        return render_template("starwars.html", person=info, error="", checked=value,
                                               searched_word=search_word,
                                               logState=logState)
                except:
                    return "too many requests using the StarWarsAPI! Try using something else."



            # IMAGE API
            elif value == 'pic':
                pictures = Results.getPicture(search_word)
                return render_template("picture.html", pictures=pictures, checked=value, searched_word=search_word,
                                       logState=logState)






            #ALL APIS
            elif value == 'all':
                list = []
                words = Results.getWikipediaList(search_word)
                for w in words:
                    list.append(Results.getWikiInfo(w))

                pictures = Results.getPicture(search_word)
                picture = pictures[0]
                # picture = ["one","two", "three"]

                info = Results.getStarWarsList(search_word)
                test = info[0]
                if test == 'NA':
                    error = "STARWARS API: Nothing found! Try searching again."
                    if not words:
                        wikierror = "There are no matches. Search again"
                        return render_template("allresults.html", error=error, person="", results=list, picture=picture,
                                               checked=value, searched_word=search_word, logState=logState, wikierror = wikierror)
                    else:
                        return render_template("allresults.html", error=error, person="", results=list, picture=picture,
                                           checked=value, searched_word=search_word, logState=logState)
                else:
                    if not words:
                        wikierror = "There are no matches. Search again"
                        return render_template("allresults.html", person=info, error="", results=list, picture=picture,
                                           checked=value, searched_word=search_word, logState=logState, wikierror = wikierror)
                    else:
                        return render_template("allresults.html", person=info, error="", results=list, picture=picture,
                                           checked=value, searched_word=search_word, logState=logState)



@app.route('/login', methods=['GET', 'POST'])
def loginRoute():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':

        userEntry = request.form['loginUser']
        pwEntry = request.form['loginPW']

        if userEntry == "" or pwEntry == "":
            return render_template("login.html", errormsg=errorMsg)

        user = Models.User.query.filter_by(username=userEntry).first()
        print("debug: user: " + str(user))
        if user:
            if user.password == pwEntry:
                login_user(user)
                session['username'] = user.username
                logState = True
                # return redirect(url_for('home'), logState)
                return render_template("homestyle.html", logState=logState)

        return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signupRoute():
    if request.method == 'GET':
        return render_template('signup.html')

    elif request.method == 'POST':
        username = request.form['signupUser']
        password = request.form['signupPW']
        confirm = request.form['signupPW2']
        firstname = request.form['signupFirst']
        lastname = request.form['signupLast']
        email = request.form['signupEmail']

        # Verifies all fields have been filled in; otherwise, the page is reloaded
        # with an error message at top.
        if username == "" or password == "" or confirm == "" or firstname == "" or lastname == "" or email == "":
            return render_template("signup.html", errormsg=errorMsg)
        else:


            try:
                if password == confirm:
                    new_user = Models.User(username, password, firstname, lastname, email)
                    Models.db.session.add(new_user)
                    session['username'] = new_user.username
                    Models.db.session.commit()
                    # print("debug: new_user: " + new_user)
                    login_user(new_user)
                    logState = True

            except RuntimeError as rte:
                print('failed to create user')

            # return redirect(url_for('home'), logState)
            return render_template("homestyle.html", logState=logState)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)