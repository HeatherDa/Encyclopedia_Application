
from flask import Flask, render_template, request, g
import os
import Database
import sqlite3

# Picks the name of the database.
DATABASE = '/Encyclopedia_Application/history.sqlite'

app = Flask(__name__)


@app.route('/')
def index():
    # Creates an instance of database.
    # with app.app_context():
    #     cur = get_db().cursor()
    return render_template('webpage.html')

@app.route('/login', methods=['GET', 'POST'])
def loginRoute():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        inputValues = request.get_data()
        return str(inputValues)

@app.route('/signup')
def signupRoute():
    return render_template('signup.html')


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


if __name__ == '__main__':
    app.run(debug=True)