from app import app, db
from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from app.models.constants.keys import keys
from app.models.registroModel import Registro
from app.models.services.youtubeService import Youtube
from app.models.learningObjectModel import LearningObject
from app.models.settings.manipulacaoForm import ManipulacaoForm
from app.models.forms.learningObjectForm import campoPesquisa, filtroDeDados, updateGeral

import copy

# Listar vídeos salvos no sistema
@app.route("/")
@login_required
def index():
    videos = db.list('objetoAprendizagem')
    return render_template('index.html', videos=videos)

# Escolher vídeo a ser adicionado
@app.route("/adicionar", methods=['POST', 'GET'])
@login_required
def adicionar():
    videos = None
    form = campoPesquisa()
    youtube = Youtube()
    if form.validate_on_submit():
        try:
            videos = youtube.buscarListaVideos(form.pesquisa.data)
        except:
            flash("Erro ao buscar informações sobre vídeos na api")
    return render_template('adicionar.html', form=form, videos=videos)

# Adicionar vídeo ao sistema
@app.route("/adicionar/<videoId>", methods=['POST', 'GET'])
@login_required
def adicionarVideo(videoId):
    youtube = Youtube()
    video = None
    try:
        video = youtube.retornarVideo(videoId)
    except:
        flash("Erro ao buscar informações sobre vídeos na api: ")
    learningObject = LearningObject(video)
    db.inserir("objetoAprendizagem", learningObject)
    reg = Registro()
    reg.registrarVideoAdicionado(videoId)
    return render_template('adicionado.html', tituloVideo=learningObject.geral['titulo'])

# Deletar vídeo do sistema
@app.route("/excluir/<objetoId>", methods=['DELETE', 'GET'])
@login_required
def excluirVideo(objetoId):
    objetoAprendizagem = db.buscarObjeto('objetoAprendizagem', objetoId)
    db.delete('objetoAprendizagem', objetoAprendizagem)
    reg = Registro()
    reg.registrarVideoExcluido(objetoId)
    return render_template('removido.html', tituloObjeto=objetoAprendizagem['geral']['titulo'])


# Listar informações do objeto de aprendizagem no sistema
@app.route("/listar/<objetoId>", methods=['GET'])
@login_required
def listarVideo(objetoId):
    try:
        objetoAprendizagem = db.buscarObjeto('objetoAprendizagem', objetoId)
        if not objetoAprendizagem['dados_tecnicos']['localizacao']:
            objetoAprendizagem['dados_tecnicos']['localizacao'] = "http://127.0.0.1:5000/listar/" + objetoId
    except:
        flash("Objeto de aprendizagem não encontrado")
        return redirect(url_for("errorPage"))
    return render_template('listar.html', objeto=objetoAprendizagem, objetoId=objetoId)


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
        campo = form.campo.data
        resultados = []
        for subCampo in keys[campo].values():
            resultado = db.filtrar('objetoAprendizagem', {subCampo: filtro})
            if(resultado):
                resultados.append(resultado)
        for resultado in resultados:
            for video in resultado:
                videos.append(video)
    else:
        pass
    return render_template('pesquisar.html', form=form, videos=videos, filtro=filtro)

# Editar vídeo salvo no sistema
@app.route("/editar/<objetoId>", methods=['GET', 'POST'])
@login_required
def editar(objetoId):
    video = db.buscarObjeto('objetoAprendizagem', objetoId)
    objetoAntigo = copy.deepcopy(video)
    form = updateGeral()
    if form.validate_on_submit():
        video = ManipulacaoForm.atualizarObjeto(form, video)
        db.update('objetoAprendizagem', video)
        reg = Registro()
        reg.registrarVideoAtualizado(objetoAntigo, video)
        return redirect(url_for("listarVideo", objetoId=objetoId))
    else:
        form = ManipulacaoForm.preencher(form, video)
    return render_template('atualizar.html', video=video, form=form)

# Mostrar Documentação dos Objetos de Aprendizagem
@app.route("/doc-oa", methods=['GET'])
@login_required
def documentacaoOa():
    return render_template('doc-oa.html')