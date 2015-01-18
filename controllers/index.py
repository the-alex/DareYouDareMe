from flask import *

from database_utility import DatabaseManager

index = Blueprint('index', __name__, template_folder='templates')

@index.route('/', methods=['GET'])
def index_route():
    if 'username' in session:
        db_man = DatabaseManager()
        needed_dares = db_man.get_needed_dares(float(session['latlon']['lat']), float(session['latlon']['lon']))
        claimed_dares = db_man.get_claimed_dares()
        return render_template("index.html", needed_dares = needed_dares, claimed_dares = claimed_dares)
    else:
        return redirect("/login")

