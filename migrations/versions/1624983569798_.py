"""empty message

Revision ID: 1624983569798
Revises: 1624981559158
Create Date: 2021-06-29 23:19:30.603890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1624983569798'
down_revision = '1624981559158'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('project_slack_team_admin_id_key', 'project', type_='unique')
    op.drop_column('project', 'slack_team_admin_id')
    op.add_column('user', sa.Column('slack_user_id', sa.String(), nullable=False))
    op.add_column('user', sa.Column('type', sa.String(), nullable=False))
    op.drop_constraint('user_slack_id_key', 'user', type_='unique')
    op.create_unique_constraint(None, 'user', ['slack_user_id'])
    op.drop_column('user', 'slack_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('slack_id', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'user', type_='unique')
    op.create_unique_constraint('user_slack_id_key', 'user', ['slack_id'])
    op.drop_column('user', 'type')
    op.drop_column('user', 'slack_user_id')
    op.add_column('project', sa.Column('slack_team_admin_id', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.create_unique_constraint('project_slack_team_admin_id_key', 'project', ['slack_team_admin_id'])
    # ### end Alembic commands ###
