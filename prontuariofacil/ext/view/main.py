from flask  import Blueprint, render_template
from ..models.models import Medico


bp = Blueprint("view", __name__)

@bp.route("/")
def index():
    return render_template('index.html')

@bp.route("/formulario")
def forms():
    return render_template('forms.html')

@bp.route("/user/add", methods=['GET','POST'])
def add_user():
    user = Medico()    
    return render_template('user_add.html',user=user)

@bp.route("/cadastro-prontuario")
def cadastroPront():
    return render_template("cadastroPront.html")

@bp.route("/recuperacao-de-senha")
def resenha():
    return render_template("recupSenha.html")

@bp.route("/cadastro-medico")
def cadastroMedico():
    return render_template("cadastroMedico.html")

@bp.route("/consulta-prontuario")
def consultaProntuario():
    return render_template("consultaProntuario.html")

@bp.route("/login")
def login():
    return render_template("login.html")

@bp.route("/escolha")
def escolha():
    return render_template("opcaoEscolha.html")