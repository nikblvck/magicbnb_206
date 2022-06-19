from app.models import db, Spot


def seed_spots():
    spots = [
        {
            'home_type': 'House',
            'room_type': 'Entire House',
            'total_occupancy': 4,
            'total_bedrooms': 2,
            'total_bathrooms': 2,
            'description': 'This is a great house, even has access to the Floo network!',
            'address': '123 Main St',
            'city': 'New York',
            'state': 'NY',
            'price': 100,
            'owner_id': 1,
            'house_style': 1,
            'longitude': -73.935242,
            'latitude': 40.730610,
            'created_at': '2022-01-01 00:00:00',
            'updated_at': '2022-01-01 00:00:00'
        },
        {
            'home_type': 'Apartment',
            'room_type': 'Entire Apartment',
            'total_occupancy': 2,
            'total_bedrooms': 1,
            'total_bathrooms': 1,
            'description': 'Quiet apartment in South Seattle with a great view of Lake Washington',
            'address': '456 Seward Park Lane Apt #4',
            'city': 'Seattle',
            'state': 'WA',
            'price': 200,
            'owner_id': 1,
            'house_style': 2,
            'longitude': -122.332069,
            'latitude': 47.606209,
            'created_at': '2022-01-01 00:00:00',
            'updated_at': '2022-01-01 00:00:00'
        }
    ]

    for spot in spots:
        new_spot = Spot(**spot)
        db.session.add(new_spot)

    db.session.commit()


def undo_spots():
    db.session.execute('TRUNCATE spots RESTART IDENTITY CASCADE;')
    db.session.commit()
