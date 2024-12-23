"""updated courses

Revision ID: ab8aa38e303a
Revises: 7e544de39c15
Create Date: 2024-12-22 22:32:07.719169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab8aa38e303a'
down_revision = '7e544de39c15'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('courses', sa.Column('course_desc', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('courses', 'course_desc')
    # ### end Alembic commands ###