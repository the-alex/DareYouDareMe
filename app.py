from flask import Flask, render_template, session, url_for, redirect, request, flash
import controllers

# Used for sessions
from os import urandom
from datetime import timedelta

app = Flask(__name__, template_folder='templates')

app.secret_key = urandom(24)
app.permanent = True
app.permanent_session_lifetime = timedelta(minutes=(60*24)) # One day


# Example how to add a blueprint to hierarchy
# app.register_blueprint(controllers.login)


app.register_blueprint(controllers.login)
app.register_blueprint(controllers.index)
app.register_blueprint(controllers.account)
app.register_blueprint(controllers.register)
app.register_blueprint(controllers.new_dare)
app.register_blueprint(controllers.venmoauth)
app.register_blueprint(controllers.about)
app.register_blueprint(controllers.logout)
app.register_blueprint(controllers.video)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(401)
def access_denied(e):
    return render_template('401.html'), 401

# comment this out using a WSGI like gunicorn
# if you dont, gunicorn will ignore it anyway
if __name__ == '__main__':
    # listen on external IPs
    app.run(host='0.0.0.0', port=3000, debug=True)


