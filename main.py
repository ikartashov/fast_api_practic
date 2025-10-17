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
         tags=['Получить пользователей'],
         summary='Получить всех пользователей')
def get_users():
    return user_manager.get_users()


@app.get('/get/user_by_id',
         tags=['Получить пользователей'],
         summary='Получить конкретного пользователя')
def get_user_by_id(user_id: int):
    try:
        user = user_manager.get_user_by_id(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return user


@app.post('/post',
          response_model=list,
          tags=['Добавить нового пользователя'],
          summary='Добавить пользователя')
def post_users(new_user: User):
    try:
        user_manager.add_user(new_user.name)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return user_manager.get_users()

@app.patch('/patch',
           tags=['Обновить пользователя'],
           summary='Обновить пользователя')
def update_user(user_id, new_name):
    try:
        new_user = user_manager.update_user(user_id, new_name)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return new_user

@app.delete('/delete/{user_id}',
            tags=['Удалить пользователя'],
            summary='Удалить пользователя')
def delete_user(user_id:int):
    try:
        deleted_user = user_manager.delete_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return deleted_user


if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
