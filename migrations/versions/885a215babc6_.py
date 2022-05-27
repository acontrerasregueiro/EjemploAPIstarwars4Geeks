"""empty message

Revision ID: 885a215babc6
Revises: 91e6eaad60a4
Create Date: 2022-05-23 17:15:23.965519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '885a215babc6'
down_revision = '91e6eaad60a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('terrain', sa.String(length=120), nullable=True),
    sa.Column('climate', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    # ### end Alembic commands ###
