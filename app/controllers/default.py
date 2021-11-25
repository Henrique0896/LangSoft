from app import app
from flask import render_template, jsonify, Response, redirect, url_for
from app import db
from app.models.forms import campoPesquisa, filtroDeDados, updateGeral, loginForm, createAccountForm, profileForm
import json
from ..models.tables import User
from .keys import keys
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from bson import json_util
from app.models.registro import Registro
from app.models.youtube import Youtube
from app.models.learningObject import LearningObject


db_registros = db.list("logs")

# # ----------------- API ------------

# # READ
# @app.route("/api/lista", methods=['GET'])
# def lista():
#     query = db.filter_by('learning_object', {})
#     if (len(query) < 1):
#         return ({"success :": False, "message": "Nao existe nenhum registro para a consulta"})
#     return Response(json.dumps(query, default=json_util.default, ensure_ascii=False), content_type="application/json; charset=utf-8")


# # READ TITLES
# @app.route("/api/titulos", methods=['GET'])
# def titulos():
#     query = db.filter_by('learning_object', {})
#     r = []
#     if (len(query) < 1):
#         return ({"success :": False, "message": "Nao existe nenhum registro para a consulta"})
#     for i in query:
#         r.append(i["geral"]["titulo"])
#     return Response(json.dumps(r, default=json_util.default, ensure_ascii=False), content_type="application/json; charset=utf-8")


# # FILTRO
# @app.route("/api/consulta/<campo>/<filtro>", methods=['GET'])
# def consulta(campo, filtro):
#     resultado = []
#     if (campo not in keys):
#         return ({"success": False, "message": "Campo inexistente"})
#     for value in keys[campo].values():
#         query = db.filter_by('learning_object', {value: filtro})
#         resultado.append(json.dumps(query, default=json_util.default,
#                          ensure_ascii=False)) if (len(query)) != 0 else None
#     if (len(resultado) < 1):
#         return ({"success :": False, "message": "Nao existe nenhum registro para a consulta"})
#     return Response(resultado, content_type="application/json; charset=utf-8")


# # CREATE
# @app.route("/api/add/<page>/<pagination>", methods=['GET', 'POST'])
# def add(page, pagination):
#     pages = []
#     for i in [wikipedia.search(page)[int(pagination)]] if str.isdigit(pagination) else wikipedia.search(page):
#         if len(db.filter_by('learning_object', {"geral.titulo": i})) < 1:
#             page = wikipedia.page(i)
#             learning_object = (LearningObject(page))
#             lom = json.dumps(learning_object.get_as_json(),
#                              default=json_util.default, ensure_ascii=False)
#             db.create("learning_object", learning_object)
#             pages.append(lom)
#     return Response({"success": True}, content_type="application/json; charset=utf-8")


# # DELETE
# @app.route("/api/delete/<title>/", methods=['GET', 'POST'])
# def delete(title):
#     page = db.filter_by('learning_object', {"geral.titulo": title})
#     if (len(page) < 1):
#         return {"success": "false", "msg": "Não existe nenhuma pagina salva com este titulo"}
#     else:
#         db.delete("learning_object", page[0])
#     return Response({"success": True}, content_type="application/json; charset=utf-8")


# # UPDATE
# @app.route("/api/update/<title>/<prop>/<data>", methods=['GET', 'POST'])
# def update(title, prop, data):
#     try:
#         page = db.filter_by('learning_object', {"geral.titulo": title})
#         ref = page[0]
#         if (len(page) < 1):
#             return {"success": "false", "msg": "Não existe nenhuma pagina salva com este titulo"}
#         ls = str.split(prop, ".")
#         if( len(ls) == 2 ):
#             fst = ls.pop()
#             for i in ls:
#                 ref = ref[i]
#             ref[fst] = data
#             page[0][ls[0]] = ref
#         elif( len(ls) == 3 ):
#             fst = ls.pop()
#             for i in ls:
#                 ref = ref[i]
#             ref[fst] = data
#             page[0][ls[0]][ls[1]] = ref
#         else: raise Exception

#         db.update("learning_object", page[0])

#         return Response({"success": True}, content_type="application/json; charset=utf-8")
#     except:
#         return Response({"success": False}, content_type="application/json; charset=utf-8")



# # ------------ ROTAS -------------


# Listar vídeos salvos no sistema
@app.route("/")
@login_required
def index():
    videos = db.list("learningObject")
    return render_template('index.html', videos=videos)

