"""empty message

Revision ID: 1b2af4f493c1
Revises: 0ea201a58210
Create Date: 2022-06-24 11:39:46.412445

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1b2af4f493c1'
down_revision = '0ea201a58210'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planeta', sa.Column('name', sa.String(length=50), nullable=False))
    op.add_column('planeta', sa.Column('diameter', sa.Integer(), nullable=True))
    op.add_column('planeta', sa.Column('rotation', sa.Integer(), nullable=True))
    op.add_column('planeta', sa.Column('translation', sa.Integer(), nullable=True))
    op.add_column('planeta', sa.Column('gravity', sa.Integer(), nullable=True))
    op.drop_index('nombre', table_name='planeta')
    op.drop_index('nombre_2', table_name='planeta')
    op.create_unique_constraint(None, 'planeta', ['name'])
    op.drop_column('planeta', 'rotación')
    op.drop_column('planeta', 'traslación')
    op.drop_column('planeta', 'diametro')
    op.drop_column('planeta', 'gravedad')
    op.drop_column('planeta', 'nombre')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planeta', sa.Column('nombre', mysql.VARCHAR(length=50), nullable=False))
    op.add_column('planeta', sa.Column('gravedad', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('planeta', sa.Column('diametro', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('planeta', sa.Column('traslación', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('planeta', sa.Column('rotación', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'planeta', type_='unique')
    op.create_index('nombre_2', 'planeta', ['nombre'], unique=False)
    op.create_index('nombre', 'planeta', ['nombre'], unique=False)
    op.drop_column('planeta', 'gravity')
    op.drop_column('planeta', 'translation')
    op.drop_column('planeta', 'rotation')
    op.drop_column('planeta', 'diameter')
    op.drop_column('planeta', 'name')
    # ### end Alembic commands ###
