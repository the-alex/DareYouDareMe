from flask import *

from database_utility import DatabaseManager
import os

index = Blueprint('index', __name__, template_folder='templates')

@index.route('/', methods=['GET'])
def index_route():
    if 'username' in session:
        db_man = DatabaseManager()
        dares = db_man.get_dares()
        return render_template("index.html", dares=dares)
    else:
        return render_template("login.html")

