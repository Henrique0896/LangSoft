from ..models.tables import Registro
from datetime import datetime
from flask_login import current_user
from app import db

class Registrar():
    def usuario():
        registroUsuario = Registro(current_user.email, "Novo usuário registrado", datetime.today())
        db.create("registro", registroUsuario)