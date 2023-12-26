from flask import Flask
from controllers.main_controller import main_blueprint

app = Flask(__name__, template_folder='views/templates')

# Register blueprints (controllers)
app.register_blueprint(main_blueprint)
