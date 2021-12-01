from app import app
from flask import render_template, redirect, url_for, flash
from app import db
from app.models.forms.usuarioForm import loginForm, createAccountForm, profileForm
from app.models.usuarioModel import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from app.models.registroModel import Registro
import copy

#Login
@app.route("/login", methods=['GET', 'POST'])
def login():
    if not current_user.is_authenticated:
        error = None
        form = loginForm()
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            try:
                [usuario] = db.filtrar('users', {"email": email})
            except:
                usuario = None
            if usuario:
                is_pass_ok = check_password_hash(usuario['password'], password)
                if is_pass_ok:
                    user = User(usuario['name'], usuario['email'], usuario['password'])
                    login_user(user)
                    return redirect(url_for("index"))
                else:
                    error = 1
            else:
                error = 1
        else:
            pass
        return render_template('login.html', form=form, error=error)
    else:
        return redirect(url_for("index"))


#Logout
@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

    
#Editar o perfil
@app.route("/perfil", methods=['GET', 'POST'])
@login_required
def perfil():
    form = profileForm()
    error = None
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        current_password = form.current_password.data
        new_password = form.new_password.data
        repeat_new_password = form.repeat_new_password.data
        # Saber se email é o mesmo
        query = db.filtrar('users', {"email": email})
        if query:
            user_bd = query[0]
            is_email_used = True
            is_email_same = (user_bd['email'] == current_user.email)
        else:
            is_email_used = False
            is_email_same = False
        if not is_email_used or is_email_same:
            #verificar se a senha atual é igual
            user_bd = db.filtrar('users', {"email": current_user.email})
            user_bd = user_bd[0]
            is_pass_ok = check_password_hash(user_bd['password'], current_password)
            if is_pass_ok:
                if new_password == repeat_new_password:
                    usuarioAntigo = copy.deepcopy(user_bd)
                    user_bd['name'] = name
                    user_bd['password'] = new_password
                    user_bd['email'] = email
                    db.update("users", user_bd)
                    reg = Registro()
                    reg.registrarUsuarioAtualizado(usuarioAntigo, user_bd)
                    return redirect(url_for("index"))
                else:
                    error = 3 # Nova Senha Não coincide
            else:
                error = 2 #Senha atual está errada
        else:
            error = 1 #Email está em uso e não é o mesmo
    else:
        form.name.data = current_user.name
        form.email.data = current_user.email
    
    return render_template('perfil.html', form=form, error=error)

#Criar Conta
@app.route("/createaccount", methods=['GET', 'POST'])
def createAccount():
    if not current_user.is_authenticated:
        error = None
        form = createAccountForm()
        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            password = form.password.data
            password2 = form.repeat_password.data
            query = db.filtrar('users', {"email": email})
            if not query:
                if password == password2:
                    user = User(name, email, password)
                    db.inserir("users", user)
                    login_user(user)
                    reg = Registro()
                    reg.registrarUsuarioCadastrado()
                    return redirect(url_for("index"))
                else:
                    error = 2 #Senhas são diferentes
            else:
                error = 1 #Email já cadastrado
        else:
            pass

        return render_template('criar-conta.html', form=form, error=error)
    else:
        return redirect(url_for("index"))

# Deletar usuário do sistema
@app.route("/excluir-usuario", methods=['DELETE', 'GET'])
@login_required
def excluirUsuario():
    try:
        [usuario] = db.filtrar('users', {"email": current_user.email})
        db.delete("users", usuario)
        reg = Registro()
        reg.registrarUsuarioExcluido()
        usuarioExcluido=True
    except:
        usuarioExcluido=False
    if usuarioExcluido:
        return redirect(url_for("login"))
    else:
        flash("Erro ao excluir usuario")
        return redirect(url_for("perfil"))

@app.route("/erro", methods=['GET'])
@app.errorhandler(404)
def errorPage(e=None):
    return render_template('404.html')
    
@app.errorhandler(401)
def page_not_found(e):
    return redirect(url_for("login"))
