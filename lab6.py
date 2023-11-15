from flask import Blueprint, request, render_template, redirect 
from Db import db
# Данные объекты представляют из себя таблицы users и articles в БД
from Db.models import users, articles 
from werkzeug. security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user
import psycopg2

lab6 = Blueprint ("lab6", __name__)

@lab6.route("/lab6/check")
def main():
# Тоже самое, что select * from users
    my_users = users.query.all()
    print (my_users)
    return "result in console!"

@lab6.route("/lab6/chekarticles")
def chekarticles():
# Тоже самое, что select * from users
    my_articles = articles.query.all()
    print (my_articles)
    return "result in console!"