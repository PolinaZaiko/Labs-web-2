from flask import Flask
app=Flask(__name__)

@app.route("/")
def start():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>Заико Полина Алексеевна, Лабораторная 1</title>  
    </head>

    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

       <h1>web-сервер на flask</h1>

        <footer>
            &copy; Заико Полина, ФБИ-14, 3 курс, 2023  
        </footer>
    </body>
</html>
"""