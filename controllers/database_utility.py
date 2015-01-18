import keys
from parse_rest.connection import register
from parse_rest.user import User as ParseUser
from parse_rest.datatypes import Object as ParseObject

class Dares(ParseObject):
    pass

class DatabaseManager(object):
    """Helps with database operations, yo"""
    def __init__(self):
        register(keys.APPLICATION_ID, keys.REST_API_KEY, master_key=None)

    def add_user(self, username, password):
        newUser = ParseUser.signup(username, password)
        newUser.save()

    def check_for_user(self, username):
        return ParseUser.Query.get(username = username)

    def get_dares(self):
        return Dares.Query.all()

    def get_single_dare(self, id):
        return Dares.Query.filter(id=id)

