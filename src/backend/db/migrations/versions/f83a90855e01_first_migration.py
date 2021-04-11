"""first_migration

Revision ID: f83a90855e01
Revises: 
Create Date: 2021-04-10 14:36:01.030801

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f83a90855e01'
down_revision = None
branch_labels = None
depends_on = None


def create_some_test_table() -> None:
    op.create_table(
        "cleanings",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False, index=True),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("cleaning_type", sa.Text, nullable=False, server_default="spot_clean"),
        sa.Column("price", sa.Numeric(10, 2), nullable=False),
    )


def upgrade():
    create_some_test_table()


def downgrade():
    op.drop_table("posts")
