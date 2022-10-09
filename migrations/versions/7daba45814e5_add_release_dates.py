"""add release_dates

Revision ID: 7daba45814e5
Revises: b9abf7802c27
Create Date: 2022-10-09 15:14:56.951416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7daba45814e5'
down_revision = 'b9abf7802c27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('release_dates',
    sa.Column('render', sa.String(), nullable=False),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.Column('release_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('render', 'version')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('release_dates')
    # ### end Alembic commands ###
