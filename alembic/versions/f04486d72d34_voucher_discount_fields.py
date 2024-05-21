"""Voucher discount fields

Revision ID: f04486d72d34
Revises: b0aa081a93ae
Create Date: 2024-05-21 22:42:49.070879

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f04486d72d34'
down_revision: Union[str, None] = 'b0aa081a93ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vouchers', sa.Column('discount_value', sa.Integer(), nullable=True))
    op.add_column('vouchers', sa.Column('discount_type', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vouchers', 'discount_type')
    op.drop_column('vouchers', 'discount_value')
    # ### end Alembic commands ###