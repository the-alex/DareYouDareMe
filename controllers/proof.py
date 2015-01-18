from flask import *
from database_utility import DatabaseManager


proof  = Blueprint('proof', __name__, template_folder='templates')

@proof.route('/proof', methods=['GET', 'POST'])
def proof_route():
    id = request.form['id']
    url = request.form['url']
    db = DatabaseManager()

    userid = db.give_proof(url, id, session)
    return render_template("/")
