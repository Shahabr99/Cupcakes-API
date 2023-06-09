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
     
     return render_template('home.html')


@app.route('/api/cupcakes')
def list_cupcakes():
    cupcakes = Cupcake.query.all()
    serialized_cupcake = [cupcake.serialize() for cupcake in cupcakes]
    return jsonify(cupcake = serialized_cupcake)


@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    serialized_cupcake = cupcake.serialize()
    return jsonify(cupcake=serialized_cupcake)


@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """Adding a new cupcake to the list and responding with json"""
    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json.get('image')

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image or None)

    db.session.add(new_cupcake)
    db.session.commit()
   
    response = jsonify(cupcake=new_cupcake.serialize())
   
    return (response, 201)

@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    """Update the data about a cupcake"""
    cupcake = Cupcake.query.get_or_404(id)

    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json['image']

    altered_cupcake = Cupcake(flavor=flavor, size = size, rating=rating, image=image or None)

    db.session.add(altered_cupcake)
    db.session.commit()

    response = jsonify(altered_cupcake.serialize())
    return response


@app.route('/api/cupcakes/<int:id>')
def delete_cupcake(id):
    """deleting a cupcake from database"""
    cupcake = Cupcake.query.get_or_404(id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message='Deleted')