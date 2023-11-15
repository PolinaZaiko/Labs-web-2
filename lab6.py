from werkzeug.security import check_password_hash, generate_password_hash 
from flask import redirect, render_template, request, Blueprint, session 
import psycopg2

lab6 = Blueprint("lab6", __name__)

