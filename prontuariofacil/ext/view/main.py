from flask  import Blueprint, render_template

bp = Blueprint("view", __name__)

@bp.route("/")
def index():
    return render_template('index.html')

@bp.route("/ola")
def ola():
    return "Olá"