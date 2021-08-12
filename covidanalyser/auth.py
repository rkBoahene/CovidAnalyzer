import functools
from flask import (Blueprint, flash, g, redirect,render_template,request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from covidanalyser.db import get_db

# create blueprint named auth, with second arguement telling where its defined 
# and a url_prefix which is prepended to all routes associated with this blueprint
bp = Blueprint('auth', __name__, url_prefix='/auth')