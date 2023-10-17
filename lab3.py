from flask import Blueprint, render_template, request
lab3=Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/form1/')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
        
    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)

@lab3.route('/lab3/order/')
def order():
    return render_template('order.html')

@lab3.route('/lab3/pay/')
def pay():
    price=0
    drink = request.args.get('drink' )
# Пусть кофе стоит 120 рублей, чёрный чай - 80 рублей, зелёный - 70 рублей.
    if drink == 'cofee':
        price = 120
    elif drink == 'b-tea':
        price = 80
    else:
        price = 70
# Добавка молока удорожает напиток на 30 рублей, • а сахара - на 10.
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get ('sugar') == 'on':
        price += 10
    return render_template('pay.html', price = price)

@lab3.route('/lab3/success/')
def success():
    return render_template('success.html')

@lab3.route('/lab3/bilet/')
def bilet():
    errors = {}
    pas = request.args.get('pas')
    if pas == '':
        errors['pas'] = 'Заполните поле!'

    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
        
    type = request.args.get('type')

    polka = request.args.get('polka')

    baggage = request.args.get('baggage')

    viezd= request.args.get('viezd')
    if viezd == '':
        errors['viezd'] = 'Заполните поле!'

    naznach = request.args.get('naznach')
    if naznach == '':
        errors['naznach'] = 'Заполните поле!'

    date = request.args.get('date')
    if date == '':
        errors['date'] = 'Заполните поле!'

    return render_template('bilet.html', pas=pas, age=age, errors=errors, type=type, polka=polka, baggage=baggage, viezd=viezd, naznach=naznach, date=date)

@lab3.route('/lab3/oplatabileta/')
def oplatabileta():
    price = 2000
    
    # Не работает почему-то
    # price = 0
    # type = request.args.get('type' )
    # if type == 'det':
    #     price = 1000
    # elif type == 'vzr':
    #     price = 2000
    # else: 
    #     price = 0

    # if request.args.get('baggage' ) == 'on':
    #     price += 500

    return render_template('oplatabileta.html', price=price)
 
@lab3.route('/lab3/gotbilet/')
def gotbilet():
    return render_template('gotbilet.html')
