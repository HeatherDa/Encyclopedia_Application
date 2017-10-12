
from flask import Flask, render_template, request, g, redirect, url_for
import os
import Database
import sqlite3
import WikipediaAPI, StarWarsAPI, ImageAPI

# Picks the name of the database.
DATABASE = 'history.sqlite'
#DATABASE = '/Encyclopedia_Application/history.sqlite'

loggedIn = False
app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
#def index():
    # Creates an instance of database.
    # with app.app_context():
    #     cur = get_db().cursor()
  #  if request.method == 'GET':
  #      return render_template('webpage.html')
  #  elif request.method == 'POST':
        # return request.get_data()
        # return request.form[]
        # return request.form.get('cbox1')
# TODO I'm drawing a blank on a better way to do this, but for now...:
   #     if request.form.get('cboxA'):
   #         summary = WikipediaAPI.getSummary(1)
   #         starwars = StarWarsAPI.StarWarsAPI.getData(StarWarsAPI.StarWarsAPI)
   #         images = ImageAPI.ImageSearch.key
   #     else:
   #         if request.form.get('cboxW'):
   #             summary = WikipediaAPI.getSummary(1)
   #         if request.form.get('cboxS'):
   #             starwars = StarWarsAPI.StarWarsAPI.getData(StarWarsAPI.StarWarsAPI)
   #         if request.form.get('cboxI'):
   #             images = ImageAPI.ImageSearch.key


    #    return redirect(url_for('index', wiki=summary, starwars=starwars, pictures=images))


def index():
    # Creates an instance of database.
    # with app.app_context():
    #     cur = get_db().cursor()
    return render_template("homestyle.html")



@app.route('/searchresults', methods=['GET', 'POST'])
def searchresults():
    if request.method == 'POST':
        try:
            search_word = request.form['search']
            msg = ("search word is: " + search_word)
        except:
            msg = ("Unable to copy word")
        try:
            sent = ""
            for checkbox in 'cbox1', 'cbox2', 'cbox3':
                value = request.form.get(checkbox)
                if value:
                    sent = sent + checkbox + ", "
            msg2 = (sent)
        except:
            msg2 = ("nothing checked")
        finally:
            return render_template("results.html", msg=msg2)



@app.route('/login', methods=['GET', 'POST'])
def loginRoute():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        # inputValues = request.get_data()
# TODO  Add validation for login using database
        loggedIn = True
        print("got to end of login!  " + str(loggedIn))
        return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signupRoute():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
# TODO  Add credentials to databaase
        return redirect(url_for('index'))


'''the following db code is from...
 http://flask.pocoo.org/docs/0.12/patterns/sqlite3/'''
# Method that creates the database if one does not exist.
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Process for closing connection.
@app.teardown_appcontext
def close_connection(exception):
    print("teardown thing reached")
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

'''Makes dictionary from rows '''
# Conversion method for turning database results (tuples)
# into a dictionary.
def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


    # g.db.row_factory = make_dicts

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return (rows[0] if rows else None) if one else rows

'''Here is how you can use it:

for user in query_db('select * from users'):
    print user['username'], 'has the id', user['user_id']'''

# init_db()


if __name__ == '__main__':
    app.run(debug=True)