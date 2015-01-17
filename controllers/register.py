from flask import *
import os

register = Blueprint('register', __name__, template_folder='views')

@register.route('/register', methods=['GET', 'POST'])
def register_route():
    pass

