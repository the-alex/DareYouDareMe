from flask import *
import os

venmoauth = Blueprint('venmoauth', __name__, template_folder='templates')

@venmoauth.route('/venmoauth', methods=['GET', 'POST'])
def account_route():
    authcode = request.args.get('code', '')
    # Save authcode to Parse User

    # Redirect back to home
    return redirect(url_for('index'))
        
@venmoauth.route('/pay/:id', methods=['GET', 'POST'])
def pay_things():
    payee = session.username
    
    dare_id = request.kwargs.get('id', '')

