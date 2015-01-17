from flask import *
import os

new_dare = Blueprint('new_dare', __name__, template_folder='views')

@new_dare.route('/newDare', methods=['GET', 'POST'])
def new_dare_route():
    pass

