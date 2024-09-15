from flask import Flask
from extensions import db
from routes import stock_routes, user_routes
from config import Config
from models import User
from flask_migrate import Migrate
from flask_login import LoginManager

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))  # Retrieve the user from the database using the user_id

    # Redirect to the login page if the user is not authenticated
    login_manager.login_view = 'user_routes.login'

    with app.app_context():
        db.create_all()

    app.register_blueprint(stock_routes)
    app.register_blueprint(user_routes)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