# Escolher vídeo a ser adicionado
@app.route("/adicionar", methods=['POST', 'GET'])
@login_required
def adicionar():
    form = campoPesquisa()
    youtube = Youtube()
    videos = None
    if form.validate_on_submit():
        videos = youtube.buscarListaVideos(form.pesquisa.data)
    else:
        pass
    return render_template('adicionar.html', form=form, videos=videos)

# Adicionar vídeo ao sistema
@app.route("/adicionar/<videoId>", methods=['POST', 'GET'])
@login_required
def adicionarVideo(videoId):
    youtube = Youtube()
    video = youtube.retornarVideo(videoId)
    learningObject = LearningObject(video)
    db.create("learningObject", learningObject)
    reg = Registro()
    reg.registrarVideoAdicionado(videoId)
    return render_template('adicionado.html', tituloVideo=learningObject.geral['titulo'])

# Deletar vídeo do sistema
@app.route("/excluir/<videoId>", methods=['DELETE', 'GET'])
@login_required
def excluirVideo(videoId):
    [video] = db.filter_by('learningObject', {"geral.id": videoId})
    db.delete("learningObject", video)
    return render_template('delete/removido.html', tituloVideo=video['geral']['titulo'])


# Listar informações do video no sistema
@app.route("/listar/<videoId>", methods=['GET'])
@login_required
def listarVideo(videoId):
    [video] = db.filter_by('learningObject', {"geral.id": videoId})
    return render_template('read/listar.html', video=video, videoId=videoId)


# Pesquisar informações sobre um vídeo adicionado no sistema
@app.route("/pesquisar", methods=['POST', 'GET'])
@login_required
def pesquisar():
    form = filtroDeDados()
    videos = None
    filtro = None
    if form.validate_on_submit():
        videos = []
        filtro = form.pesquisa.data
        campo = form.subject.data
        resultados = []
        for subCampo in keys[campo].values():
            resultado = db.filter_by('learningObject', {subCampo: filtro})
            if(resultado):
                resultados.append(resultado)
        for resultado in resultados:
            for video in resultado:
                videos.append(video)
    else:
        pass
    return render_template('pesquisar.html', form=form, videos=videos, filtro=filtro)

