from flask import *
from database_utility import *

import os

account = Blueprint('account', __name__, template_folder='templates')

@account.route('/account', methods=['GET', 'POST'])
def account_route():
    if "username" not in session:
        return redirect("/login")

    if request.method == "POST":
        if request.form["delete"]:
            to_delete = request.form.get("d_id")
            d_obj = Dares.Query.get(objectId=to_delete)
            print dir(d_obj)
            d_obj.delete()

            p_obj = posts.Query.filter(dareID=to_delete)
            print dir(p_obj[0])
            p_obj[0].delete()




    db = DatabaseManager()

    userid = db.get_userID_from_username("testuser")
    if userid is None:
        return redirect('/login')

    user_dares = db.get_dares_with_userid(userid)


    # print dir(user_dares[0])
    # print type(user_dares)
    # print user_dares

    options = {
        "dares": user_dares,
        "username": "testuser",
    }

    return render_template("account.html", **options)

