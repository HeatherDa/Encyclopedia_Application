import sqlite3

# Global variables, change the sqlite_file file path if necessary
sqlite_file = '/Users/DarthVader/Desktop/Encyclopedia_Application/history.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

table_user = 'Users'
userID = 'user_ID'
user_name = 'user_name'
password = 'user_password'
first = 'user_first_name'
last = 'user_last_name'
table_search = 'History'
col1 = 'search_ID'
col2 = 'search_item'
col3 = 'user_ID'

# Database class


class Database:

    # create database table
    def create_search_table(self):

        c.execute('CREATE TABLE TABLE_SEARCH(col1 INTEGER PRIMARY KEY NULL, col2 VARCHAR,'
                  ' col3 INTEGER FOREIGN KEY REFERENCES TABLE_USER(userID))')

        conn.commit()

    # create database table
    def create_user_table(self):
            c.execute('CREATE TABLE TABLE_USER(userID INTEGER PRIMARY KEY NULL,user_name VARCHAR,'
                      ' password VARCHAR, first TEXT, last Text)')

            conn.commit()



    # plug in user input from textbox to save item to database
    def add_result(self, item):

        search_item = item

        try:
            c.execute('INSERT INTO TABLE_SEARCH(col2) VALUES (?)', search_item)

        except sqlite3.IntegrityError:
            print('Error with PRIMARY KEY')

        conn.commit()

    def add_user(self, uname, pw, fname, lname):

        try:
            c.execute('INSERT INTO TABLE_USER(user_name, password, first, last) VALUES (?, ?, ?, ?)'
                      , (uname, pw, fname, lname))
        except sqlite3.IntegrityError:
            print('Error with PRIMARY KEY')

        conn.commit()

    # returns rows of search items stored in database, use in the combobox for search history
    def display_all_history(self):

        c.execute('SELECT * FROM TABLE_SEARCH')

        all_rows = c.fetchall()

        conn.commit()

        return all_rows

    # todo: test this method by feeding it a username.
    # depending on user name it should yield all the search results matching the username and ID
    def display_user_history(self, user_name):

        un = user_name

        c.execute('SELECT userID.tu, user_name.tu, col2.ts FROM TABLE_USER AS tu JOIN TABLE_SEARCH'
                  ' AS ts ON tu.userID = ts.col3'
                  ' WHERE lower(user_name) = lower(?)', un)

        user_history = c.fetchall()

        conn.commit()

        return user_history


    def check_if_user(self,username, password):

        c.execute('SELECT * FROM TABLE_USER WHERE user_name = ? AND password = ?, (username, password)')

        found = c.fetchone()

        if found:
            print('user exists')
            # todo: give permissions
        else:
            print('user does not exist')
            # todo: deny permissions


    # deletes the table, for testing purpose
    def delete_tables(self):

        c.execute('DROP TABLE TABLE_SEARCH')
        c.execute('DROP TABLE TABLE_USER')
        conn.commit()

    # closes database connection
    def close_db(self):

        conn.close()