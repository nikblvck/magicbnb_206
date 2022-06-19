from flask.cli import AppGroup
from .users import seed_users, undo_users
from .houses import seed_houses, undo_houses
from .spots import seed_spots, undo_spots
from .images import seed_images, undo_images
from .amenities import seed_amenities, undo_amenities
from .hasamenities import seed_hasamenities, undo_hasamenities
# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_houses()
    seed_users()
    seed_spots()
    seed_images()
    seed_amenities()
    seed_hasamenities()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_houses()
    undo_users()
    undo_spots()
    undo_images()
    undo_amenities()
    undo_hasamenities()
    # Add other undo functions here
