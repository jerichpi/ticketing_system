from . import app, mysql
from dotenv import load_dotenv
import os
from os.path import join, dirname

dotenv_path = join(dirname(__file__), 'dev.env')  # Path to .env file
load_dotenv(dotenv_path)

app.config['MYSQL_DATABASE_HOST'] = "127.0.0.1"
app.config['MYSQL_DATABASE_PORT'] = "3306"
app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = "admiS11"
app.config['MYSQL_DATABASE_DB'] = "ticket_db"
app.config['MYSQL_DATABASE_CHARSET'] = "utf-8"