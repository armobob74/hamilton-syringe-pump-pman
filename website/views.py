from flask import Blueprint, render_template, render_template_string, request, flash, jsonify, redirect, url_for
import os
import sass

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
def index():
    sass.compile(dirname=('website/static/sass','website/static/css'))
    return render_template('index.html')

@views.route('/form/<filename>', methods=['GET'])
def getForm(filename):
    """
    used to get generic forms
    if form needs keyword arguments, put that logic in the getKwargs() function
    """
    # if kwargs are necessary, modify the getKwargs function to put them in
    kwargs = getKwargs(filename) 

    if filename in os.listdir('website/templates/forms'):
        return render_template(f'forms/{filename}',**kwargs)
    else:
        return f"The file \"{filename}\" was not found"

def getKwargs(filename):
    """
    return the keywords needed by templates
    """
    return {}
