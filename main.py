from fastapi import FastAPI, HTTPException
from models import User
import json
from services import UserManager
import uvicorn
from database import create_table



app = FastAPI(title='Еще одна практика FastAPI')

create_table()
user_manager = UserManager()


@app.get('/get',
         tags=['Получить пользователя'],
         summary='Получить всех пользователей')
def get_users():
    return user_manager.get_users()


@app.post('/post',
          response_model=list,
          tags=['Добавить нового пользователя'])
def post_users(new_user: User):
    try:
        user_manager.add_user(new_user.name)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return user_manager.get_users()


if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
