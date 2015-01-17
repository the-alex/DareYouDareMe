from flask import *
import os

account = Blueprint('account', __name__, template_folder='views')

@account.route('/account', methods=['GET', 'POST'])
def account_route():
    pass

