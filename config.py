import sys
import os
import imports

from flask import Flask
from flask_mysqldb import MySQL
import json
app = Flask(__name__)
app.secret_key = "cedzkii123"  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
mysql = MySQL(app)
