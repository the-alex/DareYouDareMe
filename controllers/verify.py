from flask import *
from database_utility import DatabaseManager


verify = Blueprint('verify', __name__, template_folder='templates')

@verify.route('/verify', methods=['GET', 'POST'])
def route_verify():
    dbManager = DatabaseManager()

    user_response = request.form['verify-checkbox']
    dare_id = request.form['id']

    dare_id = dare_id.replace("-verify", "")

    # Get dare
    dare_set = dbManager.get_single_dare(dare_id)

    dare = dare_set[0]

    if user_response == "True":
        claimer = dare.claiming_user
        reward = dare.bounty
        dare.verified = True
        # Get person who claimed dare
        dbManager.award_user_points(claimer, reward)
    else:
        dare.claiming_user = ""
        dare.claimed = False

    dare.save()
    # return render_template("index.html")
    return redirect("/")
