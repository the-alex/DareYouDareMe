from database_utility import DatabaseManager
from database_utility import ParseUser
from flask import *

login = Blueprint('login', __name__, template_folder='templates')

@login.route('/login', methods=['GET', 'POST'])
def login_route():
    options = {
        'error': None
    }

    if request.method == 'POST':
        # Get the text entered in the fields.
        p_username = request.form.get('username')
        p_password = request.form.get('password')

        lat = request.form.get("lat")
        lon = request.form.get("lon")

        # Provide access to database
        dbManager = DatabaseManager()

        try:
            user = ParseUser.login(p_username, p_password)
        except:
            options['error'] = "Incorrect username or password"
            return render_template("login.html", **options)

        print user.username
        session['username'] = user.username
        session['latlon']  = {
            "lat": lat,
            "lon": lon
        }


        return redirect('/')




    return render_template("login.html", **options)
