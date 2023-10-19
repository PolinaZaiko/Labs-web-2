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
