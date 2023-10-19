from flask import Blueprint, redirect, url_for
lab1=Blueprint('lab1', __name__)


@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect ("/menu", code=302)


@lab1.route("/menu")
def menu():
    return '''
<!DOCTYPE html>
<html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>  
    </head>

    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        <div style="margin-bottom: 100px">
            <h1 style="margin-top: 100px"><a href = "/lab1">Первая лабораторная</a></h1>
            <h1><a href = "/lab2">Вторая лабораторная</a></h1>
            <h1><a href = "/lab3">Третья лабораторная</a></h1>
            <h1><a href = "/lab4">Четвертая лабораторная</a></h1>
        </div>

        <footer>
            &copy; Заико Полина, ФБИ-14, 3 курс, 2023  
        </footer>
    </body>
</html>
'''


@lab1.route("/lab1")
def lab():
    return '''
<!DOCTYPE html>
<html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <head>
        <title>Заико Полина Алексеевна. Лабораторная 1</title>  
    </head>

    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

       <h1 style="margin-top: 100px">
            Flask — фреймворк для создания веб-приложений на языке 
            программирования Python, использующий набор инструментов 
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории
            так называемых микрофреймворков — минималистичных каркасов 
            веб-приложений, сознательно предоставляющих лишь самые 
            базовые возможности.
        </h1>

        <h1><a href = "/menu">Меню</a></h1>

        <h2>Реализованные роуты</h2>

        <ul>
            <li><a href="/lab1/oak">дуб</a></li>
            <li><a href="/lab1/student">Студент</a></li></li>
            <li><a href="/lab1/python">Python</a></li></li>
            <li><a href="/lab1/fitnes">Фитнес</a></li></li>
        </ul>

        <footer>
            &copy; Заико Полина, ФБИ-14, 3 курс, 2023  
        </footer>
    </body>
</html>
'''


@lab1.route("/lab1/oak")
def oak():
    return '''
<!DOCTYPE html>
<html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
       <h1>Дуб</h1>
       <img src="''' + url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
'''


@lab1.route("/lab1/student")
def student():
    return '''
<!DOCTYPE html>
<html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <h1>Заико Полина Алексеевна</h1>
        <img src="''' + url_for('static', filename='logo.png') + '''">
    </body>
</html>
'''


@lab1.route("/lab1/python")
def python():
    return '''
<!DOCTYPE html>
<html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <h1>Что такое Python?</h1>

        <div>
            Python — это язык программирования, который широко используется в 
            интернет-приложениях, разработке программного обеспечения, науке о данных 
            и машинном обучении (ML). Разработчики используют Python, потому что он
            эффективен, прост в изучении и работает на разных платформах. Программы 
            на языке Python можно скачать бесплатно, они совместимы со всеми типами 
            систем и повышают скорость разработки.
        </div>

        <h1>Где применяется Python?</h1>

        <div>
            Язык Python имеет несколько стандартных примеров 
            использования при разработке приложений, в числе которых:
        </div>

        <h2>Веб-разработка на стороне сервера</h2>

        <div>
           еб-разработка на стороне сервера включает в себя 
           сложные серверные функции, с помощью которых веб-сайты 
           отображают информацию для пользователя. Например, веб-сайты 
           должны взаимодействовать с базами данных и другими веб-сайтами,
           а также защищать данные при их отправке по сети.  
        </div>

        <h2>Автоматизация с помощью скриптов Python</h2>

        <div>
           Язык скриптов — это язык программирования, который 
           автоматизирует задачи, обычно выполняемые людьми. 
           Программисты широко используют скрипты Python для 
           автоматизации многих повседневных задач.
        </div>

        <h2>Разработка программного обеспечения</h2>

        <div style="margin-bottom: 30px">
           Разработчики программного обеспечения часто 
           используют Python для различных задач разработки и программных приложений.
        </div>

        <img src="''' + url_for('static', filename='prog.jpeg') + '''">
    </body>
</html>
'''


@lab1.route("/lab1/fitnes")
def fitnes():
    return '''
<!DOCTYPE html>
<html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <h1>Что такое фитнес?</h1>

        <div>
            Фитнес - это оздоровительная методика, направленная на 
            поддержание физической формы. Что становится возможным 
            лишь тогда, когда фитнес прочно входит в образ жизни 
            человека, меняя режим дня, двигательную активность, 
            психическое здоровье, формируя позитивное мировосприятие.
        </div>

        <h1>История фитнеса</h1>

        <div>
            Фитнес имеет древнюю историю, начиная с эпохи древних 
            греков и римлян, которые активно занимались физическими 
            упражнениями. Однако современный фитнес начал развиваться 
            в 20 веке с появлением первых тренажеров и специализированных залов.
            С течением времени фитнес стал все более популярным, и сейчас
            предлагает широкий спектр тренировок для различных целей и уровней подготовки.
        </div>

        <h1>Как начать заниматься фитнесом?</h1>

        <div style="margin-bottom: 30px"> 
            Перед тем как начать заниматься фитнесом, важно определить 
            свои цели и уровень физической подготовки. Затем следует 
            разработать план тренировок, который включает в себя 
            разнообразные упражнения, регулярность и постепенное 
            увеличение интенсивности тренировок. Рекомендуется 
            также проконсультироваться с тренером или специалистом 
            по фитнесу, чтобы получить профессиональные рекомендации и советы.
        </div>

        <img src="''' + url_for('static', filename='fit.jpeg') + '''" >
    </body>
</html>
'''
