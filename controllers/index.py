from flask import *
import os

index = Blueprint('index', __name__, template_folder='views')

@index.route('/', methods=['GET'])
def index_route():
    pass