# Editar Geral
@app.route("/editar/<videoId>", methods=['GET', 'POST'])
@login_required
def editarGeral(videoId):
    [video] = db.filter_by('learningObject', {"geral.id": videoId})
    form = updateGeral()

    if form.validate_on_submit():
        video['geral']['titulo'] = form.titulo.data
        video['geral']['idioma'] = form.idioma.data
        video['geral']['descricao'] = form.descricao.data
        video['geral']['palavras_chave'] = form.palavrasChave.data
        video['geral']['cobertura'] = form.cobertura.data
        video['geral']['estrutura'] = form.estrutura.data
        video['geral']['nivel_de_agregacao'] = form.nivelDeAgregacao.data
        
        video['ciclo_de_vida']['versao'] = form.versao.data
        video['ciclo_de_vida']['status'] = form.status.data
        video['ciclo_de_vida']['contribuinte']['entidade'] = form.entidade.data
        video['ciclo_de_vida']['contribuinte']['data'] = form.data.data
        video['ciclo_de_vida']['contribuinte']['papel'] = form.papel.data
        
        video['meta_metadados']['identificador']['catalogo'] = form.i_catalogo.data
        video['meta_metadados']['identificador']['entrada'] = form.i_entrada.data
        video['meta_metadados']['contribuinte']['entidade'] = form.c_entidade.data
        video['meta_metadados']['contribuinte']['data'] = form.c_data.data
        video['meta_metadados']['contribuinte']['papel'] = form.c_papel.data
        video['meta_metadados']['esquema_de_metadados'] = form.esquema_de_metadados.data
        video['meta_metadados']['idioma'] = form.m_idioma.data
        
        video['metadados_tecnicos']['formato'] = form.m_formato.data
        video['metadados_tecnicos']['tamanho'] = form.m_tamanho.data
        video['metadados_tecnicos']['localizacao'] = form.m_localizacao.data
        video['metadados_tecnicos']['requisitos'] = form.m_requisitos.data
        video['metadados_tecnicos']['observacoes_de_Instalacoes'] = form.m_observacoes_de_Instalacoes.data
        video['metadados_tecnicos']['outros_requisitos_de_sistema'] = form.m_outros_requisitos_de_sistema.data
        video['metadados_tecnicos']['duracao'] = form.m_duracao.data

        video['aspectos_educacionais']['tipo_de_iteratividade'] = form.ae_tipo_de_iteratividade.data
        video['aspectos_educacionais']['tipo_de_recurso_de_aprendizado'] = form.ae_tipo_de_recurso_de_aprendizado.data
        video['aspectos_educacionais']['nivel_de_interatividade'] = form.ae_nivel_de_interatividade.data
        video['aspectos_educacionais']['densidade_semantica'] = form.ae_densidade_semantica.data
        video['aspectos_educacionais']['usuario_final'] = form.ae_usuario_final.data
        video['aspectos_educacionais']['contexto_de_aprendizagem'] = form.ae_contexto_de_aprendizagem.data
        video['aspectos_educacionais']['idade_recomendada'] = form.ae_idade_recomendada.data
        video['aspectos_educacionais']['grau_de_dificuldade'] = form.ae_grau_de_dificuldade.data
        video['aspectos_educacionais']['tempo_de_aprendizado'] = form.ae_tempo_de_aprendizado.data
        video['aspectos_educacionais']['descricao'] = form.ae_descricao.data
        video['aspectos_educacionais']['linguagem'] = form.ae_linguagem.data

        video['direitos']['custo'] = form.d_custo.data
        video['direitos']['direitos_autorais'] = form.d_direitos_autorais.data
        video['direitos']['descricao'] = form.d_descricao.data

        video['relacoes']['genero'] = form.r_genero.data
        video['relacoes']['recurso']['referencias'] = form.r_recurso_referencias.data
        video['relacoes']['recurso']['links_externos'] = form.r_recurso_links_externos.data

        video['classificacao']['finalidade'] = form.c_finalidade.data
        video['classificacao']['diretorio'] = form.c_diretorio.data
        video['classificacao']['descricao'] = form.c_descricao.data
        video['classificacao']['palavra_chave'] = form.c_palavra_chave.data

        video['conteudo']['data'] = form.cont_data.data
        video['conteudo']['entidade'] = form.cont_entidade.data 
        video['conteudo']['imagens'] = form.cont_imagens.data
        video['conteudo']['comentarios'] = form.cont_comentarios.data
          
        db.update("learning_object", video)
        return redirect(url_for("listarVideo", videoId=videoId))
    else:
        form.titulo.data = video['geral']['titulo']
        form.idioma.data = video['geral']['idioma']
        form.descricao.data = video['geral']['descricao']
        form.palavrasChave.data = video['geral']['palavras_chave']
        form.cobertura.data = video['geral']['cobertura']
        form.estrutura.data = video['geral']['estrutura']
        form.nivelDeAgregacao.data = video['geral']['nivel_de_agregacao']

        form.versao.data = video['ciclo_de_vida']['versao']
        form.status.data = video['ciclo_de_vida']['status']
        form.entidade.data = video['ciclo_de_vida']['contribuinte']['entidade']
        form.data.data = video['ciclo_de_vida']['contribuinte']['data']
        form.papel.data = video['ciclo_de_vida']['contribuinte']['papel']

        form.i_catalogo.data = video['meta_metadados']['identificador']['catalogo']
        form.i_entrada.data = video['meta_metadados']['identificador']['entrada']
        form.c_entidade.data = video['meta_metadados']['contribuinte']['entidade']
        form.c_data.data = video['meta_metadados']['contribuinte']['data']
        form.c_papel.data = video['meta_metadados']['contribuinte']['papel']
        form.esquema_de_metadados.data = video['meta_metadados']['esquema_de_metadados']
        form.m_idioma.data = video['meta_metadados']['idioma']

        form.m_formato.data = video['metadados_tecnicos']['formato']
        form.m_tamanho.data = video['metadados_tecnicos']['tamanho']
        form.m_localizacao.data = video['metadados_tecnicos']['localizacao']
        form.m_requisitos.data = video['metadados_tecnicos']['requisitos']
        form.m_observacoes_de_Instalacoes.data = video['metadados_tecnicos']['observacoes_de_Instalacoes']
        form.m_outros_requisitos_de_sistema.data = video['metadados_tecnicos']['outros_requisitos_de_sistema']
        form.m_duracao.data = video['metadados_tecnicos']['duracao']

        form.ae_tipo_de_iteratividade.data = video['aspectos_educacionais']['tipo_de_iteratividade']
        form.ae_tipo_de_recurso_de_aprendizado.data = video['aspectos_educacionais']['tipo_de_recurso_de_aprendizado']
        form.ae_nivel_de_interatividade.data = video['aspectos_educacionais']['nivel_de_interatividade']
        form.ae_densidade_semantica.data = video['aspectos_educacionais']['densidade_semantica']
        form.ae_usuario_final.data = video['aspectos_educacionais']['usuario_final']
        form.ae_contexto_de_aprendizagem.data = video['aspectos_educacionais']['contexto_de_aprendizagem']
        form.ae_idade_recomendada.data = video['aspectos_educacionais']['idade_recomendada']
        form.ae_grau_de_dificuldade.data = video['aspectos_educacionais']['grau_de_dificuldade']
        form.ae_tempo_de_aprendizado.data = video['aspectos_educacionais']['tempo_de_aprendizado']
        form.ae_descricao.data = video['aspectos_educacionais']['descricao']
        form.ae_linguagem.data = video['aspectos_educacionais']['linguagem']

        form.d_custo.data = video['direitos']['custo']
        form.d_direitos_autorais.data = video['direitos']['direitos_autorais']
        form.d_descricao.data = video['direitos']['descricao']

        form.r_genero.data = video['relacoes']['genero']
        form.r_recurso_referencias.data = video['relacoes']['recurso']['referencias']
        form.r_recurso_links_externos.data = video['relacoes']['recurso']['links_externos']

        form.c_finalidade.data = video['classificacao']['finalidade']
        form.c_diretorio.data = video['classificacao']['diretorio']
        form.c_descricao.data = video['classificacao']['descricao']
        form.c_palavra_chave.data = video['classificacao']['palavra_chave']

        form.cont_data.data = video['conteudo']['data']
        form.cont_entidade.data = video['conteudo']['entidade']
        form.cont_imagens.data = video['conteudo']['imagens']
        form.cont_comentarios.data = video['conteudo']['comentarios']

        

    return render_template('update/geral.html', video=video, form=form, videoId=videoId)


