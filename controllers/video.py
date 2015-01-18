from flask import *
from database_utility import DatabaseManager


video  = Blueprint('video', __name__, template_folder='templates')

@video.route('/video', methods=['GET', 'POST'])
def account_route():
    id = request.form.get['id']
    url = request.form.get['url']
    db = DatabaseManager()

    userid = db.get_video(url, id)
    return redirect('/')

