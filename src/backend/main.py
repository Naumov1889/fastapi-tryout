from pydantic import BaseModel

from fastapi import FastAPI

from src.backend.core.db import SQLALCHEMY_DATABASE_URL

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    email: str


@app.get('/user/{user_id}', response_model=User)
def home(user_id: int):
    print(SQLALCHEMY_DATABASE_URL)
    user = {
        'id': user_id,
        'username': 'my_username',
        'email': 'myemail@test.com'
    }
    return user


@app.post('/user/')
def set_user(user: User):
    return {'key': user}
