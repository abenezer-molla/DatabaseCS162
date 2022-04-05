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

    __tablename__ = 'AgentTable'

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


# complete CRUD for the Agent Table that can be accessed via an api (you can use platforms such as postman)


def format_event(event):
    '''
    for the agent table
    '''

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

    events = Agent.query.order_by(Agent.agent_id.asc()).all()
    event_list = []
    for event in events:
        event_list.append(format_event(event))

    return {'event': event_list}


@app.route('/agent/<agent_id>', methods=['GET'])
def get_event(agent_id):

    event = Agent.query.filter_by(agent_id=agent_id).one()
    formatted_event = format_event(event)
    return {'event': formatted_event}


@app.route('/agent/<agent_id>', methods=['DELETE'])
def delete_event(agent_id):
    event = Agent.query.filter_by(agent_id=agent_id).one()
    db.session.delete(event)
    db.session.commit()
    return 'Event is Deleted!'


@app.route('/agent/<agent_id>', methods=['PUT'])
def update_event(agent_id):

    event = Agent.query.filter_by(agent_id=agent_id)

    try:
        agent_firstName = request.json['agent_firstName']
        event.update(dict(agent_firstName=agent_firstName,
                          created_at=datetime.utcnow()))

    except:
        pass

    try:
        agent_lastName = request.json['agent_lastName']
        event.update(dict(agent_lastName=agent_lastName,
                          created_at=datetime.utcnow()))

    except:
        pass

    try:
        email = request.json['email']
        event.update(dict(email=email,
                          created_at=datetime.utcnow()))

    except:
        pass

    try:
        phoneNumber = request.json['phoneNumber']
        event.update(dict(phoneNumber=phoneNumber,
                          created_at=datetime.utcnow()))

    except:
        pass

    try:
        AddressLine1 = request.json['AddressLine1']
        event.update(dict(AddressLine1=AddressLine1,
                          created_at=datetime.utcnow()))

    except:
        pass

    try:
        AddressLine2 = request.json['AddressLine2']
        event.update(dict(AddressLine2=AddressLine2,
                          created_at=datetime.utcnow()))

    except:
        pass

    db.session.commit()
    print("event is =", event)
    return {'event': format_event(event.one())}


class Seller(db.Model):

    __tablename__ = 'SellerTable'

    seller_id = db.Column(db.Integer, primary_key=True)
    seller_firstName = db.Column(db.String(100), nullable=False)
    seller_lastName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phoneNumber = db.Column(db.BigInteger, nullable=False)
    AddressLine1 = db.Column(db.String(100), nullable=False)
    AddressLine2 = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __repr__(self):

        return self.seller_firstName

    def __init__(self, seller_firstName, seller_lastName, email, phoneNumber, AddressLine1, AddressLine2):

        self.seller_lastName = seller_lastName
        self.seller_firstName = seller_firstName
        self.email = email
        self.phoneNumber = phoneNumber
        self.AddressLine1 = AddressLine1
        self.AddressLine2 = AddressLine2


def format_event_seller(event):
    '''
    for the Seller table
    '''

    return {

        "seller_id": event.seller_id,
        "created_at": event.created_at,
        "seller_lastName": event.seller_lastName,
        "seller_firstName": event.seller_firstName,
        "email": event.email,
        "phoneNumber": event.phoneNumber,
        "AddressLine1": event.AddressLine1,
        "AddressLine2": event.AddressLine2

    }


@app.route('/seller', methods=['POST'])
def create_event2():
    if request.method == 'POST':
        seller_firstName = request.json['seller_firstName']
        seller_lastName = request.json['seller_lastName']
        email = request.json['email']
        phoneNumber = request.json['phoneNumber']
        AddressLine1 = request.json['AddressLine1']
        AddressLine2 = request.json['AddressLine2']

        event1 = Seller(seller_firstName, seller_lastName,  email,
                        phoneNumber, AddressLine1, AddressLine2)
        db.session.add(event1)

        db.session.commit()
        return format_event_seller(event1)


@app.route('/seller',  methods=["GET"])
def get_events2():

    events = Seller.query.order_by(Seller.seller_id.asc()).all()
    event_list = []
    for event in events:
        event_list.append(format_event_seller(event))

    return {'event': event_list}


@app.route('/seller/<seller_id>', methods=['GET'])
def get_event2(seller_id):

    event = Seller.query.filter_by(seller_id=seller_id).one()
    formatted_event = format_event_seller(event)
    return {'event': formatted_event}


@app.route('/seller/<seller_id>', methods=['DELETE'])
def delete_event2(seller_id):
    event = Seller.query.filter_by(seller_id=seller_id).one()
    db.session.delete(event)
    db.session.commit()
    return 'Event is Deleted!'


