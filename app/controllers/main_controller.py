from flask import Blueprint, render_template

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def home():
    return render_template('home.html', message='Welcome to my Flask App!')