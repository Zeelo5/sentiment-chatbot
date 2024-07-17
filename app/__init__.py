# from flask import Flask

# app = Flask(__name__)
# app.config.from_object('config')

# from app import routes
 
# from flask import Flask
# from .routes import main
# from .suggestions import suggest

# # Initialize the app
# def create_app():
#     app = Flask(__name__)
#     app.config.from_pyfile('config.py')

#     # Register blueprints
#     app.register_blueprint(main)
#     app.register_blueprint(suggest)

#     return app



# from flask import Flask

# # Initialize the app
# def create_app():
#     app = Flask(__name__)
#     app.config.from_pyfile('config.py')

#     # Register blueprints
#     from .routes import main
#     from .suggestions import suggest
#     app.register_blueprint(main)
#     app.register_blueprint(suggest)

#     return app


# from flask import Flask
# from .routes import main  # Import routes after initializing app

# def create_app():
#     app = Flask(__name__)
#     app.config.from_pyfile('config.py')
#     app.register_blueprint(main)  # Register the routes blueprint
#     return app


from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='your-secret-key',
    )

    from .routes import suggest_bp
    app.register_blueprint(suggest_bp, url_prefix='/suggest')  # Register the Blueprint with the correct URL prefix

    return app
