"""added dept

Revision ID: 960bf4025c37
Revises: 83412c962531
Create Date: 2024-12-22 21:59:18.156905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '960bf4025c37'
down_revision = '83412c962531'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('departments',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('dept_name', sa.String(), nullable=True),
    sa.Column('dept_code', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('dept_code')
    )
    op.create_index(op.f('ix_departments_id'), 'departments', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_departments_id'), table_name='departments')
    op.drop_table('departments')
    # ### end Alembic commands ###
