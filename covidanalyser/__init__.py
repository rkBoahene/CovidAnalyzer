import os
from flask import Flask
from flask.templating import render_template

def create_app(test_config=None):
    # creating and configuring the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path,'covidanalyser.sqlite')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # import and initialize db in main app
    from . import db
    db.init_app(app)

    # register auth blueprint to app
    from . import auth
    app.register_blueprint(auth.bp)

    # register analyzer blueprint to app
    from . import analyzer
    app.register_blueprint(analyzer.bp)
    # associate '/' to endpoint name == index 
    app.add_url_rule('/', endpoint='index')














    # a simple page saying hello
    @app.route('/hello')
    def welcome():
        return 'Hello, World!'

    return app 
