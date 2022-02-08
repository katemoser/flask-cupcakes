from flask import Flask, jsonify, request
from models import db, connect_db, Cupcake

"""Flask app for Cupcakes"""
# FLASK_RUN_PORT=5001 flask run 

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)
db.create_all()


#CR: makes it easier on the reader to start with the route like app.get
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
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.route("/api/cupcakes", methods=["POST"])
def make_new_cupcake():
    """Make a new cupcake"""

    image = request.json.get("image") or None #CR: if the left is falsy, try the right

    new_cupcake = Cupcake(
        flavor=request.json["flavor"],
        size=request.json["size"],
        rating=request.json["rating"],
        image=image,
    )

    db.session.add(new_cupcake)
    db.session.commit()

    serialized_cupcake = new_cupcake.serialize()

    return (jsonify(cupcake=serialized_cupcake), 201)

@app.patch("/api/cupcakes/<int:cupcake_id>")
def update_cupcake(cupcake_id):
    """Update cupcake via cupcake_id passed to function
        returns JSON: {cupcake: {id, flavor, size, rating, image}}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    ## TODO: Fix the rating = 0 problem

    cupcake.flavor = request.json.get("flavor") or cupcake.flavor
    cupcake.size = request.json.get("size") or cupcake.size
    cupcake.rating = request.json.get("rating") or cupcake.rating
    cupcake.image = request.json.get("image") or cupcake.image

    db.session.commit()

    serialized = cupcake.serialize()
    return jsonify(cupcake=serialized)


@app.delete("/api/cupcakes/<int:cupcake_id>")
def delete_cupcake(cupcake_id):
    """Delete cupcake with the id passed in the URL.
        returns JSON: {deleted: [cupcake-id]}.
    """

    Cupcake.query.get_or_404(cupcake_id)
    Cupcake.query.filter_by(id=cupcake_id).delete()

    # db.session.delete(cupcake)

    db.session.commit()

    return jsonify(deleted=cupcake_id)
