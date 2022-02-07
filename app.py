from flask import Flask
from models import db, connect_db, Cupcake

"""Flask app for Cupcakes"""

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)
db.create_all()


@app.route("/api/cupcakes", methods=['GET','POST'])
def display_cupakes():
    """ Get data about all cupcakes"""

    cupcakes = Cupcake.query.all()
    "serialize here"



    return jsonify("JSON THING")