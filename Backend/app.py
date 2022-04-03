from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
from sqlalchemy.orm import relationship
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/cs162'
db = SQLAlchemy(
    app,
    engine_options={'connect_args': {'connect_timeout': 1000}})
CORS(app)


class Agent(db.Model):

    __tablename__ = 'Agent_Table'

    agent_id = db.Column(db.Integer, primary_key=True)
    agent_firstName = db.Column(db.String(100), nullable=False)
    agent_lastName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phoneNumber = db.Column(db.BigInteger, nullable=False)
    AddressLine1 = db.Column(db.String(100), nullable=False)
    AddressLine2 = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __repr__(self):

        return self.agent_firstName

    def __init__(self, agent_firstName, agent_lastName, email, phoneNumber, AddressLine1, AddressLine2):

        self.agent_firstName = agent_firstName
        self.agent_lastName = agent_lastName
        self.email = email
        self.phoneNumber = phoneNumber
        self.AddressLine1 = AddressLine1
        self.AddressLine2 = AddressLine2


class Seller(db.Model):

    __tablename__ = 'Seller_Table'

    seller_id = db.Column(db.Integer, primary_key=True)
    seller_firstName = db.Column(db.String(100), nullable=False)
    seller_lastName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phoneNumber = db.Column(db.Integer, nullable=False)
    AddressLine1 = db.Column(db.String(100), nullable=False)
    AddressLine2 = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __repr__(self):

        return self.sellerfirstName

    def __init__(self, sellerfirstName, seller_lastName, email, phoneNumber, AddressLine1, AddressLine2):

        self.seller_lastName = seller_lastName
        self.sellerfirstName = sellerfirstName
        self.email = email
        self.phoneNumber = phoneNumber
        self.AddressLine1 = AddressLine1
        self.AddressLine2 = AddressLine2


class Houses(db.Model):
    __tablename__ = 'Houses_Table'

    house_id = db.Column(db.Integer, primary_key=True)
    seller_id = db.Column(
        db.Integer, db.ForeignKey('Seller_Table.seller_id'), nullable=False)
    agent_id = db.Column(
        db.Integer, db.ForeignKey('Agent_Table.agent_id'), nullable=False)
    office_id = db.Column(
        db.Integer, db.ForeignKey('Offices_Table.office_id'), nullable=False)
    zipCode = db.Column(db.Integer, nullable=False)
    AddressLine1 = db.Column(db.String(100), nullable=False)
    area_in_square_meter = db.Column(db.Integer, nullable=False)
    house_price = db.Column(db.Integer, nullable=False)
    date_of_listing = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __repr__(self):

        return self.AddressLine1

    def __init__(self, zipCode, AddressLine1, area_in_square_meter, house_price, date_of_listing):

        self.zipCode = zipCode
        self.AddressLine1 = AddressLine1
        self.area_in_square_meter = area_in_square_meter
        self.house_price = house_price
        self.date_of_listing = date_of_listing


class Offices(db.Model):

    __tablename__ = 'Offices_Table'

    office_id = db.Column(db.Integer, primary_key=True)
    office_name = db.Column(db.String(100), nullable=False)
    office_phoneNumber = db.Column(db.Integer, nullable=False)
    office_adressLine1 = db.Column(db.String(100), nullable=False)
    office_adressLine2 = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __repr__(self):

        return self.office_name

    def __init__(self, office_name, office_phoneNumber, office_adressLine1, office_adressLine2):

        self.office_name = office_name
        self.office_phoneNumber = office_phoneNumber
        self.office_adressLine1 = office_adressLine1
        self.office_adressLine2 = office_adressLine2


class Sales(db.Model):

    __tablename__ = 'Sales_Table'

    sales_id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(
        db.Integer, db.ForeignKey('Buyer_Table.buyer_id'), nullable=False)
    seller_id = db.Column(
        db.Integer, db.ForeignKey('Seller_Table.seller_id'), nullable=False)
    agent_id = db.Column(
        db.Integer, db.ForeignKey('Agent_Table.agent_id'), nullable=False)
    house_id = db.Column(
        db.Integer, db.ForeignKey('Houses_Table.house_id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    date_of_sale = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __repr__(self):

        return self.sales_id

    def __init__(self, price, date_of_sale):

        self.price = price
        self.date_of_sale = date_of_sale


class Buyer(db.Model):

    __tablename__ = 'Buyer_Table'

    buyer_id = db.Column(db.Integer, primary_key=True)
    buyer_firstName = db.Column(db.String(100), nullable=False)
    buyer_lastName = db.Column(db.String(100), nullable=False)
    buyer_phoneNumber = db.Column(db.String(100), nullable=False)
    buyer_email = db.Column(db.String(100), nullable=False)
    buyer_AddressLine1 = db.Column(db.String(100), nullable=False)
    buyer_AddressLine2 = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __repr__(self):

        return self.buyer_firstName

    def __init__(self, buyer_firstName, buyer_lastName, buyer_phoneNumber, buyer_email, buyer_AddressLine1, buyer_AddressLine2, ):

        self.buyer_firstName = buyer_firstName
        self.buyer_lastName = buyer_lastName
        self.buyer_phoneNumber = buyer_phoneNumber
        self.buyer_email = buyer_email
        self.buyer_AddressLine1 = buyer_AddressLine1
        self.buyer_AddressLine2 = buyer_AddressLine2


def format_event(event):

    return {

        "agent_id": event.agent_id,
        "created_at": event.created_at,
        "agent_firstName": event.agent_firstName,
        "agent_lastName": event.agent_lastName,
        "email": event.email,
        "phoneNumber": event.phoneNumber,
        "AddressLine1": event.AddressLine1,
        "AddressLine2": event.AddressLine2

    }


@app.route('/test', methods=['GET'])
def hello():
    if request.method == 'GET':
        return jsonify({"response": "IT IS WORKING, ABEN! CHILL BRO!"})


@app.route('/agent', methods=['POST'])
def create_event():
    if request.method == 'POST':
        agent_firstName = request.json['agent_firstName']
        agent_lastName = request.json['agent_lastName']
        email = request.json['email']
        phoneNumber = request.json['phoneNumber']
        AddressLine1 = request.json['AddressLine1']
        AddressLine2 = request.json['AddressLine2']

        event1 = Agent(agent_firstName, agent_lastName,  email,
                       phoneNumber, AddressLine1, AddressLine2)
        db.session.add(event1)

        db.session.commit()
        return format_event(event1)


@app.route('/agent',  methods=["GET"])
def get_events():

    events = Event.query.order_by(Event.id.asc()).all()
    event_list = []
    for event in events:
        event_list.append(format_event(event))

    return {'event': event_list}


@app.route('/agent/<agent_id>', methods=['GET'])
def get_event(id):

    event = Event.query.filter_by(id=id).one()
    formatted_event = format_event(event)
    return {'event': formatted_event}


@app.route('/agent/<agent_id>', methods=['DELETE'])
def delete_event(id):
    event = Event.query.filter_by(id=id).one()
    db.session.delete(event)
    db.session.commit()
    return 'Event is Deleted!'


@app.route('/agent/<agent_id>', methods=['PUT'])
def update_event(id):

    event = Event.query.filter_by(id=id)
    description = request.json['description']
    event.update(dict(description=description, created_at=datetime.utcnow()))
    db.session.commit()
    return {'event': format_event(event.one())}


if __name__ == '__main__':
    app.run(debug=True, port=7070)
