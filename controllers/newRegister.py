from parse_rest.connection import register
from parse_rest.user import User as ParseUser
from parse_rest.datatypes import Object as ParseObject

from flask import *
import os

register = Blueprint('register', __name__, template_folder='templates')

@register.route('/register', methods=['GET', 'POST'])
def register_route():
    options = {
    # if something went wrong, this should be replaced with a string
    # that says what went wrong.
        "error_message": None
    }

    if "username" in session: # If currently logged in.
        return redirect(url_for('account'))

    else:
        if request.method == 'GET':
            return render_template("register.html", **options)

        # The method is POST. User has submitted their info.
