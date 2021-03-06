"""empty message

Revision ID: f4c21269287e
Revises: d3c88021680f
Create Date: 2018-03-15 18:13:44.648000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f4c21269287e'
down_revision = 'd3c88021680f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('user_type_id', sa.Integer(), nullable=True))
    op.drop_constraint(u'user_ibfk_2', 'user', type_='foreignkey')
    op.create_foreign_key(None, 'user', 'user_types', ['user_type_id'], ['id'])
    op.drop_column('user', 'user_type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('user_type', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.create_foreign_key(u'user_ibfk_2', 'user', 'user_types', ['user_type'], ['id'])
    op.drop_column('user', 'user_type_id')
    # ### end Alembic commands ###
