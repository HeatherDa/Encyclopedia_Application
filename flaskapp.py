
from flask import Flask, render_template, request, g, redirect, url_for, session

import WikipediaAPI, StarWarsAPI, ImageAPI
import Results
import Models
from flask_login import login_user, logout_user, LoginManager, login_required



# loggedIn = False
app = Flask(__name__)

# secret key & sqlalchemy database link
app.secret_key = 'tiniest little secrets'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///searches.sqlite'

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

# for logging in user and loading them
@login_manager.user_loader
def load_user(user_id):
    print("debug: user id is " + user_id)
    return Models.User.query.filter_by(user_id=user_id).first()

# required for login
@app.route('/protected')
@login_required
def protected():
    return "protected area"

# logs user out
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return "Logged out"

@app.route('/', methods=['GET', 'POST'])
def index():
    # Creates an instance of database.
    # with app.app_context():
    #     cur = get_db().cursor()
    return render_template("homestyle.html")


# todo: test to make sure search results are getting stored with correct user_id attachted
@app.route('/searchresults', methods=['GET', 'POST'])
def searchresults():
    words = []
    info = []
    # I think this is how to get the current logged in user - requires further testing
    current_user = session.get(load_user)

    if request.method == 'POST':
        try:
            search_word = request.form['search']

            new_search = Models.Search(None, search_word, current_user)
            Models.db.session.add(new_search)
            Models.db.session.commit()

            #For Wikipedia
            words = Results.getWikipediaList(search_word)
            for w in words:
                info.append(Results.getWikiInfo(w))


            #For StarWars

        except:
            msg = ("Unable to copy word")

        finally:
            return render_template("results.html", results=info)
            #return render_template("results.html")



@app.route('/login', methods=['GET', 'POST'])
def loginRoute():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        user = Models.User.query.filter_by(username=request.form['loginUser']).first()

        if user:
            if user.password == request.form['loginPW']:
                login_user(user)

                return redirect('/')

        return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signupRoute():
    if request.method == 'GET':
        return render_template('signup.html')

    elif request.method == 'POST':
        username = request.form['signupUser']
        password = request.form['signupPW']
        firstname = request.form['signupFirst']
        lastname = request.form['signupLast']
        email = request.form.get['signupEmail']

        try:
            new_user = Models.User(None, username, password, firstname, lastname, email)
            Models.db.session.add(new_user)
            Models.db.session.commit()

            login_user(new_user)

        except RuntimeError as rte:
            print('failed to create user')

        return redirect(url_for('index'))


if __name__ == '__main__':
    init_db()
    app.run(debug=True)