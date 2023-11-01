from werkzeug.security import check_password_hash, generate_password_hash 
from flask import redirect, render_template, request, Blueprint, session 
import psycopg2

lab5 = Blueprint("lab5", __name__)

def dbConnect():
    conn = psycopg2.connect (
        host="127.0.0.1", 
        database="Knowledge_base_for_Zaiko_Polina",
        user="Zaiko_Polina_knowledge_base", 
        password="12345")
    
    return conn

def dbClose (cursor, connection):
# Закрываем курсор и соединение
# Порядок важен!
    cursor.close ()
    connection.close ()

@lab5.route ("/lab5")
def main():
    if 'username' in session:
        visibleUser = session['username']
    else:
        visibleUser = "Anon"
    return render_template ('lab5.html', username=visibleUser)

@lab5.route ("/lab5/users")
def users():
    conn = dbConnect()
    cur = conn.cursor ()

    cur.execute ("SELECT * FROM users;")

    result = cur.fetchall()

    # Создаем пустой список для хранения имен пользователей
    names = []

     # Проходимся по каждой строке в результате и добавляем имена в список
    for user in result:
        names.append(user[1])

    dbClose(cur, conn)      
    return render_template('users.html', names=names)

@lab5.route('/lab5/register', methods=["GET", "POST"]) 
def registerPage() :
    errors = []

    if request.method == "GET":
        return render_template ("register.html", errors=errors)
    

    username = request.form.get ("username")
    password = request. form.get ("password")

    if not (username or password):
        errors. append("Пожалуйста, заполните все поля")
        print(errors)
        return render_template ("register.html", errors=errors, username=username, password=password)

    hashPassword = generate_password_hash(password)

    conn = dbConnect()
    cur = conn.cursor()


    cur.execute(f"SELECT username FROM users WHERE username = '{username}';")

    if cur.fetchone() is not None:
        errors.append ("Пользователь с данным именем уже существует")
        
        dbClose (cur, conn) 
        return render_template ("register.html", errors=errors, username=username, password=password)
    
   
    cur.execute (f"INSERT INTO users (username, password) VALUES ('{username}', '{hashPassword}');")

    conn.commit()
    dbClose(cur, conn)

    return redirect("/lab5/log")

@lab5.route('/lab5/log', methods= ["GET", "POST"]) 
def loginPage():
    errors = []

    if request.method == "GET":
        return render_template("log.html", errors=errors)
    
    username = request.form.get("username")
    password = request.form.get("password")

    if not (username or password):
        errors.append("Пожалуйста, заполните все поля")
        return render_template ("log.html", errors=errors)
    
    conn = dbConnect()
    cur = conn.cursor()
    
    cur.execute(f"SELECT id, password FROM users WHERE username = '{username}';")
    result = cur.fetchone()

    if result is None:
        errors.append("Неправильный логин или пароль")
        dbClose (cur, conn) 
        return render_template ("log.html", errors=errors)
    
    userID, hashPassword = result

    if check_password_hash(hashPassword, password):
        session['id'] = userID
        session['username'] = username
        dbClose(cur, conn)
        return redirect("/lab5")

    else:
        errors.append ("Неправильный логин или пароль")
        return render_template ("log.html", errors=errors)
    

@lab5.route ("/lab5/new_article", methods=["GET", "POST"]) 
def createArticle():
    errors = []

    userID = session.get("id")

    if userID is not None:
        if request.method == "GET":
            return render_template("new_article.html")
        
        if request.method == "POST":
            text_article = request.form.get("text_article")
            title = request.form.get("title_article")
            
            if len(text_article) == 0:
                errors.append ("Заполните текст")
                return render_template ("new_article.html", errors=errors)
            
            conn = dbConnect()
            cur = conn.cursor()
            
            cur.execute (f"INSERT INTO articles (user_id, title, article_text) VALUES ({userID}, '{title}', '{text_article}') RETURNING id")

            new_article_id = cur.fetchone()[0]
            conn.commit ()

            dbClose (cur,conn)
    
            return redirect (f"/lab5/articles/{new_article_id}")
            
        return redirect(")/lab5/login")