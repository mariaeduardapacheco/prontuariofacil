# -*- encoding: utf-8 -*-
from prontuariofacil.ext.database import db

class Prontuario(db.Model):
    __tablename__ = "prontuario"
    id = db.Column('id', db.Integer, primary_key=True)
    nome = db.Column('nome', db.String(255))
    nascimento = db.Column('nascimento', db.Date)
    numsus = db.Column('numSUS', db.String(25))
    cpf = db.Column('cpf', db.String(25))
    alergia = db.Column('alergia', db.String(255))
    doencas = db.Column('doencas', db.String(255))
    historico_fami = db.Column('Historico_fami', db.Text)

    def __repr__(self) -> str:
        return f'Nome completo do paciente: {self.nome} CPF: {self.cpf} Data de Data de nascimento: {self.nascimento} SUS: {self.numsus} Alergias: {self.alergia}  Doenças pré existentes: {self.doencas} Histórico familiar: {self.historico_fami}'

class Medico(db.Model):
    __tablename__ = "medico"
    id = db.Column('id', db.Integer, primary_key=True)
    nome = db.Column('nome', db.String(255))
    crm = db.Column('crm', db.String(25))
    email = db.Column('email', db.String(25))
    senha = db.Column('senha', db.String(25))