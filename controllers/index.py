from flask import *
import os

index = Blueprint('index', __name__, template_folder='templates')

@index.route('/', methods=['GET'])
def index_route():
    if 'username' in session:
        return render_template("index.html")
    else:
        return redirect("/login")

