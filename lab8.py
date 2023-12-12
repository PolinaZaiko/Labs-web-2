from flask import Blueprint, request, render_template, redirect, url_for, abort, jsonify

lab8 = Blueprint ("lab8", __name__)

@lab8.route('/lab8/index')
def main():
    return render_template('lab8/index.html')