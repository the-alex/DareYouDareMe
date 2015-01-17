from database_utility import DatabaseManager
from database_utility import ParseUser
from flask import *
import os

logout = Blueprint('logout', __name__, template_folder='templates')

@logout.route('/logout', methods=['GET', 'POST'])
def logout_route():
    options = {
        'error': None
    }

    if 'username' in session:
        del session['username']

    return render_template("login.html", **options)
