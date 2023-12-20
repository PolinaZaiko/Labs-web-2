from flask import Blueprint, render_template, request, redirect, url_for

lab9 = Blueprint ("lab9", __name__)

@lab9.route('/lab9/')
def main ():
    return render_template ('lab9/index.html')

@lab9.app_errorhandler(404)
def not_found(e):
    return render_template('lab9/error404.html'), 404

@lab9.app_errorhandler(500)
def server_error(e):
    return render_template('lab9/error500.html'), 500

# Роут для вызова ошибки 500
@lab9.route('/lab9/cause500')
def cause_error():
    return 1 / 0


@lab9.route('/lab9/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        recipient_name = request.form.get('recipient_name')
        recipient_gender = request.form.get('recipient_gender')
        sender_name = request.form.get('sender_name')
        return redirect(url_for('lab9.greeting_card', recipient_name=recipient_name, recipient_gender=recipient_gender, sender_name=sender_name))
    return render_template('lab9/index.html')

@lab9.route('/lab9/greeting_card/')
def greeting_card():
    recipient_name = request.args.get('recipient_name')
    recipient_gender = request.args.get('recipient_gender')
    sender_name = request.args.get('sender_name')
    return render_template('lab9/greeting_card.html', recipient_name=recipient_name, recipient_gender=recipient_gender, sender_name=sender_name)