@app.route('/seller/<seller_id>', methods=['PUT'])
def update_event2(seller_id):

    event = Seller.query.filter_by(seller_id=seller_id)

    try:
        seller_firstName = request.json['seller_firstName']
        event.update(dict(seller_firstName=seller_firstName,
                          created_at=datetime.utcnow()))

    except:
        pass

    try:
        agent_lastName = request.json['agent_lastName']
        event.update(dict(seller_lastName=agent_lastName,
                          created_at=datetime.utcnow()))

    except:
        pass

    try:
        email = request.json['email']
        event.update(dict(email=email,
                          created_at=datetime.utcnow()))

    except:
        pass

    try:
        phoneNumber = request.json['phoneNumber']
        event.update(dict(phoneNumber=phoneNumber,
                          created_at=datetime.utcnow()))

    except:
        pass

    try:
        AddressLine1 = request.json['AddressLine1']
        event.update(dict(AddressLine1=AddressLine1,
                          created_at=datetime.utcnow()))

    except:
        pass

    try:
        AddressLine2 = request.json['AddressLine2']
        event.update(dict(AddressLine2=AddressLine2,
                          created_at=datetime.utcnow()))

    except:
        pass

    db.session.commit()
    print("event is =", event)
    return {'event': format_event_seller(event.one())}


class Houses(db.Model):
    __tablename__ = 'HousesTable_'

    house_id = db.Column(db.Integer, primary_key=True)
    seller_id = db.ForeignKey('SellerTable.seller_id')
    agent_id = db.ForeignKey('AgentTable.agent_id')
    office_id = db.ForeignKey('OfficesTable.office_id')
    zipCode = db.Column(db.Integer, nullable=False)
    AddressLine1 = db.Column(db.String(100), nullable=False)
    area_in_square_meter = db.Column(db.BigInteger, nullable=False)
    house_price = db.Column(db.BigInteger, nullable=False)
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


# Methods for the HouseTable will be below


def format_event_houses(event):
    '''
    for the Houses table
    '''

    return {

        "house_id": event.house_id,
        "created_at": event.created_at,
        "zipCode": event.zipCode,
        "area_in_square_meter": event.area_in_square_meter,
        "house_price": event.house_price,
        "date_of_listing": event.date_of_listing,
        "AddressLine1": event.AddressLine1,

    }


@app.route('/houses', methods=['POST'])
def create_event3():
    if request.method == 'POST':
        zipCode = request.json['zipCode']
        area_in_square_meter = request.json['area_in_square_meter']
        house_price = request.json['house_price']
        AddressLine1 = request.json['AddressLine1']
        date_of_listing = request.json['date_of_listing']

        event1 = Houses(zipCode, AddressLine1,
                        area_in_square_meter, house_price, date_of_listing)
        db.session.add(event1)

        db.session.commit()
        return format_event_houses(event1)


@app.route('/houses',  methods=["GET"])
def get_events3():

    events = Houses.query.order_by(Houses.house_id.asc()).all()
    event_list = []
    for event in events:
        event_list.append(format_event_houses(event))

    return {'event': event_list}


@app.route('/houses/<house_id>', methods=['GET'])
def get_event3(house_id):

    event = Houses.query.filter_by(house_id=house_id).one()
    formatted_event = format_event_houses(event)
    return {'event': formatted_event}


@app.route('/houses/<house_id>', methods=['DELETE'])
def delete_event3(house_id):
    event = Houses.query.filter_by(house_id=house_id).one()
    db.session.delete(event)
    db.session.commit()
    return 'Event is Deleted!'


@app.route('/houses/<house_id>', methods=['PUT'])
def update_event3(house_id):

    event = Houses.query.filter_by(house_id=house_id)

    try:
        zipCode = request.json['zipCode']
        event.update(dict(zipCode=zipCode,
                          created_at=datetime.utcnow()))

    except:
        pass

    try:
        area_in_square_meter = request.json['area_in_square_meter']
        event.update(dict(area_in_square_meter=area_in_square_meter,
                          created_at=datetime.utcnow()))

    except:
        pass

    try:
        house_price = request.json['house_price']
        event.update(dict(house_price=house_price,
                          created_at=datetime.utcnow()))

    except:
        pass

    try:
        date_of_listing = request.json['date_of_listing']
        event.update(dict(date_of_listing=date_of_listing,
                          created_at=datetime.utcnow()))

    except:
        pass

    try:
        AddressLine1 = request.json['AddressLine1']
        event.update(dict(AddressLine1=AddressLine1,
                          created_at=datetime.utcnow()))

    except:
        pass

    db.session.commit()
    print("event is =", event)
    return {'event': format_event_houses(event.one())}


class Offices(db.Model):

    __tablename__ = 'OfficesTable'

    office_id = db.Column(db.Integer, primary_key=True)
    office_name = db.Column(db.String(100), nullable=False)
    office_phoneNumber = db.Column(db.BigInteger, nullable=False)
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


