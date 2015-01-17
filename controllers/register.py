from flask import *
import os

register = Blueprint('register', __name__, template_folder='templates')

@register.route('/register', methods=['GET', 'POST'])
def register_route():
    list_of_usernames = ['testuser', 'alex', 'preeti', 'devin', 'erin']

    options = {
        "error_message": None # if something went wrong, this should be replaced
                             # with a string that says what went wrong
    }

    if "username" in session: # not currently logged in
        return redirect(url_for('account'))

    else:
        if request.method =='GET':
            return render_template("register.html", **options)
        
        else:
            if not request.form.get('username'):
                options["error_message"] = "Please choose a non-empty username"

            if request.form.get('username') in list_of_usernames:
                options["error_message"] = "Username already taken, please choose another"
            
            if not request.form.get('password'):
                options["error_message"] = "Please choose a stronger password"
            
            # attempt to add to db
            added_to_db = True
            if added_to_db: # Assume that the user was successfully added to the db
                return render_template("login.html")
            else:
                options["error_message"] = "Error adding user to the db"


    return render_template("register.html", **options)
