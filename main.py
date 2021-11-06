from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://root:root@db/main'

db = SQLAlchemy(app)

# building model
class Cinema(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    addess = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    movies = db.Column(db.Integer)
    snack = db.Column(db.String(200))
    capacity = db.Column(db.Integer)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(500))
    cast = db.Column(db.String(400))
    duration = db.Column(db.Integer)
    # timeslot = db.Column(db.String(100))
    # timeslotID = db.Column(db.Integer)

class Timeslots(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movieID = db.Column(db.Integer)
    cinemaID = db.Column(db.Integer)
    startTime = db.Column(db.String(100))
    endTime = db.Column(db.String(100))
    # availableSeat = db.Column(db.Integer)
    # bookedSeat = db.Column(db.Integer)

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timeSlotID = db.Column(db.Integer)
    typeTicket = db.Column(db.String(50))

class Seats(db.Model):
    id = id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cinemaID = db.Column(db.Integer)
    status = db.Column(db.String(50))



# re create new
# add second comments
# create the DB on demand
# @app.before_first_request
# def create_tables():
#     print("---------------------------------------")
#     db.create_all()
#     pro = Product(id=10, title="thwerwe", image="hhasga")
#     db.session.add(pro)
#     db.session.commit()



hhh = db.Table('product', db.metadata, autoload=True, autoload_with=db.engine)

@app.route('/')
def index():
    print("hello")

    # user1 = Product.query.all() 
    user1 = db.session.query(hhh).all()
    for _ in user1:
        print(_)

@app.route('/api')
def internal():
    print("api call")
    return {"message": "An id does not exist"}, 200




if __name__ == '__main__':
    
    app.run(debug=True, host='0.0.0.0')
