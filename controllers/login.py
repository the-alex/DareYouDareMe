from database_utility import DatabaseManager
from database_utility import ParseUser
from flask import *
import os

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
        # Provide access to database
        dbManager = DatabaseManager()

        # TODO: Implement try/catch on login
        user = ParseUser.login(p_username, p_password)

        # add to session? I'm going to sleep. // Alex C.
        print user.username
        session['username']= user.username

        return redirect('/')




    return render_template("login.html", **options)
