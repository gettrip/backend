"""unique constr added for routes

Revision ID: 41ab4c801e53
Revises: 80ab071d8611
Create Date: 2022-04-04 18:24:56.266364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41ab4c801e53'
down_revision = '80ab071d8611'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('routes_name_key', 'routes', type_='unique')
    op.create_unique_constraint(None, 'routes', ['name', 'city_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'routes', type_='unique')
    op.create_unique_constraint('routes_name_key', 'routes', ['name'])
    # ### end Alembic commands ###
