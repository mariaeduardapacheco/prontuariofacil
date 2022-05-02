from crypt import methods
from flask  import Blueprint, render_template, request
from ext.models.form import Prontuario


bp = Blueprint("view", __name__)

@bp.route("/")
def index():
    return render_template('index.html')

@bp.route("/formulario")
def forms():
    return render_template('forms.html')

#@bp.route("/user/add", methods=['GET','POST'])
# def add_user():
#    user = Medico()    
#    return render_template('user_add.html',user=user)

@bp.route("/cadastro-prontuario")
def cadastro_pront():
    prontuario = Prontuario()
    return render_template("cadastroPront.html", prontuario=prontuario)

@bp.route("/recuperacao-de-senha")
def resenha():
    return render_template("recupSenha.html")

@bp.route("/cadastro-medico")
def cadastro_medico():
    return render_template("cadastroMedico.html")

@bp.route("/consulta-prontuario")
def consulta_prontuario():
    return render_template("consultaProntuario.html")

@bp.route("/login")
def login():
    return render_template("login.html")

@bp.route("/escolha")
def escolha():
    return render_template("opcaoEscolha.html")

@bp.route("/receiver", methods=["POST"])
def receiver():
    return f"teste {request.values['nome']}"