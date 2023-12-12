from flask import Flask
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8

from flask_sqlalchemy import SQLAlchemy  
from Db import db 
from Db.models import users 
from flask_login import LoginManager


app=Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab7)
app.register_blueprint(lab8)

app.secret_key = "12345"
user_db = "Zaiko_Polina_knowledge_base_orm"
host_ip = "127.0.0.1"
host_port = "5432"
database_name = "Knowledge_base_orm"
password = "12345"

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user_db}:{password}@{host_ip}:{host_port}/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Подключаем Flask-Login
login_manager = LoginManager ()
# Куда редиректить, если пользователь не авторизован, # а он пытается попасть на защищенную страницу
login_manager.login_view = "lab6.log2"
login_manager.init_app(app)
# Показываем Flask-Login как и где найти нужного пользователя
@login_manager.user_loader
def load_users(user_id):
    # Метод get вернет объект users с нужным id 
    #со всеми атрибутами и методами класса
    return users.query.get(int(user_id))

app.register_blueprint (lab6)