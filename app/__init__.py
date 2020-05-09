from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
mysql.init_app(app)

from app.admin.routes import bp
from app.users.routes import bp

app.register_blueprint(admin.routes.bp)
app.register_blueprint(users.routes.bp, url_prefix='/user')