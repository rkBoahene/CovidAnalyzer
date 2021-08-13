from flask import (Blueprint, flash, g,redirect,render_template,request,url_for)
from werkzeug.exceptions import abort
from covidanalyser.auth import login_required
from covidanalyser.db import get_db

bp = Blueprint('analyzer', __name__)
# url_prefix='/analyzer'

@bp.route('/')
def index():
    return render_template('analyzer/index.html')

@bp.route('/dashboard')
def dashboard():
    return render_template('analyzer/dashboard.html')