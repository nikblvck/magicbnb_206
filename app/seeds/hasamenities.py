from app.models import db, HasAmenity

def seed_hasamenities():
    hasamenities = [
        {'amenity_id': 1, 'spot_id': 1},
        {'amenity_id': 2, 'spot_id': 1},
        {'amenity_id': 3, 'spot_id': 1},
        {'amenity_id': 4, 'spot_id': 1},
        {'amenity_id': 5, 'spot_id': 2},
        {'amenity_id': 1, 'spot_id': 2},
        {'amenity_id': 2, 'spot_id': 2}

    ]

    for hasamenity in hasamenities:
        new_hasamenity = HasAmenity(**hasamenity)
        db.session.add(new_hasamenity)

    db.session.commit()

def undo_hasamenities():
    db.session.execute('TRUNCATE hasamenities RESTART IDENTITY CASCADE;')
    db.session.commit()
