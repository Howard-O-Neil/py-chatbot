"""empty message

Revision ID: 1622203567901
Revises: 1622201764165
Create Date: 2021-05-28 19:06:08.297499

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1622203567901'
down_revision = '1622201764165'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('iteration',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('project_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('goal', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('velocity', sa.Float(), nullable=False),
    sa.Column('point', sa.Float(), nullable=False),
    sa.Column('estimated_hours', sa.Float(), nullable=False),
    sa.Column('logged_hours', sa.Float(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('iteration')
    # ### end Alembic commands ###