"""Initial Migration

Revision ID: e00dddf2b617
Revises: ae29b132741a
Create Date: 2022-06-22 14:39:53.132907

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel             # NEW


# revision identifiers, used by Alembic.
revision = 'e00dddf2b617'
down_revision = 'ae29b132741a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('version_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('versionhistory')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('versionhistory',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('tag', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='versionhistory_pkey')
    )
    op.drop_table('version_history')
    # ### end Alembic commands ###