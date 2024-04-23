"""vocher tables

Revision ID: cc674fee8528
Revises: cff9bc858424
Create Date: 2024-04-22 23:43:38.743480

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "cc674fee8528"
down_revision: Union[str, None] = "cff9bc858424"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "vouchers",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("name", sa.String(length=20), nullable=True),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("product_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["products.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_vouchers_id"), "vouchers", ["id"], unique=False)
    op.create_table(
        "voucher_codes",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("voucher_id", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("code", sa.UUID(), nullable=False),
        sa.Column("used", sa.Boolean(), nullable=True),
        sa.Column("used_at", sa.DateTime(), nullable=True),
        sa.Column("last_retrieved_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["voucher_id"],
            ["vouchers.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_voucher_codes_id"), "voucher_codes", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_voucher_codes_id"), table_name="voucher_codes")
    op.drop_table("voucher_codes")
    op.drop_index(op.f("ix_vouchers_id"), table_name="vouchers")
    op.drop_table("vouchers")
    # ### end Alembic commands ###
