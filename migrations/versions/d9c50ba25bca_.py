"""empty message

Revision ID: d9c50ba25bca
Revises: 46ad8cf6f2f9
Create Date: 2022-06-24 14:37:03.532619

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd9c50ba25bca'
down_revision = '46ad8cf6f2f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('diameter', sa.Integer(), nullable=True),
    sa.Column('rotation', sa.Integer(), nullable=True),
    sa.Column('translation', sa.Integer(), nullable=True),
    sa.Column('gravity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('name', table_name='planeta')
    op.drop_table('planeta')
    op.drop_table('favoritos')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favoritos',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('planet_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('character_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], name='favoritos_ibfk_1'),
    sa.ForeignKeyConstraint(['planet_id'], ['planeta.id'], name='favoritos_ibfk_2'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='favoritos_ibfk_3'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('planeta',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('diameter', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('rotation', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('translation', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('gravity', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('name', 'planeta', ['name'], unique=False)
    op.drop_table('favorite')
    op.drop_table('planet')
    # ### end Alembic commands ###
