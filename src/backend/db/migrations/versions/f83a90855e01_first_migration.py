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
        "posts",
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String(100)),
        sa.Column('text', sa.Text),
        sa.Column('date', sa.DateTime),
    )


def upgrade():
    create_some_test_table()


def downgrade():
    op.drop_table("posts")
