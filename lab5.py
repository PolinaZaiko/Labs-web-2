from flask import redirect, render_template, request, Blueprint 
import psycopg2

lab5 = Blueprint("lab5", __name__)

@lab5.route ("/lab5")
def main():
# Прописываем параметры подключения к БД
    conn = psycopg2.connect (
        host="127.0.0.1", 
        database="Knowledge_base_for_Zaiko_Polina",
        user="Zaiko_Polina_knowledge_base", 
        password="12345")

    # Получаем курсор. С помощью него мы можем выполнять SQL-запросы
    cur = conn.cursor ()

    # Пишем запрос, который psycog2 должен выполнить
    cur.execute ("SELECT * FROM users;")

    # fetchall - получить все строки, которые получились в результате # выполнения SQL-запроса в execute
    # Сохраняем эти строки в переменную result
    result = cur.fetchall ()

    # Закрываем соединение с БД
    cur.close ()
    conn.close ()

    print (result)

    return "go to console"


@lab5.route ("/lab5/users")
def users():
# Прописываем параметры подключения к БД
    conn = psycopg2.connect (
        host="127.0.0.1", 
        database="Knowledge_base_for_Zaiko_Polina",
        user="Zaiko_Polina_knowledge_base", 
        password="12345")

    # Получаем курсор. С помощью него мы можем выполнять SQL-запросы
    cur = conn.cursor ()

    # Пишем запрос, который psycog2 должен выполнить
    cur.execute ("SELECT * FROM users;")

    # fetchall - получить все строки, которые получились в результате # выполнения SQL-запроса в execute
    # Сохраняем эти строки в переменную result
    result = cur.fetchall ()

    # Закрываем соединение с БД
    cur.close ()
    conn.close ()

    # Создаем пустой список для хранения имен пользователей
    names = []

     # Проходимся по каждой строке в результате и добавляем имена в список
    for user in result:
        names.append(user[1])

    return render_template('users.html', names=names)