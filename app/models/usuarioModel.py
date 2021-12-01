from flask_login import LoginManager, UserMixin
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    user = User.get(user_id)
    return user

class User(object):
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
    

    def get_as_json(self):
        return self.__dict__

    @property
    def is_authenticated(self):
        return True

    
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    
    def get_id(self):
        query = db.filtrar('users', {"email": self.email})
        user_bd = query[0]
        return str(user_bd['email'])

    @staticmethod
    def get(user_id):
        query = db.filtrar('users', {"email": user_id})
        if query:
            user_bd = query[0]
            user = User(user_bd['name'], user_bd['email'], user_bd['password'])
        else:
            user = None
        return user

