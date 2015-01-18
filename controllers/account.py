from flask import *
from database_utility import DatabaseManager

import os

account = Blueprint('account', __name__, template_folder='templates')

@account.route('/account', methods=['GET', 'POST'])
def account_route():
    #if "username" not in session:
    #    return redirect("/login")
    db = DatabaseManager()

    userid = db.get_userID_from_username("testuser")
    if userid is None:
        return redirect('/login')

    user_dares = db.get_dares_with_userid(userid)


    print dir(user_dares[0])
    print type(user_dares)
    print user_dares

    options = {
        "dares": user_dares,
        "username": "testuser",
    }

    return render_template("account.html", **options)