# CRUD methods for the Offices Table


def format_event_offices(event):
    '''
    for the Offices table
    '''

    return {

        "office_id": event.office_id,
        "created_at": event.created_at,
        "office_name": event.office_name,
        "office_phoneNumber": event.office_phoneNumber,
        "office_adressLine1": event.office_adressLine1,
        "office_adressLine2": event.office_adressLine2,

    }


@app.route('/offices', methods=['POST'])
def create_event4():
    if request.method == 'POST':
        office_name = request.json['office_name']
        office_phoneNumber = request.json['office_phoneNumber']
        office_adressLine1 = request.json['office_adressLine1']
        office_adressLine2 = request.json['office_adressLine2']

        event1 = Offices(office_name, office_phoneNumber,
                         office_adressLine1, office_adressLine2)
        db.session.add(event1)

        db.session.commit()
        return format_event_offices(event1)


@app.route('/offices',  methods=["GET"])
def get_events4():

    events = Offices.query.order_by(Offices.office_id.asc()).all()
    event_list = []
    for event in events:
        event_list.append(format_event_offices(event))

    return {'event': event_list}


@app.route('/offices/<office_id>', methods=['GET'])
def get_event4(office_id):

    event = Offices.query.filter_by(office_id=office_id).one()
    formatted_event = format_event_offices(event)
    return {'event': formatted_event}


@app.route('/offices/<office_id>', methods=['DELETE'])
def delete_event4(office_id):
    event = Offices.query.filter_by(office_id=office_id).one()
    db.session.delete(event)
    db.session.commit()
    return 'Event is Deleted!'


@app.route('/offices/<office_id>', methods=['PUT'])
def update_event4(office_id):

    event = Offices.query.filter_by(office_id=office_id)

    try:
        office_name = request.json['office_name']
        event.update(dict(office_name=office_name,
                          created_at=datetime.utcnow()))

    except:
        pass

    try:
        office_phoneNumber = request.json['office_phoneNumber']
        event.update(dict(office_phoneNumber=office_phoneNumber,
                          created_at=datetime.utcnow()))

    except:
        pass

    try:
        office_adressLine1 = request.json['office_adressLine1']
        event.update(dict(office_adressLine1=office_adressLine1,
                          created_at=datetime.utcnow()))

    except:
        pass

    try:
        office_adressLine2 = request.json['office_adressLine2']
        event.update(dict(office_adressLine2=office_adressLine2,
                          created_at=datetime.utcnow()))

    except:
        pass

    db.session.commit()
    print("event is =", event)
    return {'event': format_event_offices(event.one())}


class Sales(db.Model):

    __tablename__ = 'SalesTable_'

    sales_id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.ForeignKey('BuyerTable.buyer_id')
    seller_id = db.ForeignKey('SellerTable.seller_id')
    agent_id = db.ForeignKey('AgentTable.agent_id')
    house_id = db.ForeignKey('HousesTable_.house_id')
    price = db.Column(db.BigInteger, nullable=False)
    date_of_sale = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __repr__(self):

        return self.sales_id

    def __init__(self, price, date_of_sale):

        self.price = price
        self.date_of_sale = date_of_sale


# CRUD methods for Sales Table

def format_event_sales(event):
    '''
    for the Offices table
    '''

    return {

        "sales_id": event.sales_id,
        "price": event.price,
        "date_of_sale": event.date_of_sale

    }


@app.route('/sales', methods=['POST'])
def create_event5():
    if request.method == 'POST':

        price = request.json['price']
        date_of_sale = request.json['date_of_sale']

        event1 = Sales(price, date_of_sale)
        db.session.add(event1)
        db.session.commit()
        return format_event_sales(event1)


@app.route('/sales',  methods=["GET"])
def get_events5():

    events = Sales.query.order_by(Sales.sales_id.asc()).all()
    event_list = []
    for event in events:
        event_list.append(format_event_sales(event))

    return {'event': event_list}


@app.route('/sales/<sales_id>', methods=['GET'])
def get_event5(sales_id):

    event = Sales.query.filter_by(sales_id=sales_id).one()
    formatted_event = format_event_sales(event)
    return {'event': formatted_event}


@app.route('/sales/<sales_id>', methods=['DELETE'])
def delete_event5(sales_id):
    event = Sales.query.filter_by(sales_id=sales_id).one()
    db.session.delete(event)
    db.session.commit()
    return 'Event is Deleted!'


@app.route('/sales/<sales_id>', methods=['PUT'])
def update_event5(sales_id):

    event = Sales.query.filter_by(sales_id=sales_id)

    try:
        date_of_sale = request.json['date_of_sale']
        event.update(dict(date_of_sale=date_of_sale,
                          created_at=datetime.utcnow()))

    except:
        pass

    try:
        price = request.json['price']
        event.update(dict(price=price,
                          created_at=datetime.utcnow()))

    except:
        pass

    db.session.commit()
    print("event is =", event)
    return {'event': format_event_sales(event.one())}


