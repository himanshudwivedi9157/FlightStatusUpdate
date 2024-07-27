from flask import Blueprint, render_template, jsonify, request, current_app as app

views = Blueprint('views', __name__)

@views.route('/flights', methods=['GET'])
def get_flights():
    flights = app.mongo.db.flights.find()
    return jsonify([flight for flight in flights])

@views.route('/flights/<flight_id>', methods=['GET'])
def get_flight(flight_id):
    flight = app.mongo.db.flights.find_one_or_404({'_id': flight_id})
    return jsonify(flight)

@views.route('/flights', methods=['POST'])
def add_flight():
    data = request.get_json()
    result = app.mongo.db.flights.insert_one(data)
    return jsonify({'_id': str(result.inserted_id)}), 201

@views.route('/flights/<flight_id>', methods=['PUT'])
def update_flight(flight_id):
    data = request.get_json()
    app.mongo.db.flights.update_one({'_id': flight_id}, {'$set': data})
    return jsonify({'_id': flight_id})

@views.route('/flights/<flight_id>', methods=['DELETE'])
def delete_flight(flight_id):
    app.mongo.db.flights.delete_one({'_id': flight_id})
    return '', 204

@views.route('/', methods=['GET'])
def home():
    return render_template('index.html')
