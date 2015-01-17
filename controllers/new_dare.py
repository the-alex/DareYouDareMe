from flask import *
import os

new_dare = Blueprint('new_dare', __name__, template_folder='templates')

@new_dare.route('/newDare', methods=['GET', 'POST'])
def new_dare_route():
    
    options = {
        "show_new_dare_form" : False,
        "successful_dare_post": False, 
        "errors" = None
    }

    if "username" not in session: # not currently logged in
        return redirect(url_for('login'))


    if request.method =='POST':
        dare_title       = request.forms.get("dare_title")
        dare_description = request.forms.get("dare_description")
        dare_bounty      = request.forms.get("bounty")

        if not dare_bounty.isdigit():
            options["errors"] = "Bounty is not a number"

        # send to the database
        db_success = True
        if db_success:
            options["successful_dare_post"] = True

    return render_template("new_dare.html", **options)





