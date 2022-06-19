from app.models import db, Image

def seed_images():
    images = [
    {
      'spot_id': 1,
      'url': 'https://res.cloudinary.com/bigtechnik/image/upload/v1655612824/magicbnb/seederPhotos/image_xxvrfr.png'
    },
    {
      'spot_id': 1,
      'url': 'https://res.cloudinary.com/bigtechnik/image/upload/v1655612826/magicbnb/seederPhotos/image_bcnioa.png'
    },
    {
      'spot_id': 1,
      'url': 'https://res.cloudinary.com/bigtechnik/image/upload/v1655612828/magicbnb/seederPhotos/image_f9rxss.png'
    },
    {
      'spot_id': 1,
      'url': 'https://res.cloudinary.com/bigtechnik/image/upload/v1655612830/magicbnb/seederPhotos/image_qxpjjr.png'
    },
    {
      'spot_id': 1,
      'url': 'https://res.cloudinary.com/bigtechnik/image/upload/v1655612835/magicbnb/seederPhotos/image_o7pxgh.png'
    },
    {
      'spot_id': 1,
      'url': 'https://res.cloudinary.com/bigtechnik/image/upload/v1655612837/magicbnb/seederPhotos/image_uerfgs.png'
    }
  ]

    for image in images:
      new_image = Image(**image)
      db.session.add(new_image)

    db.session.commit()

def undo_images():
  db.session.execute('TRUNCATE images RESTART IDENTITY CASCADE')
  db.session.commit()
