from flask import *
from database_utility import DatabaseManager
import os

venmoauth = Blueprint('venmoauth', __name__, template_folder='templates')

@venmoauth.route('/venmoauth/:userid', methods=['GET', 'POST'])
def account_route():
    authcode = request.args.get('code', '')
    userid = request.args.get('userid', '')

    # Save authcode to Parse User
    dm = DatabaseManager()
    user = dm.check_for_user(userid)
    user.venmoCode = authcode
    user.save()

    # Redirect back to home
    return redirect(url_for('index'))
        
@venmoauth.route('/pay/:id', methods=['GET', 'POST'])
def pay_things():
    payee = session.username
    
    dare_id = request.args.get('id', '')

