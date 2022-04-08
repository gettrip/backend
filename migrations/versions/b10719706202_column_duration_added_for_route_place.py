"""column_duration_added_for_route_place

Revision ID: b10719706202
Revises: 41ab4c801e53
Create Date: 2022-04-06 21:38:33.332805

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b10719706202'
down_revision = '41ab4c801e53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('places', sa.Column('duration', sa.Integer(), nullable=True))
    op.add_column('routes', sa.Column('duration', sa.Integer(), nullable=True))
    op.execute('UPDATE places SET duration=3600')
    op.execute('UPDATE routes SET duration=18000')
    op.alter_column('places', 'duration', nullable=False)
    op.alter_column('routes', 'duration', nullable=False)
    op.alter_column('routes_points', 'distance',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('routes_points', 'distance',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('routes', 'duration')
    op.drop_column('places', 'duration')
    # ### end Alembic commands ###
