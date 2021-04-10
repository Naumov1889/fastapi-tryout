import sqlalchemy as sa
from core.db import Base


class Post(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    title = sa.Column(sa.String)
    text = sa.Column(sa.Text(500))
    date = sa.Column(sa.Datetime)
