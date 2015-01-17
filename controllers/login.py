from flask import *
import os

login = Blueprint('login', __name__, template_folder='templates')

def add_user():
    pass

@login.route('/login', methods=['GET', 'POST'])
def login_route():
    test = 5
    options = {'display': test}
    return render_template("login.html", **options)
