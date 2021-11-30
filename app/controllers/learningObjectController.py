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
    videos = db.list("learningObject")
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
        except Exception as e:
            flash("Erro ao buscar informações sobre vídeos na api: " + e.args)
    return render_template('adicionar.html', form=form, videos=videos)

# Adicionar vídeo ao sistema
@app.route("/adicionar/<videoId>", methods=['POST', 'GET'])
@login_required
def adicionarVideo(videoId):
    youtube = Youtube()
    video = None
    try:
        video = youtube.retornarVideo(videoId)
    except Exception as e:
        flash("Erro ao buscar informações sobre vídeos na api: " + e.args )
    learningObject = LearningObject(video)
    db.inserir("learningObject", learningObject)
    reg = Registro()
    reg.registrarVideoAdicionado(videoId)
    return render_template('adicionado.html', tituloVideo=learningObject.geral['titulo'])

# Deletar vídeo do sistema
@app.route("/excluir/<objetoId>", methods=['DELETE', 'GET'])
@login_required
def excluirVideo(objetoId):
    objetoAprendizagem = db.buscarObjeto('learningObject', objetoId)
    db.delete("learningObject", objetoAprendizagem)
    reg = Registro()
    reg.registrarVideoExcluido(objetoId)
    return render_template('removido.html', tituloVideo=video['geral']['titulo'])


# Listar informações do video no sistema
@app.route("/listar/<videoId>", methods=['GET'])
@login_required
def listarVideo(videoId):
    try:
        [video] = db.filter_by('learningObject', {"geral.id": videoId})
    except:
        flash("Video não encontrado")
        return redirect(url_for("errorPage"))
    return render_template('listar.html', video=video, videoId=videoId)


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

# Editar vídeo salvo no sistema
@app.route("/editar/<videoId>", methods=['GET', 'POST'])
@login_required
def editar(videoId):
    [video] = db.filter_by('learningObject', {"geral.id": videoId})
    videoAntigo = copy.deepcopy(video)
    form = updateGeral()
    if form.validate_on_submit():
        video = ManipulacaoForm.atualizarObjeto(form, video)
        db.update("learningObject", video)
        reg = Registro()
        reg.registrarVideoAtualizado(videoAntigo, video)
        return redirect(url_for("listarVideo", videoId=videoId))
    else:
        form = ManipulacaoForm.preencher(form, video)
    return render_template('atualizar.html', video=video, form=form)