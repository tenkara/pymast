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

## HTTP GET Search - Read Record
@app.route("/search", methods=["GET"])
def search():
    query_location = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    if cafe:
        return jsonify(cafe=cafe)
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})




## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH", "GET"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})


## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    if request.args.get("api-key") == "TopSecretAPIKey":
        cafe = Cafe.query.get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe."})
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})
    else:
        return jsonify(error={"Forbidden": "Sorry, you're not allowed to delete a cafe."})
        
if __name__ == '__main__':
    app.run(debug=True)
