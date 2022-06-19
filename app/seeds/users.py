from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():
    users = [
        {
            'first_name': 'Demo',
            'last_name': 'User',
            'username': 'demo',
            'email': 'demo@magicbnb.io',
            'password': 'demopassword',
            'profile_pic': 'https://i.imgur.com/XyqQZ9x.png',
            'house_allegiance': 1
        },
        {
            'first_name': 'Harry',
            'last_name': 'Potter',
            'username': 'hpotter',
            'email': 'hpotter@magicbnb.io',
            'password': 'hedwig2022',
            'profile_pic': 'https://i.imgur.com/XyqQZ9x.png',
            'house_allegiance': 1
        }
    ]
    for user in users:
        new_user = User(**user)
        db.session.add(new_user)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
