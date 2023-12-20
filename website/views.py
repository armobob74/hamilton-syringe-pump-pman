from flask import Blueprint, render_template
import sass

views = Blueprint('views', __name__)

@views.before_request
def beforeRequest():
    sass.compile(dirname=('website/static/sass','website/static/css'))

@views.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@views.route('/transfer', methods=['GET'])
def transferView():
    return render_template('transfer.html')

@views.route('/control', methods=['GET'])
def controlView():
    return render_template('control.html')

@views.route('/mix', methods=['GET'])
def mixView():
    return render_template('mix.html')
