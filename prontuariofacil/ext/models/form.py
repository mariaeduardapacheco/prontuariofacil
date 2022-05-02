import wtforms as wtf
from flask_wtf import FlaskForm

class Prontuario(FlaskForm):
    nome = wtf.StringField("Nome completo do paciente", validators=[wtf.validators.DataRequired()])
    cpf = wtf.StringField("CPF")
    nasc = wtf.DateField("Data de nascimento")
    sus = wtf.StringField("SUS")
    alergia = wtf.StringField("Alergias")
    doenca = wtf.StringField("Doenças pré existentes")
    historico = wtf.StringField("Histórico familiar")
    submit = wtf.SubmitField("Confirmar cadastro")

