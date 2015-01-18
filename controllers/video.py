from flask import *
from database_utility import DatabaseManager


video  = Blueprint('video', __name__, template_folder='templates')

@video.route('/video', methods=['GET', 'POST'])
def account_route():
    id = request.form['id']
    url = request.form['url']
    db = DatabaseManager()

    userid = db.give_video(url, id)
    return redirect('/')

