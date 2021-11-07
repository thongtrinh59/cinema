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
from sqlalchemy.orm import sessionmaker

import json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://root:root@db/main'

db = SQLAlchemy(app)
engine = create_engine('postgresql://root:root@db/main')
Session = sessionmaker(bind = engine)
session = Session()

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

# Get available cinemas
@app.route('/cinema')
def get_avai_cinema():
    parser = reqparse.RequestParser()
    parser.add_argument('status', type=str,  required=False)
    parser.add_argument('name', type=str,  required=False)
    parser.add_argument('movie_title', type=str,  required=False)
    
    args = parser.parse_args()
    print(args)

    if args['status'] is not None:
        list_of_avai_cinema = []

        with engine.connect() as con:
            q_str = "SELECT * FROM cinema;"
            rs = con.execute(q_str)
            for _ in rs:
                dict_result = {
                    "id": _.id,
                    "name": _.name,
                    "address": _.address,
                    "phone": _.phone,
                    "snack": _.snack,
                    "capacity": _.capacity
                }
                list_of_avai_cinema.append(dict_result)

        # avai_cinema = Cinema.query.all()
        # for _ in avai_cinema:
        #     dict_result = {
        #         "id": _.id,
        #         "name": _.name,
        #         "address": _.address,
        #         "phone": _.phone,
        #         "snack": _.snack,
        #         "capacity": _.capacity
        #     }
        #     list_of_avai_cinema.append(dict_result)

        return {'return': list_of_avai_cinema}, 200

    if args['name'] is not None:
        list_cinema_by_name = []
        # for _ in args['name']:
        cinema_by_name = Cinema.query.filter_by(name=args['name']).first()
        dict_result = {
            "id": cinema_by_name.id,
            "name": cinema_by_name.name,
            "address": cinema_by_name.address,
            "phone": cinema_by_name.phone,
            "snack": cinema_by_name.snack,
            "capacity": cinema_by_name.capacity
        }
        list_cinema_by_name.append(dict_result)
        return {'return': list_cinema_by_name}, 200

    if args['movie_title'] is not None:
        print("OKKKKKKKKKK")
        result = []
        with engine.connect() as con:
            q_str = "SELECT DISTINCT(c.name) FROM movie as m,  \
                timeslots as t, cinema as c WHERE m.id = t.mid AND \
                c.id = t.cid AND LOWER(m.title) = LOWER('{}');".format(args['movie_title'])

            rs = con.execute(q_str)
            for row in rs:
                result.append(row.name)
        print(result)
        return {'result': result}, 200
        
        



# # Get available cinemas
# @app.route('/cinema')
# def get_avai_cinema():
#     parser = reqparse.RequestParser()
#     parser.add_argument('status', type=str,  required=False, help='Status cannot be blank')
    
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

    
    
#     return {'return': list_of_result}, 200







if __name__ == '__main__':
    
    app.run(debug=True, host='0.0.0.0')
