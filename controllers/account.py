from flask import *
import os

account = Blueprint('account', __name__, template_folder='templates')

@account.route('/account', methods=['GET', 'POST'])
def account_route():
    return render_template("account.html")

