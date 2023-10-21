from flask import Blueprint, render_template, request
lab4=Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET': 
        return render_template('login.html')

    username = request.form.get('username')
    password = request.form.get('password')

    if not username:
        error = 'Не введен логин'
        return render_template('login.html', error=error, username=username, password=password)
    
    if not password:
        error = 'Не введен пароль'
        return render_template('login.html', error=error, username=username, password=password)


    if username == 'polina' and password == '12345':
        return render_template('succesfull.html', username=username,)

    error = 'Неверный логин и/или пароль'
    return render_template('login.html', error=error, username=username, password=password)

@lab4.route('/lab4/holod', methods=['GET', 'POST'])
def holod():
    if request.method == 'GET':
        return render_template('holod.html')

    temperature = request.form.get('temperature')

    if not temperature:
        error = 'ошибка: не задана температура'
        return render_template('holod.html', error=error, temperature=temperature, snowflakes=0)
    
    temperature = int(temperature)  # Преобразование в целое число

    snowflakes = 0

    if temperature < -12:
        error = "Не удалось установить температуру — слишком низкое значение"
        return render_template('holod.html', error=error, temperature=temperature, snowflakes=snowflakes)

    elif temperature >= -12 and temperature <= -9:
        error = "Установлена температура: {}°С".format(temperature)
        snowflakes = 3
        return render_template('holod.html', error=error, temperature=temperature, snowflakes=snowflakes)

    elif temperature >= -8 and temperature <= -5:
        error = "Установлена температура: {}°С".format(temperature)
        snowflakes = 2
        return render_template('holod.html', error=error, temperature=temperature, snowflakes=snowflakes)

    elif temperature >= -4 and temperature <= -1:
        error = "Установлена температура: {}°С".format(temperature)
        snowflakes = 1
        return render_template('holod.html', error=error, temperature=temperature, snowflakes=snowflakes)

    else:
        error = "Не удалось установить температуру — слишком высокое значение"
        return render_template('holod.html', temperature=temperature, error=error, snowflakes=snowflakes)



@lab4.route('/lab4/zerno', methods=['GET', 'POST'])
def zerno():
    if request.method == 'GET':
        return render_template('zerno.html')

    zerno = request.form.get('zerno')
    weight = request.form.get('weight')

    if not weight:
        error = 'не введён вес'
        return render_template('zerno.html', error=error, zerno=zerno)
    
    if int(weight) > 500:
        error = 'Такого объема сейчас нет в наличии.'
        return render_template('zerno.html', error=error, weight=weight)
    elif int(weight) <= 0:
        error = "неверное значение веса"
        return render_template('zerno.html', weight=weight,  error=error)
        
 # Цены зерна
    prices = {
        'ячмень': 12000,
        'овёс': 8500,
        'пшеница': 8700,
        'рожь': 14000
    }
    # Расчет суммы заказа
    total_price = int(weight) * prices[zerno]

    # Применение скидки при заказе более 50 тонн
    if int(weight) >= 50 and int(weight) <= 500:
        total_price *= 0.9
        message = "Применена скидка 10% за большой объем"

        return render_template('zerno.html', zerno=zerno, weight=weight, total_price=total_price, message=message)

    return render_template('zerno.html', zerno=zerno, weight=weight, total_price=total_price)


@lab4.route('/lab4/cookies', methods = ['GET', 'POST'])
def cookies():
    if request.method == 'GET': 
        return render_template('cookies.html')
    
    color = request.form.get('color')
    bg_color = request.form.get('bg_color')
    font_size = request.form.get('font_size')

    if color == bg_color:
        error = 'Цвет текста не должен совпадать с цветом фона'
        return render_template('cookies.html', error=error)
    
    headers = {
        'Set-Cookie': [
            'color=' + color + ';path=/',
            'bg_color=' + bg_color + ';path=/',
            'font_size=' + font_size + ';path=/'
            ],
        'Location': '/lab4/cookies'
}

    return '', 303, headers
