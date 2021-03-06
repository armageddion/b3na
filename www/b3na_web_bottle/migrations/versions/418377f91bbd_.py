"""empty message

Revision ID: 418377f91bbd
Revises: 6b4151a6ca63
Create Date: 2018-03-15 11:53:51.185000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '418377f91bbd'
down_revision = '6b4151a6ca63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('device', sa.Column('state_id', sa.Integer(), nullable=True))
    op.drop_constraint(u'device_ibfk_3', 'device', type_='foreignkey')
    op.create_foreign_key(None, 'device', 'states', ['state_id'], ['id'])
    op.drop_column('device', 'state')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('device', sa.Column('state', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'device', type_='foreignkey')
    op.create_foreign_key(u'device_ibfk_3', 'device', 'states', ['state'], ['id'])
    op.drop_column('device', 'state_id')
    # ### end Alembic commands ###
