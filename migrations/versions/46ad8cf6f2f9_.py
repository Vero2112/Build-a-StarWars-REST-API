"""empty message

Revision ID: 46ad8cf6f2f9
Revises: b99e449813ce
Create Date: 2022-06-24 13:11:40.187924

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '46ad8cf6f2f9'
down_revision = 'b99e449813ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
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
    op.create_table('favoritos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planeta.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('name', table_name='personaje')
    op.drop_index('name_2', table_name='personaje')
    op.drop_table('personaje')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('personaje',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('eye_color', mysql.VARCHAR(length=10), nullable=True),
    sa.Column('birthday_date', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('gender', mysql.VARCHAR(length=10), nullable=True),
    sa.Column('height', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('name_2', 'personaje', ['name'], unique=False)
    op.create_index('name', 'personaje', ['name'], unique=False)
    op.drop_table('favoritos')
    op.drop_table('character')
    # ### end Alembic commands ###