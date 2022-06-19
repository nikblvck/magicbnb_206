from app.models import db, Amenity

def seed_amenities():
    amenities = [
        {'name': 'Wifi'},
        {'name': 'Washer & Dryer'},
        {'name': 'Coffee Machine'},
        {'name': 'Central Air Conditioning'},
        {'name': 'TV'},
        {'name': 'Kitchen'},
        {'name': 'Stocked Refrigerator'},
        {'name': 'Portkey Access'},
        {'name': 'Floo Network'},
        {'name': 'Pool'},
        {'name': 'Gym'},
        {'name': 'Hot Tub'},
        {'name': 'Ironing Board'},
        {'name': 'Hair Dryer'},
        {'name': 'Hair Iron'},
        {'name': 'Guest Parking'},
    ]

    for amenity in amenities:
        new_amenity = Amenity(**amenity)
        db.session.add(new_amenity)

    db.session.commit()

def undo_amenities():
    db.session.execute('TRUNCATE amenities RESTART IDENTITY CASCADE;')
    db.session.commit()
    
