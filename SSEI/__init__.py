from flask import Flask
from SSEI.blueprints import simple_page

app = Flask(__name__)


app.register_blueprint(simple_page)
