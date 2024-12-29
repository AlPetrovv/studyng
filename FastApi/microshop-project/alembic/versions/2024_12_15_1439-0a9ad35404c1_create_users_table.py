"""create users table

Revision ID: 0a9ad35404c1
Revises: a62b45d9303f
Create Date: 2024-12-15 14:39:54.494360

"""

from typing import Sequence
from typing import Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "0a9ad35404c1"
down_revision: Union[str, None] = "a62b45d9303f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "shop_app__users",
        sa.Column("username", sa.String(length=32), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("username"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("shop_app__users")
    # ### end Alembic commands ###