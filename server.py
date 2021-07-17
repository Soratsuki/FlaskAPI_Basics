from flask import Flask, request, jsonify
from sqlite3 import Connection as SQLiteConnection
from datetime import datetime

#app
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config["SQL_TRACK_MODIFICATIONS"] = 0

#models
