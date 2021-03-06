from flask import Flask, json, request, jsonify
from sqlite3 import Connection as SQLiteConnection
from datetime import date, datetime

from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy
import linked_list
import hash_table

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
    #Whenever a user is deleted, any item in the Blog Post table that reference that ID will also be deleted 
    posts = db.relationship("BlogPost", cascade= "all, delete") #Relationship to another table called BlogPost


class BlogPost(db.Model):
    __tablename__ = "blog_post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(200))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


# Routes for the APi
@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = User(
        name = data["name"],
        email = data["email"],
        address = data["address"],
        phone = data["phone"]
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 200

@app.route("/user/descending_id", methods=["GET"])
def get_all_users_descending():
    users = User.query.all() #gives us users by id in ascending
    all_users_linked_list = linked_list.Linked_List()
    for user in users:
        #each time a user is added they are set as the head of the linked list so it reverses the order of the original query
        all_users_linked_list.insert_beginning(
            {
                'id' : user.id,
                'name' : user.name,
                "email" : user.email,
                "address" : user.address,
                "phone" : user.phone
            }
        )
    return jsonify(all_users_linked_list.to_array()), 200




@app.route("/user/ascending_id", methods=["GET"])
def get_all_users_ascending():
    users = User.query.all() #gives us users by id in ascending
    all_users_linked_list = linked_list.Linked_List()
    for user in users:
        #each time a user is added they are set as the head of the linked list so it reverses the order of the original query
        all_users_linked_list.insert_at_end(
            {
                'id' : user.id,
                'name' : user.name,
                "email" : user.email,
                "address" : user.address,
                "phone" : user.phone
            }
        )
    return jsonify(all_users_linked_list.to_array()), 200

@app.route("/user/<user_id>", methods=["GET"])
def get_one_user(user_id):
    users = User.query.all()

    all_users_linked_list = linked_list.Linked_List()

    for user in users:
        all_users_linked_list.insert_beginning(
            {
                'id' : user.id,
                'name' : user.name,
                "email" : user.email,
                "address" : user.address,
                "phone" : user.phone
            }
        )

    user = all_users_linked_list.get_user_by_id(user_id)    
    return jsonify(user), 200    

@app.route("/user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.filter_by(id = user_id).first()

    db.session.delete(user)
    db.session.commit()
    return jsonify({}), 200

@app.route("/blog_post/<user_id>", methods=["POST"])
def create_blog_post(user_id):
    data = request.get_json()

    user = User.query.filter_by(id = user_id).first()
    if not user:
        return jsonify({"message ": "user does not exist"}), 400
    
    hash_tb = hash_table.Hash_Table(10)

    hash_tb.add_key_value("title", data["title"])
    hash_tb.add_key_value("body", data["body"])
    hash_tb.add_key_value("date", now)
    hash_tb.add_key_value("user_id", user_id)

    print(hash_tb)

@app.route("/blog_post/<user_id>", methods=["GET"])
def get_all_blog_posts(user_id):
    pass

@app.route("/blog_post/<blog_post_id>", methods=["POST"])
def get_one_blog_post(blog_post_id):
    pass

@app.route("/blog_post/<blog_post_id>", methods=["DELETE"])
def delete_blog_post(blog_post_id):
    pass

if __name__ == "__main__":
    app.run(debug=True)
