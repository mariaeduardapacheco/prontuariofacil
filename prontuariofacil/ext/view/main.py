import email
from mailbox import NotEmptyError
from typing_extensions import Self
from flask  import Blueprint, redirect, render_template, request
from ext.models.tables import Medico, Prontuario
from ext.models.form import Form, Form_medico
from ext.database import db


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

@bp.route("/cadastro-prontuario", methods=["GET", "POST"])
def cadastro_pront():
    form = Form()
    nome = (form.nome.data)
    cpf = (form.cpf.data)
    nasc = (form.nasc.data)
    sus = (form.sus.data)
    alergia = (form.alergia.data)
    doenca = (form.doenca.data)
    historico = (form.historico.data)
    
    i = Prontuario()
    i.alergia = alergia
    i.nome = nome
    i.cpf = cpf
    i.nascimento = nasc
    i.numsus = sus
    i.doencas = doenca
    i.historico_fami = historico
    db.session.add(i)
    db.session.commit()
    
    print(i.query.all())

    '''
    if form.validate_on_submit:
        prontuario = Prontuario(nome=form.nome, cpf=form.cpf, nascimento=form.nasc, numsus=form.sus, alergia=form.alergia, doencas=form.doenca ,historico_fami=form.historico)
        db.session.add(prontuario)
        db.session.commit()
    '''
    return render_template("cadastroPront.html", prontuario=form)

@bp.route("/cadastro-medico")
def cadastro_medico():
    form = Form_medico()
    medico = Medico()
    medico.nome = form.nome.data
    medico.crm = form.crm.data
    medico.email = form.email.data
    medico.senha = form.cadastrar_senha.data

    db.session.add(medico)
    db.session.commit()

    print(medico.query.all())

    return render_template("cadastroMedico.html", form=form)


@bp.route("/recuperacao-de-senha")
def resenha():
    return render_template("recupSenha.html")


@bp.route("/consulta-prontuario")
def consulta_prontuario():
    read = Prontuario.query.all()
    return render_template("consultaProntuario.html", read=read)

@bp.route("/login")
def login():
    return render_template("login.html")

@bp.route("/escolha")
def escolha():
    return render_template("opcaoEscolha.html")

@bp.route("/receiver", methods=["POST"])
def receiver():
    return f"teste {request.values['nome']}"