from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/cs162'
db = SQLAlchemy(app)
CORS(app)


class Event(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __repr__(self):

        return self.description

    def __init__(self, description):

        self.description = description


def format_event(event):

    return {

        "description": event.description,
        "id": event.id,
        "created_at": event.created_at
    }


@app.route('/test', methods=['GET'])
def hello():
    if request.method == 'GET':
        return jsonify({"response": "IT IS WORKING, ABEN! CHILL BRO!"})


@app.route('/event', methods=['POST'])
def create_event():
    if request.method == 'POST':
        description = request.json['description']
        event = Event(description)
        db.session.add(event)
        db.session.commit()
        return format_event(event)


@app.route('/event',  methods=["GET"])
def get_events():

    events = Event.query.order_by(Event.id.asc()).all()
    event_list = []
    for event in events:
        event_list.append(format_event(event))

    return {'event': event_list}


@app.route('/event/<id>', methods=['GET'])
def get_event(id):

    event = Event.query.filter_by(id=id).one()
    formatted_event = format_event(event)
    return {'event': formatted_event}


@app.route('/event/<id>', methods=['DELETE'])
def delete_event(id):
    event = Event.query.filter_by(id=id).one()
    db.session.delete(event)
    db.session.commit()
    return 'Event is Deleted!'


@app.route('/event/<id>', methods=['PUT'])
def update_event(id):

    event = Event.query.filter_by(id=id)
    description = request.json['description']
    event.update(dict(description=description, created_at=datetime.utcnow()))
    db.session.commit()
    return {'event': format_event(event.one())}


if __name__ == '__main__':
    app.run(debug=True, port=9090)