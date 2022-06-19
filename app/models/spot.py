from .db import db

class Spot(db.Model):
    __tablename__ = 'spots'

    id = db.Column(db.Integer, primary_key=True)
    home_type = db.Column(db.String(40), nullable=False)
    room_type = db.Column(db.String(40), nullable=False)
    total_occupancy = db.Column(db.Integer, nullable=False)
    total_bedrooms = db.Column(db.Integer, nullable=False)
    total_bathrooms = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(40), nullable=False)
    state = db.Column(db.String(40), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    house_style = db.Column(db.Integer, db.ForeignKey('houses.id'), nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), server_onupdate=db.func.now())

    def to_dict(self):
      return {
        'id': self.id,
        'home_type': self.home_type,
        'room_type': self.room_type,
        'total_occupancy': self.total_occupancy,
        'total_bedrooms': self.total_bedrooms,
        'total_bathrooms': self.total_bathrooms,
        'description': self.description,
        'address': self.address,
        'city': self.city,
        'state': self.state,
        'price': self.price,
        'owner_id': self.owner_id,
        'house_style': self.house_style,
        'longitude': self.longitude,
        'latitude': self.latitude,
        'created_at': self.created_at,
        'updated_at': self.updated_at
      }
