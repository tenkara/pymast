from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func


app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/random")
def random():
    # cafes = db.session.query(Cafe).all()
    random_cafe = Cafe.query.order_by(func.random()).first()
    # print(random_cafe)
    # convert to dictionary
    dict_cafe = {}
    for key, value in random_cafe.__dict__.items():
        if not key.startswith("_sa_"):
            dict_cafe[key] = value
    print(random_cafe.__dict__.items())
    return jsonify(cafe=dict_cafe)

## HTTP GET - Read Record

## HTTP GET All - Read all Records
@app.route("/all")
def all():
    cafes = db.session.query(Cafe).all()
    # print(cafes)
    # convert to dictionary
    dict_cafes = []
    for cafe in cafes:
        dict_cafe = {}
        for key, value in cafe.__dict__.items():
            if not key.startswith("_sa_"):
                dict_cafe[key] = value
        dict_cafes.append(dict_cafe)
    return jsonify(cafes=dict_cafes)
    

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
