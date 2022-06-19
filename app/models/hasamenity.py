from .db import db

class HasAmenity(db.Model):
  __tablename__ = 'has_amenities'

  id = db.Column(db.Integer, primary_key=True)
  amenity_id = db.Column(db.Integer, db.ForeignKey('amenities.id'), nullable=False)
  spot_id = db.Column(db.Integer, db.ForeignKey('spots.id'), nullable=False)

  amenity = db.relationship('Amenity', backref='has_amenities')

  def to_dict(self):
    return {
      'id': self.id,
      'amenity_id': self.amenity_id,
      'spot_id': self.spot_id,
      'amenity': self.amenity.name
    }
