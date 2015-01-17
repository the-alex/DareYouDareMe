from database_utility import DatabaseManager

from flask import *
import os

register = Blueprint('register', __name__, template_folder='templates')

@register.route('/register', methods=['GET', 'POST'])
def register_route():
    options = {
    # if something went wrong, this should be replaced with a string
    # that says what went wrong.
        "error_message": None
    }

    if "username" in session: # If currently logged in.
        return redirect(url_for('account'))

    else:
        if request.method == 'GET':
            return render_template("register.html", **options)

        # User has submitted their info.
        else:
            # Get the entered information.
            # p_ denotes "Possible"
            p_username = request.form.get('username')
            p_password = request.form.get('password')
            # Check if the user entered valid information.

            # Check if the Username is valid.
            if not p_username:
                options["error_message"] = "Please enter a username"
                return render_template("register.html", **options)

            # If the username field has a string, check if that string
            # matches an entry in the database. (returns a list)

            # Open Database
            dbManager = DatabaseManager()

            # Check ...
            try:
                possibleUser = ParseUser.Query.get(username = p_username)
            except:
                possibleUser = None

            if possibleUser != None:
                # If the username is already in use ...
                if possibleUser.username == p_username:
                    options["error_message"] = "Username already in use"
                    return render_template("404.html", **options)

            # If the username is not in use, then check if the password
            # is valid.
            if not p_password:
                options["error_message"] = "Please enter a valid password"
                return render_template("register.html", **options)

            # If the password and username check out, then attempt
            # to add the user to the database.
            dbManager.add_user(p_username, p_password)
            return render_template("index.html", **options)




# -----------------------------------------------------------------------------

# Older code written by Alex L. It might not even have been wrong,
# but I wanted to rewrite it just to be sure of what was going on.
# In the end, our versions look very, very similar.

# from parse_rest.connection import register
# from parse_rest.user import User as ParseUser
# from parse_rest.datatypes import Object as ParseObject

# from flask import *
# import os

# register = Blueprint('register', __name__, template_folder='templates')

# @register.route('/register', methods=['GET', 'POST'])
# def register_route():
#     # list_of_usernames = ['testuser', 'alex', 'preeti', 'devin', 'erin']

#     options = {
#         "error_message": None # if something went wrong, this should be replaced
#                              # with a string that says what went wrong
#     }

#     if "email" in session: # if currently logged in
#         return redirect(url_for('account'))

#     else:
#         if request.method =='GET':
#             return render_template("register.html", **options)

#         else:
#             # If the email string is empty.
#             if not request.form.get('email'):
#                 options["error_message"] = "Please choose a non-empty email"

#             possibleUser = ParseUser.Query.get(email=sessions["email"])
#             # If the email is taken already ...
#             if request.form.get('email') in possibleUser:
#                 options["error_message"] = "Email already taken, please choose another"

#             if not request.form.get('password'):
#                 options["error_message"] = "Please choose a stronger password"

#             # attempt to add to db
#             added_to_db = True
#             if added_to_db: # Assume that the user was successfully added to the db
#                 return render_template("login.html")
#             else:
#                 options["error_message"] = "Error adding user to the db"


#     return render_template("register.html", **options)
