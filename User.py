# '''User Object Class'''
# import Database
# import bcrypt
#
# #database = Database.Database()
#
#
# class User(object):
#     def __init__(self, user_name, password, first_name, last_name, email, user_id=None):
#         self.user_id = user_id
#         self.user_name = user_name
#         self.password = password
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#
#
#     def __repr__(self):
#         return '{id}:{un}\n**********\n{em}\n{f} {l}'.format(id=self.user_id, un=self.user_name,
#                                                                   em=self.email, f=self.first_name,
#                                                                   l=self.last_name)
#
#     def __str__(self):
#         return self.__repr__()
#
# class UserManager():
#     '''Manager the user's of this application'''
#
#     def __init__(self):
#         self.database = Database.Database()
#
#     def add_user(self, first_name, last_name, user_name, password, email):
#         '''Add a user to the database'''
#         if self.find_user(user_name, email) is None:
#             password_hash = self._hash_password(password)
#             user = User(first_name, last_name, user_name, email, password_hash)
#             self.database.add_user(user)
#         else:
#             raise RuntimeError('User already exists')
#
#     def find_user(self, user_name, email=''):
#         '''looks for username and email'''
#         user = self.database.get_user(user_name)
#         if user is not None:
#             return user
#         return self.database.find_user_with_email(email)
#
#     def validate_credentials(self, user_name, password):
#         '''validate a password matches what is in the database'''
#         user = self.database.get_user(user_name)
#         if user is None:
#             return False
#         db_hash = user.password
#         user_hash = bcrypt.hashpw(password, db_hash)
#         return user_hash == db_hash
#
#     def get_user_profile(self, user_name):
#         user = self.database.get_user(user_name)
#         return user
#
#     def _hash_password(self, password):
#         return bcrypt.hashpw(password, bcrypt.gensalt())
#
# '''Adapted from MediaCheetahEncyclopedia'''
