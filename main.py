from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Resource, Api
from flask_restx import fields
from flask_restx import inputs
from flask_restx import reqparse
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect
import json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://root:root@db/main'

db = SQLAlchemy(app)
engine = create_engine('postgresql://root:root@db/main')

# building model
class Cinema(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    snack = db.Column(db.String(200))
    capacity = db.Column(db.Integer)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(500))
    actors = db.Column(db.String(500))
    duration = db.Column(db.Integer)

class Timeslots(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mid = db.Column(db.Integer)
    cid = db.Column(db.Integer)
    starttime = db.Column(db.String(100))
    endtime = db.Column(db.String(100))

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timeslotid = db.Column(db.Integer)
    typeticket = db.Column(db.String(50))
    seat = db.Column(db.Integer)

# # Get available cinemas
# @app.route('/cinema')
# def get_avai_cinema():
#     parser = reqparse.RequestParser()
#     parser.add_argument('status', type=str,  required=True, help='Status cannot be blank')
    
#     args = parser.parse_args()
#     print(args)
#     list_of_result = []

#     if args['status'] == 'available':
#         avai_cinema = Cinema.query.all()
#         for _ in avai_cinema:
#             print(_.name)
#             dict_result = {
#                 "id": _.id,
#                 "name": _.name,
#                 "address": _.address,
#                 "phone": _.phone,
#                 "snack": _.snack,
#                 "capacity": _.capacity
#             }
            
#             # dict_result = json.dumps(dict_result)
#             # print(dict_result)
#             list_of_result.append(dict_result)

#     # with engine.connect() as con:

#     #     rs = con.execute('SELECT * FROM cinema;')

#     #     for row in rs:
#     #         print(row.id)
    
#     # list_of_result = json.dumps(list_of_result)
    
    
#     return {'return': list_of_result}, 200


# Get cinema information
@app.route('/cinema')
def get_info_cinema():
    parser = reqparse.RequestParser()
    parser.add_argument('name', action='append', type=str,  required=True, help='Name cannot be blank')
    
    args = parser.parse_args()
    print(args)

    list_of_result = []
    # for name in args['name']:
    #     info_cinema = Cinema.query.filter_by(name=name).first()
    #     dict_result = {
    #         "id": info_cinema.id,
    #         "name": info_cinema.name,
    #         "address": info_cinema.address,
    #         "phone": info_cinema.phone,
    #         "snack": info_cinema.snack,
    #         "capacity": info_cinema.capacity
    #     }
    #     list_of_result.append(dict_result)

    return {'result': list_of_result}, 200



# hhh = db.Table('product', db.metadata, autoload=True, autoload_with=db.engine)

@app.route('/')
def index():
    print("hello")

    # user1 = Product.query.all() 
    # user1 = db.session.query(hhh).all()
    # for _ in user1:
    #     print(_)

@app.route('/api')
def internal():
    print("api call")
    return {"message": "An id does not exist"}, 200




if __name__ == '__main__':
    
    app.run(debug=True, host='0.0.0.0')
