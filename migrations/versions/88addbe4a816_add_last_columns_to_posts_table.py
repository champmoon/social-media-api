"""add last columns to posts table

Revision ID: 88addbe4a816
Revises: a014203b6e91
Create Date: 2022-02-06 14:28:09.979778

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88addbe4a816'
down_revision = 'a014203b6e91'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column(
            "published",
            sa.Boolean(),
            nullable=False,
            server_default="TRUE"
        )
    )
    op.add_column(
        "posts",
        sa.Column(
            "created",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()")
        )
    )


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created")
