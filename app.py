from flask import Flask, redirect, url_for, render_template
from lab1 import lab1

app=Flask(__name__)
app.register_blueprint(lab1)

@app.route('/lab2/example')
def example():
    name='Заико Полина'
    num_lab='Лабораторная работа 2'
    grup='ФБИ-14'
    kurs='3 курс'
    fruits = [
       {'name': 'Яблоки', 'price': 100},
       {'name': 'Груши', 'price': 150},
       {'name': 'Апельсины', 'price': 60},
       {'name': 'Мандарины', 'price': 200}, 
       {'name': 'Персики', 'price': 230}
    ]
    knigi = [
       {'autor': 'Джон Р. Р. Толкин', 'name': 'Властелин колец', 'zhanr': 'роман-эпопея', 'kolvo_str': 354},
       {'autor': 'Джейн Остин', 'name': 'Гордость и предубеждение', 'zhanr': 'роман', 'kolvo_str': 754},
       {'autor': 'Филип Пулман', 'name': 'Тёмные начала', 'zhanr': 'фантастическая трилогия', 'kolvo_str': 3345},
       {'autor': 'Дуглас Адамс', 'name': 'Автостопом по галактике', 'zhanr': 'фантастический роман', 'kolvo_str': 543},
       {'autor': 'Джоан Роулинг', 'name': 'Гарри Поттер и Кубок огня', 'zhanr': 'приключения', 'kolvo_str': 123},
       {'autor': 'Харпер Ли', 'name': 'Убить пересмешника', 'zhanr': 'роман-бестселлер', 'kolvo_str': 875},
       {'autor': 'Алан Александр Милн', 'name': 'Винни Пух', 'zhanr': 'повесть', 'kolvo_str': 47},
       {'autor': 'Джордж Оруэлл', 'name': '1984', 'zhanr': 'роман-антиутопия', 'kolvo_str': 654},
       {'autor': 'Клайв Стэйплз Льюис', 'name': 'Лев, колдунья и платяной шкаф', 'zhanr': 'роман', 'kolvo_str': 454},
       {'autor': 'Шарлотта Бронте', 'name': 'Джейн Эйр', 'zhanr': 'роман', 'kolvo_str': 5432}
    ]
    
    return render_template('example.html' , name=name, num_lаb=num_lab, grup=grup, kurs=kurs, fruits=fruits, knigi=knigi)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/dogs')
def dogs():
    return render_template('dogs.html')