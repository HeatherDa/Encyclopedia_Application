'''Database - Adapted from media cheetah'''
import sqlite3
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, create_engine
import sqlalchemy.types as types
from sqlalchemy.orm import mapper, sessionmaker, relationship
from User import User
from Search import Search

class Database():

    def __init__(self, connection_string='sqlite:///Encyclopedia_Application.database.sqlite3'):
        self.sql_file = connection_string
        self.engine = self._get_connection()
        self.metadata = MetaData(bind=self.engine)
        try:
            self.users, self.searches = self._create_tables()
            self._map_users()
            self._map_search()

        except Exception as e:
            print(e)

    def _get_connection(self):
        engine = create_engine(self.sql_file)
        return engine

    def _get_session(self):
        session = sessionmaker(bind=self.engine)
        return session()

    def _create_tables(self):
        users = Table('Users', self.metadata,
                      Column('user_id', Integer, primary_key=True),
                      Column('user_name', String(50)),
                      Column('password', String(100)),
                      Column('first_name', String(25)),
                      Column('last_name', String(25)),
                      Column('email', String(75)),
                      Column('currency', Integer))
        users.create(self.engine, checkfirst=True)
        searches = Table('Searches', self.metadata,
                      Column('search_id', Integer, primary_key=True),
                      Column('search_name', String(50)),
                      Column('user_id', Integer, ForeignKey('Users')))
        searches.create(self.engine, checkfirst=True)
        return users, searches

    def _map_users(self):
        try:
            mapper(User, self.users)
        except:
            pass

    def _map_search(self):
        try:
            mapper(Search, self.searches)
        except:
            pass

    def add_user(self, user_data):
        session = self._get_session()
        session.add(user_data)
        session.commit()

    def get_user(self, username):
        session = self._get_session()
        for user in session.query(User).\
            filter(User.user_name==username):
            return user

    def find_user_with_email(self, email):
        session = self._get_session()
        for user in session.query(User).\
            filter(User.email==email):
            return user