from parse_rest.connection import register
from parse_rest.user import User as ParseUser
from parse_rest.datatypes import Object as ParseObject

APPLICATION_ID = "HC69OFTmEYGO6uXqiNzL8SwDX4vzg8fikXul8F39"
REST_API_KEY = "HYOrBxaYg23WNM1p7c9iLjMedFjWpMud6pNQrdUE"
MASTER_KEY = "nneshWYCXhVtaJWlRjzXxUkl5YFRzeN2ATgzRkMD"

register(APPLICATION_ID, REST_API_KEY, master_key=None)

class Dares(ParseObject):
    pass

class Posts(ParseObject):
    pass
