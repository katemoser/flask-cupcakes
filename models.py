"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cupcake(db.Model):
    """Cupcake"""

    __tablename__ = "cupcakes"
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    flavor = db.Column(db.Text, nullable = False)
    size = db.Column(db.Text, nullable = False)
    rating = db.Column(db.Integer, nullable = False)
    image = db.Column(db.Text, nullable = False, default="https://tinyurl.com/demo-cupcake")




    #TODO: Build a serializer