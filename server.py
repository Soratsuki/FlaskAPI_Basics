from flask import Flask, request, jsonify
from sqlite3 import Connection as SQLiteConnection
from datetime import date, datetime

from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy

#app
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0

#Configure sqlite3 to enforce foreign key constraints 
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLiteConnection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

db =  SQLAlchemy(app)
now = datetime.now()

# DB Table Models:
class User(db.Model):
    """
    USer Table in class form that will be represented in the database..

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    posts = db.relationship("BlogPost") #Relationship to another table called BlogPost


class BlogPost(db.Model):
    __tablename__ = "blog_post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(200))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)