from flask import (Blueprint, flash, g,redirect,render_template,request,url_for)
from werkzeug.exceptions import abort
from covidanalyser.auth import login_required
from covidanalyser.db import get_db

bp = Blueprint('analyzer', __name__)