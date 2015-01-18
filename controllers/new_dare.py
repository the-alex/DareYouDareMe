from flask import *
from database_utility import DatabaseManager
import os

new_dare = Blueprint('new_dare', __name__, template_folder='templates')

@new_dare.route('/newDare', methods=['GET', 'POST'])
def new_dare_route():

    options = {
        "show_new_dare_form" : False,
        "successful_dare_post": False,
        "errors" : None
    }

    if "username" not in session: # not currently logged in
        return redirect('/login')


    if request.method =='POST':
        dare = {}
        dare['title']       = request.forms.get("dare_title")
        dare['description'] = request.forms.get("dare_description")
        dare['bounty']      = request.forms.get("bounty")

        if not dare['bounty'].isdigit():
            options["errors"] = "Bounty is not a number"

        # send to the database
        dm = DatabaseManager()
        db_success = dm.save_dare(dare)
        if db_success:
            options["successful_dare_post"] = True

    return render_template("new_dare.html", **options)





