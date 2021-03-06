"""empty message

Revision ID: 1622243365503
Revises: 1622243187118
Create Date: 2021-05-29 06:09:26.000060

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1622243365503'
down_revision = '1622243187118'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('task', 'iteration_id',
               existing_type=postgresql.UUID(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('task', 'iteration_id',
               existing_type=postgresql.UUID(),
               nullable=True)
    # ### end Alembic commands ###
