from flask import Flask, render_template
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
def show_cupcakes():
    cupcakes = Cupcake.query.all()
    return jsonify(cupcake.serialize())