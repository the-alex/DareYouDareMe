from flask import *
import os

@account.route('/venmoauth', methods=['GET', 'POST'])
def account_route():
    authcode = request.args.get('code', '')
    # Save authcode to Parse User

    # Redirect back to home
    return redirect(url_for('index'))
        
