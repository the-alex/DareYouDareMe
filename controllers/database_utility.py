import keys
from parse_rest.connection import register
from parse_rest.user import User as ParseUser
from parse_rest.datatypes import Object as ParseObject


class posts(ParseObject):
    pass

class Dares(ParseObject):
    pass


class DatabaseManager(object):
    """Helps with database operations, yo"""
    def __init__(self):
        register(keys.APPLICATION_ID, keys.REST_API_KEY, master_key=None)

    def add_user(self, username, password):
        # The following code is not excellent. In fact, it bugs out
        # when a username is already in use. I should be able to fix it,
        # but I am too tired. (Alex C. // Sat 10:26 am)
        try:
            newUser = ParseUser.signup(username, password)
        except:
            return False
            
        newUser.save()
        return True

    def get_userID_from_username(self, p_username):
        try:
            userID = ParseUser.Query.get(username = p_username)
            
            return userID.objectId
        except:
            return None



    def get_dares_with_userid(self, p_userID):
        try:
            user_dares = posts.Query.filter(userID=p_userID)

            dare_id = []

            for object_id in user_dares:
                #print dir(object_id)
                dare_id.append(object_id.dareID)
            
            to_return = []
            for thing_id in dare_id:
                try:
                    to_return.append(Dares.Query.get(objectId=thing_id))
                except:
                    continue

            return to_return

        except:
            return None


    def check_for_user(self, username):
        return ParseUser.Query.get(username = username)

    def get_needed_dares(self):
        return Dares.Query.filter(done__ne=True).filter(verified__ne=True)

    def get_verified_dares(self):
        return Dares.Query.filter(done__ne=True).filter(verified = True)

    def get_single_dare(self, id):
        return Dares.Query.filter(id=id)

    def save_dare(self, dare_things):
        dare = Dare()
        dare.title = dare_things['title']
        dare.description = dare_things['description']
        dare.bounty = dare_things['bounty']
        try:
            dare.save()
            return True
        except:
            return False

