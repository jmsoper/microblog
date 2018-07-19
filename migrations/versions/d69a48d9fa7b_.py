"""empty message

Revision ID: d69a48d9fa7b
Revises: 0697d81b6648
Create Date: 2018-07-18 14:56:42.918334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd69a48d9fa7b'
down_revision = '0697d81b6648'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('title', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'title')
    # ### end Alembic commands ###