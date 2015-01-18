from flask import *

from database_utility import DatabaseManager

about = Blueprint('about', __name__, template_folder='templates')

@about.route('/about', methods=['GET'])
def about_route():

    # If username is available in session, logout button is available 
    logout_available = 'username' in session

    return render_template("about.html", logout_available=logout_available)

