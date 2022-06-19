from app.models import db, House


def seed_houses():
    houses = [
     {
      'name': 'Gryffindor',
     },
     {
      'name': 'Slytherin',
     },
      {
      'name': 'Ravenclaw',
      },
      {
      'name': 'Hufflepuff',
      }
    ]

    for house in houses:
        new_house = House(**house)
        db.session.add(new_house)

    db.session.commit()

def undo_houses():
    db.session.execute('TRUNCATE houses RESTART IDENTITY CASCADE;')
    db.session.commit()
