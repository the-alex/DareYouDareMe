from flask import *
from database_utility import DatabaseManager

new_dare = Blueprint('new_dare', __name__, template_folder='templates')

@new_dare.route('/new', methods=['GET', 'POST'])
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
        dare['title'] = request.form.get("dare_title")
        dare['description'] = request.form.get("dare_description")
        dare['bounty'] = request.form.get("bounty")

        dare['latitude'] = session['latlon']['lat']
        dare['longitude'] = session['latlon']['lon']

        if not dare['bounty'].isdigit():
            options["errors"] = "Bounty is not a number"

        # send to the database
        dm = DatabaseManager()
        db_success = dm.save_dare(dare, session)
        if db_success:
            options["successful_dare_post"] = True
            return redirect('/')
        else:
            options['errors'] = "Danger, Will Robinson!"


    return render_template("new_dare.html", **options)





