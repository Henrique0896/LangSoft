from datetime import datetime
from flask_login import current_user
from app import db

class Registro():
    def __init__(self):
        self.usuario = None
        self.acao = None
        self.estadoAnterior = None
        self.estadoAtual = None
        self.data = None
    
    def registrarUsuarioCadastrado(self):
        self.usuario = current_user.email
        self.acao = "Novo usuário registrado"
        self.data = datetime.today()
        
    
    def registrarVideoAdicionado(self, videoId):
        self.usuario = current_user.email
        self.acao = "Video adicionado, id: " + videoId
        self.data = datetime.today()
        db.create("registro", self)
    
    def registrarVideoExcluido(self, videoId):
        self.usuario = current_user.email
        self.acao = "Video excluido, id: " + videoId
        self.data = datetime.today()
        db.create("registro", self)
    
    def registrarVideoAtualizado(self, estadoAnterior, estadoAtual):
        self.usuario = current_user.email
        self.acao = "Video editado, id: " + estadoAtual['geral']['id']
        self.estadoAnterior = estadoAnterior
        self.estadoAtual = estadoAtual
        self.data = datetime.today()
        db.create("registro", self)

    def get_as_json(self):
        return self.__dict__


    