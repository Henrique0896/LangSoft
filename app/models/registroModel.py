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
        db.inserir("registro", self)
    
    def registrarUsuarioAtualizado(self, estadoAnterior, estadoAtual):
        self.usuario = current_user.email
        self.acao = "Usuário editado"
        self.estadoAnterior = estadoAnterior
        self.estadoAtual = estadoAtual
        self.data = datetime.today()
        del self.estadoAnterior['password']
        del self.estadoAtual['password']
        db.inserir("registro", self)
    
    def registrarUsuarioExcluido(self):
        self.usuario = current_user.email
        self.acao = "Usuário excluido"
        self.data = datetime.today()
        db.inserir("registro", self)
    
    def registrarVideoAdicionado(self, videoId, api=False):
        if api:
            mensagem = " usando a api"
        else:
            mensagem = ""
        self.usuario = current_user.email
        self.acao = "Video adicionado" + mensagem + ", id: " + videoId
        self.data = datetime.today()
        db.inserir("registro", self)
    
    def registrarVideoExcluido(self, videoId, api=False):
        if api:
            mensagem = " usando a api"
        else:
            mensagem = ""
        self.usuario = current_user.email
        self.acao = "Video excluido" + mensagem + ", id: " + videoId
        self.data = datetime.today()
        db.inserir("registro", self)
    
    def registrarVideoAtualizado(self, estadoAnterior, estadoAtual, api=False):
        if api:
            mensagem = " usando a api"
        else:
            mensagem = ""
        self.usuario = current_user.email
        self.acao = "Video editado" + mensagem + ", id: " + str(estadoAtual['_id'])
        self.estadoAnterior = estadoAnterior
        self.estadoAtual = estadoAtual
        self.data = datetime.today()
        db.inserir("registro", self)

    def get_as_json(self):
        return self.__dict__


    