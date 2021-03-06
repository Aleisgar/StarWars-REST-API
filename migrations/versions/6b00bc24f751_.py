"""empty message

Revision ID: 6b00bc24f751
Revises: a60f38448623
Create Date: 2022-06-24 14:13:46.876509

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6b00bc24f751'
down_revision = 'a60f38448623'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('character', 'planet_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('character', 'ships_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('character', 'ships_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('character', 'planet_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
