from flask import (Blueprint, flash, g,redirect,render_template,request,url_for)
from flask.templating import render_template_string
from werkzeug.exceptions import abort
from covidanalyser.auth import login_required
from covidanalyser.db import get_db
import folium

bp = Blueprint('analyzer', __name__)
# url_prefix='/analyzer'

def call_folium_map():
    start_coords = (46.9540700, 142.7360300)
    folium_map = folium.Map(location=start_coords, zoom_start=14,width='60%',height='60%')
    # return folium_map._repr_html_()
    # return render_template(folium_map._repr_html_())
    return render_template_string(source=folium_map._repr_html_())


@bp.route('/')
def index():
    map = call_folium_map()
    return render_template('analyzer/index.html',map=map)
    # return render_template_string(source=map)

@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('analyzer/dashboard.html')