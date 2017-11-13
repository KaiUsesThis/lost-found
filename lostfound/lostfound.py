from flask import Flask
from dbClient import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:opensesame@localhost/postgres'

# Blueprints
from public import public_routes
from users import user_routes 

app.register_blueprint(public_routes.mod)
app.register_blueprint(user_routes.mod, url_prefix='/users')

