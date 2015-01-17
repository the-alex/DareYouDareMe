from database_utility import DatabaseManager
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

        dbManager = DatabaseManager()



    return render_template("login.html", **options)
