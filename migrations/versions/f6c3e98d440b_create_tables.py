"""create tables

Revision ID: f6c3e98d440b
Revises: 
Create Date: 2023-10-11 21:26:40.723100

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy


# revision identifiers, used by Alembic.
revision: str = 'f6c3e98d440b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('question_id', sa.UUID(), nullable=False),
    sa.Column('question', sa.String(), nullable=False),
    sa.Column('answer', sa.String(), nullable=False),
    sa.Column('creation_date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('question_id'),
    sa.UniqueConstraint('question')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questions')
    # ### end Alembic commands ###
