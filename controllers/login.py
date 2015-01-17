from flask import *
import os

login = Blueprint('login', __name__, template_folder='views')

@login.route('/login', methods=['GET', 'POST'])
def login_route():
    pass

