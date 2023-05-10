from flask import Flask, render_template, jsonify, request
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SECRET_KEY'] = 'oh-so-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


connect_db(app)

@app.route('/')
def show_cupcakes():
     cupcakes = Cupcake.query.all()
     return render_template('home.html', cupcakes=cupcakes)


@app.route('/api/cupcakes')
def get_cupcakes():
    cupcakes = Cupcake.query.all()
    serialized_cupcake = [cupcake.serialize() for cupcake in cupcakes]
    return jsonify(cupcake = serialized_cupcake)


@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    serialized_cupcake = cupcake.serialize()
    return jsonify(cupcake=serialized_cupcake)


@app.route('/api/cupcakes', methods=["POST"])
def add_cupcake():
    """Adding a new cupcake to the list and responding with json"""
    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json.get('image')

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image or None)

    db.session.add(new_cupcake)
    db.session.commit()
   
    response = jsonify(cupcake=new_cupcake.serialize())
   
    response.headers['Content-Type'] = 'application/json'
    return (response, 201)