import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    # function added to serialize the database

    def add_to_dict(self):
        # approach 1 - for loop to add to dictionary based on the db items
        # loop the columns in the db
        # dictionary = {}
        # for column in self.__table__.columns:
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary

        # approach 2 - dictionary comprehension method
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record - adding the get a random cafe route
@app.route("/random")
def get_random_cafee():
    # initialize db to read all items > render all items > extract random item
    db_items = db.session.execute(db.select(Cafe))
    all_items = db_items.scalars().all()
    random_item = random.choice(all_items)

    # #---> approach 1 --> call all items defined in the db class <-----#
    # return jsonify(cafe={
    #     "id": random_item.id,
    #     "name": random_item.name,
    #     "map_url": random_item.map_url,
    #     "img_url": random_item.img_url,
    #     "location": random_item.location,
    #     "seats": random_item.seats,
    #     "has_toilet": random_item.has_toilet,
    #     "has_wifi": random_item.has_wifi,
    #     "has_sockets": random_item.has_sockets,
    #     "can_take_calls": random_item.can_take_calls,
    #     "coffe_price": random_item.coffe_price
    # })

    # #---> approach 2 --> serialising our database row Object to JSON is by first converting it to a dictionary and
    # then using jsonify() to convert the dictionary (which is very similar in structure to JSON) to a JSON.
    #  this is done when declaring the Cafe Class and adapting the call made in the random route <-----#
    return jsonify(cafe=random_item.add_to_dict())


# route to get all items from the database
@app.route("/all")
def get_all_items():
    # initialize db to read all items
    db_items = db.session.execute(db.select(Cafe))
    all_items = db_items.scalars().all()
    # return using list comprehension
    return jsonify(cafes=[cafe.add_to_dict() for cafe in all_items])


# route to search for a specific item in the db
@app.route("/search")
def get_location():
    # get the location parameter
    query_location = request.args.get("location")
    # initialize db to read all items
    db_items = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    all_items = db_items.scalars().all()
    # if statement to pull by search "?"
    if all_items:
        return jsonify(cafes=[cafe.add_to_dict() for cafe in all_items])
    else:
        return jsonify(error={"Not found": "Sorry, location not yet in the db"}), 404


# HTTP POST - Create Record -> testable with Postman - webpage returns a method not allowed page
# add rout for posting a new item in the API
@app.route("/add", methods=["POST"])
def add_item():
    new_item = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record -> Postman required to make a request  to update price
# update using patch - refer to notes.txt for differences between put and patch
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


# HTTP DELETE - Delete Record - > Postman required to make a request  to delete the item
# route to delete using delete method. - url access returns method not allowed in browser
@app.route("/delete/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    # get and pass the key
    if api_key == "TopSecretAPIKey":
        cafe = db.get_or_404(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
