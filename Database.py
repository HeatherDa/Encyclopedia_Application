import sqlite3

# Global variables, change the sqlite_file file path if necessary
sqlite_file = '/Users/DarthVader/Desktop/Encyclopedia_Application/history.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
table_name = 'History'
col1 = 'search_ID'
col2 = 'search_item'

# Database class


class Database:

    # create database table
    def create_table(self):

        c.execute('CREATE TABLE TABLE_NAME(col1 INTEGER PRIMARY KEY NULL, col2 TEXT)')

        conn.commit()

    # plug in user input from textbox to save item to database
    def add_result(self, item):

        search_item = item

        try:
            c.execute('INSERT INTO TABLE_NAME(col2) VALUES (?)', search_item)

        except sqlite3.IntegrityError:
            print('Error with PRIMARY KEY')

        conn.commit()

    # returns rows of search items stored in database, use in the combobox for search history
    def display_all(self):

        c.execute('SELECT * FROM TABLE_NAME')

        all_rows = c.fetchall()

        for row in all_rows:
            return row

        conn.commit()

    # deletes the table, for testing purpose
    def delete_table(self):

        c.execute('DROP TABLE TABLE_NAME')

        conn.commit()

    # closes database connection
    def close_db(self):

        conn.close()