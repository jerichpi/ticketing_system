from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = '4772734a4be182cf756be03df1804558'
mysql = MySQL()
mysql.init_app(app)

from app.admin.routes import bp
from app.users.routes import bp

app.register_blueprint(admin.routes.bp)
app.register_blueprint(users.routes.bp, url_prefix='/user')