class Buyer(db.Model):

    __tablename__ = 'BuyerTable'

    buyer_id = db.Column(db.Integer, primary_key=True)
    buyer_firstName = db.Column(db.String(100), nullable=False)
    buyer_lastName = db.Column(db.String(100), nullable=False)
    buyer_phoneNumber = db.Column(db.BigInteger, nullable=False)
    buyer_email = db.Column(db.String(100), nullable=False)
    buyer_AddressLine1 = db.Column(db.String(100), nullable=False)
    buyer_AddressLine2 = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __repr__(self):

        return self.buyer_firstName

    def __init__(self, buyer_firstName, buyer_lastName, buyer_phoneNumber, buyer_email, buyer_AddressLine1, buyer_AddressLine2):

        self.buyer_firstName = buyer_firstName
        self.buyer_lastName = buyer_lastName
        self.buyer_phoneNumber = buyer_phoneNumber
        self.buyer_email = buyer_email
        self.buyer_AddressLine1 = buyer_AddressLine1
        self.buyer_AddressLine2 = buyer_AddressLine2


# CRUD methods for Buyer Table

def format_event_buyer(event):
    '''
    for the Buyer table
    '''

    return {

        "buyer_id": event.buyer_id,
        "buyer_firstName": event.buyer_firstName,
        "buyer_lastName": event.buyer_lastName,
        "buyer_phoneNumber": event.buyer_phoneNumber,
        "buyer_email": event.buyer_email,
        "buyer_AddressLine1": event.buyer_AddressLine1,
        "buyer_AddressLine2": event.buyer_AddressLine2
    }


@app.route('/buyer', methods=['POST'])
def create_event6():
    if request.method == 'POST':

        buyer_firstName = request.json['buyer_firstName']
        buyer_lastName = request.json['buyer_lastName']
        buyer_phoneNumber = request.json['buyer_phoneNumber']
        buyer_email = request.json['buyer_email']
        buyer_AddressLine1 = request.json['buyer_AddressLine1']
        buyer_AddressLine2 = request.json['buyer_AddressLine2']

        event1 = Buyer(buyer_firstName, buyer_lastName, buyer_phoneNumber,
                       buyer_email, buyer_AddressLine1, buyer_AddressLine2)
        db.session.add(event1)
        db.session.commit()
        return format_event_buyer(event1)


@app.route('/buyer',  methods=["GET"])
def get_events6():

    events = Buyer.query.order_by(Buyer.buyer_id.asc()).all()
    event_list = []
    for event in events:
        event_list.append(format_event_buyer(event))

    return {'event': event_list}


@app.route('/buyer/<buyer_id>', methods=['GET'])
def get_event6(buyer_id):

    event = Buyer.query.filter_by(buyer_id=buyer_id).one()
    formatted_event = format_event_buyer(event)
    return {'event': formatted_event}


@app.route('/buyer/<buyer_id>', methods=['DELETE'])
def delete_event6(buyer_id):
    event = Buyer.query.filter_by(buyer_id=buyer_id).one()
    db.session.delete(event)
    db.session.commit()
    return 'Event is Deleted!'


@app.route('/buyer/<buyer_id>', methods=['PUT'])
def update_event6(buyer_id):

    event = Buyer.query.filter_by(buyer_id=buyer_id)

    try:
        buyer_firstName = request.json['buyer_firstName']
        event.update(dict(buyer_firstName=buyer_firstName,
                          created_at=datetime.utcnow()))

    except:
        pass

    try:
        buyer_lastName = request.json['buyer_lastName']
        event.update(dict(buyer_lastName=buyer_lastName,
                          created_at=datetime.utcnow()))

    except:
        pass

    try:
        buyer_phoneNumber = request.json['buyer_phoneNumber']
        event.update(dict(buyer_phoneNumber=buyer_phoneNumber,
                          created_at=datetime.utcnow()))

    except:
        pass

    try:
        buyer_email = request.json['buyer_email']
        event.update(dict(buyer_email=buyer_email,
                          created_at=datetime.utcnow()))

    except:
        pass

    try:
        buyer_AddressLine1 = request.json['buyer_AddressLine1']
        event.update(dict(buyer_AddressLine1=buyer_AddressLine1,
                          created_at=datetime.utcnow()))

    except:
        pass

    try:
        buyer_AddressLine2 = request.json['buyer_AddressLine2']
        event.update(dict(buyer_AddressLine2=buyer_AddressLine2,
                          created_at=datetime.utcnow()))

    except:
        pass

    db.session.commit()
    print("event is =", event)
    return {'event': format_event_buyer(event.one())}


if __name__ == '__main__':
    app.run(debug=True, port=7070)
