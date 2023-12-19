from flask import Blueprint, render_template

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
