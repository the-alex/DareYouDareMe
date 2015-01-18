from flask import *

from database_utility import DatabaseManager
import os

about = Blueprint('about', __name__, template_folder='templates')

@about.route('/about', methods=['GET'])
def about_route():
    return render_template("about.html")

