from flask  import Blueprint, render_template, request
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


@bp.route("/cadastro-prontuario", methods=["GET", "POST"])
def cadastro_pront():
    name = None
    form = Form()

    if form.validate_on_submit:
        prontuario = Prontuario(nome=form.nome.data, cpf=form.cpf.data, nascimento=form.nasc.data, numsus=form.sus.data, alergia=form.alergia.data, doencas=form.doenca.data ,historico_fami=form.historico.data)
        db.session.add(prontuario)
        db.session.commit()
    
    return render_template("cadastroPront.html", prontuario=form, name = name)

@bp.route("/cadastro-medico", methods=["GET", "POST"])
def cadastro_medico():
    form = Form_medico()
    if form.validate_on_submit:
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

@bp.route("/update/<int:id>", methods=['GET','POST'])
def update(id):
    form = Form()
    prontuario_update = Prontuario.query.get_or_404(id)
    if request.method == "POST":
            prontuario_update.nome = form.nome.data
            prontuario_update.cpf = form.cpf.data
            prontuario_update.nascimento = form.nasc.data
            prontuario_update.numsus = form.sus.data
            prontuario_update.alergia = form.alergia.data
            prontuario_update.doencas = form.doenca.data
            prontuario_update.historico_fami = form.historico.data
            try:
                db.session.commit()
                print('update sucesso')
                return render_template("update_prontuario.html", prontuario_update = prontuario_update, prontuario = form)
            except:
                print("ERRO no update!")
                return render_template("update_prontuario.html", prontuario_update = prontuario_update, prontuario = form)
    else:
        return render_template("update_prontuario.html", prontuario_update = prontuario_update, prontuario = form)
    



@bp.route("/delete/<int:id>")
def delete(id):
    prontuari_delete =  Prontuario.query.get_or_404(id)
    try:
        db.session.delete(prontuari_delete)
        db.session.commit()
        print("Prontuario deletado com sucesso")
        read = Prontuario.query.all()
        return render_template("consultaProntuario.html", read=read)
    except:
        print("erro no delete")
        read = Prontuario.query.all()
        return render_template("consultaProntuario.html", read=read)
    