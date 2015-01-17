import keys
from parse_rest.connection import register
from parse_rest.user import User as ParseUser
from parse_rest.datatypes import Object as ParseObject

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
            options["error_message"] = "This user already exists!"
            return render_template("register.html", **options)

        newUser.save()

    def check_for_user(self, username):
        return ParseUser.Query.get(username = p_username)
