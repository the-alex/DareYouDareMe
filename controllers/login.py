from flask import *
import os

login = Blueprint('login', __name__, template_folder='templates')

@login.route('/login', methods=['GET', 'POST'])
def login_route():
    options = {
        'error': None
    }


    return render_template("login.html", **options)
