from flask import Flask, jsonify, request
from models import db, connect_db, Cupcake

"""Flask app for Cupcakes"""

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)
db.create_all()


@app.route("/api/cupcakes", methods=['GET'])
def display_cupakes():
    """ Get data about all cupcakes"""

    cupcakes = Cupcake.query.all()
    serialized = [cupcake.serialize() for cupcake in cupcakes]

    return jsonify(cupcakes=serialized)


@app.route("/api/cupcakes/<int:cupcake_id>", methods=['GET'])
def display_cupake(cupcake_id):
    """ Get data about a single cupcake."""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    return jsonify(cupcake=cupcake)


@app.route("api/cupcakes", methods=["POST"])
def make_new_cupcake():
    """Make a new cupcake"""

    new_cupcake = Cupcake(
        id=request.json.id,
        flavor=request.json.flavor,
        size=request.json.size,
        rating=request.json.rating,
        image=request.json.image,
    )

    db.session.add(new_cupcake)
    db.session.commit()

    serialized_cupcake = new_cupcake.serialize()

    return (jsonify(cupcake=serialized_cupcake), 201)
