from .db import db

class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    spot_id = db.Column(db.Integer, db.ForeignKey('spots.id'), nullable=False)


    def to_dict(self):
        return {
            'id': self.id,
            'url': self.url,
            'spot_id': self.spot_id
        }



        