# Mostrar histórico
@app.route("/logs", methods=['GET'])
@login_required
def logs():
    global db_registros
    db_registros = db.list("registro")
    if len(list(db_registros)) != 0:
        registros = []
        for registro in db_registros:
            registros.append(registro)
    else:
        registros = None
    return render_template('registros.html', registros=registros)


# Mostrar Documentação da API
@app.route("/doc-api", methods=['GET'])
@login_required
def documentacaoApi():

    return render_template('docApi.html')

#Login
@app.route("/login", methods=['GET', 'POST'])
def login():
    if not current_user.is_authenticated:
        error = None
        form = loginForm()
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            query = db.filter_by('users', {"email": email})
            if query:
                user_bd = query[0]
                is_pass_ok = check_password_hash(user_bd['password'], password)
                if is_pass_ok:
                    user = User(user_bd['name'], user_bd['email'], user_bd['password'])
                    login_user(user)
                    print(user.email)
                    return redirect(url_for("index"))
                else:
                    error = 1
            else:
                error = 1
        else:
            print("Não Validade")
        return render_template('login.html', form=form, error=error)
    else:
        return redirect(url_for("index"))


#Logout
@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

    
#Profile
@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    form = profileForm()
    error = None
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        current_password = form.current_password.data
        new_password = form.new_password.data
        repeat_new_password = form.repeat_new_password.data
        # Saber se email é o mesmo
        query = db.filter_by('users', {"email": email})
        if query:
            user_bd = query[0]
            is_email_used = True
            is_email_same = (user_bd['email'] == current_user.email)
        else:
            is_email_used = False
            is_email_same = False
        if not is_email_used or is_email_same:
            #verificar se a senha atual é igual
            user_bd = db.filter_by('users', {"email": current_user.email})
            user_bd = user_bd[0]
            is_pass_ok = check_password_hash(user_bd['password'], current_password)
            if is_pass_ok:
                if new_password == repeat_new_password:
                    user_bd['name'] = name
                    user_bd['password'] = new_password
                    user_bd['email'] = email

                    
                    db.update("users", user_bd)
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
    
    return render_template('profile.html', form=form, error=error)
    




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
            query = db.filter_by('users', {"email": email})
            if not query:
                if password == password2:
                    user = User(name, email, password)
                    db.create("users", user)
                    login_user(user)
                    Registrar.usuario()
                    return redirect(url_for("index"))
                else:
                    error = 2 #Senhas são diferentes
            else:
                error = 1 #Email já cadastrado
        else:
            pass

        return render_template('register.html', form=form, error=error)
    else:
        return redirect(url_for("index"))
    


@app.errorhandler(404)
def errorPage(e):
    return render_template('404.html')
    


@app.errorhandler(401)
def page_not_found(e):
    return redirect(url_for("login"))
