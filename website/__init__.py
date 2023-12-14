import pdb
from flask import Flask
import sass
from website.views import views
from website.pman import pman
from flask_cors import CORS

def create_app():
    sass.compile(dirname=('website/static/sass','website/static/css'))
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'not_important_rn_but_maybe_add_a_secure_one_later' #some random string here
    app.config['hardstop'] = None # set this in case you want to suddenly close a connection

    CORS(app)

    #app.jinja_env.globals.update(some_global = some_global) #can be used for variables or functions

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(pman)
    return app
