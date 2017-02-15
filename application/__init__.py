from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import *

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from application.shells import *
from application import *

import application.models
import application.views

#
# Trying to figure out how to build this into a views.py but at the momment I'm
# failing to understand why that doesn't work.
#
