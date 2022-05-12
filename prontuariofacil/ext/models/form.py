import wtforms as wtf
from flask_wtf import FlaskForm

class Form(FlaskForm):
    nome = wtf.StringField("Nome completo do paciente", validators=[wtf.validators.DataRequired()])
    cpf = wtf.StringField("CPF")
    nasc = wtf.DateField("Data de nascimento")
    sus = wtf.StringField("SUS")
    alergia = wtf.StringField("Alergias")
    doenca = wtf.StringField("Doenças pré existentes")
    historico = wtf.StringField("Histórico familiar")
    submit = wtf.SubmitField("Confirmar cadastro")

class Form_medico(FlaskForm):
    nome = wtf.StringField("Nome completo", validators=[wtf.validators.DataRequired()])
    crm = wtf.StringField("CRM")
    email = wtf.StringField("E-mail")
    cadastrar_senha = wtf.StringField("Cadastre uma senha de 8 dígitos")
    confirmar_senha = wtf.StringField("Confirme a senha")
    submit = wtf.SubmitField("Confirmar cadastro")