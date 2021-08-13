import functools
from flask import (Blueprint, flash, g, redirect,render_template,request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from covidanalyser.db import get_db

# create blueprint named auth, with second arguement telling where its defined 
# and a url_prefix which is prepended to all routes associated with this blueprint
bp = Blueprint('auth', __name__, url_prefix='/auth')

# create view to register users
@bp.route('/register', methods=('GET','POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # get database access
        db = get_db()
        error = None

        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = f'User {username} already exists'
        
        if error is None:
            db.execute(
            'INSERT INTO user(username, password) VALUES (?,?)', (username,generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))
        flash(error)
    return render_template('auth/register.html')
        

@bp.route('/login', methods=('POST','GET'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # get database access
        db = get_db()
        error = None

        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'User does not exist'
        elif not check_password_hash(user['password'], password):
            error = 'Password does not match'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        flash(error)

    return render_template('auth/login.html')


# @bp.before_app_request() registers a function that runs before the view function,
#  no matter what URL is requested. 
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


# to logout, just clear the session so that the load_logged_in_user()
# returns None for user when called
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


# a decorator to check if user is logged in,
#  I will use it when user tries to make any analysis
def login_required(view):
    functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view