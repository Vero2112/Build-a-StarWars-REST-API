"""empty message

Revision ID: b99e449813ce
Revises: 1b2af4f493c1
Create Date: 2022-06-24 12:24:06.300898

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b99e449813ce'
down_revision = '1b2af4f493c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('personaje',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('eye_color', sa.String(length=10), nullable=True),
    sa.Column('birthday_date', sa.String(length=20), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('personaje')
    # ### end Alembic commands ###
