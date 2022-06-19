"""updated users table

Revision ID: 1ff169d72b7f
Revises: 02ddec3e05b8
Create Date: 2022-06-18 17:07:10.337423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ff169d72b7f'
down_revision = '02ddec3e05b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('house_allegiance', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'houses', ['house_allegiance'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'house_allegiance')
    # ### end Alembic commands ###