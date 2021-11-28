from app import app, db
from flask import render_template, Response
from flask_login import login_required
from bson import json_util
import json
import copy
from app.models.constants.keys import keys
from app.models.services.youtubeService import Youtube
from app.models.learningObjectModel import LearningObject
from app.models.registroModel import Registro

# Listar vídeos salvos no sistema
@app.route("/api/lista", methods=['GET'])
def lista():
    videos = db.list("learningObject")
    if (len(videos) == 0):
        return ({"success :": False, "message": "Nao existe nenhum registro para a consulta"})
    else:
        return Response(json.dumps(videos, default=json_util.default, ensure_ascii=False), content_type="application/json; charset=utf-8")


# Listar títulos dos vídeos
@app.route("/api/titulos", methods=['GET'])
def titulos():
    videos = db.list("learningObject")
    titulos = []
    if (len(videos) == 0):
        return ({"success :": False, "message": "Nao existe nenhum registro para a consulta"})
    for video in videos:
        titulos.append(video["geral"]["titulo"])
    return Response(json.dumps(titulos, default=json_util.default, ensure_ascii=False), content_type="application/json; charset=utf-8")


# Pesquisar informações sobre um vídeo adicionado no sistema
@app.route("/api/consulta/<campo>/<termo>", methods=['GET'])
def consulta(campo, termo):
    informacoes = []
    if (campo not in keys):
        return ({"success": False, "message": "Campo inexistente"})
    for subCampo in keys[campo].values():
        resultado = db.filter_by('learningObject', {subCampo: termo})
        informacoes.append(json.dumps(resultado, default=json_util.default,
        ensure_ascii=False)) if (len(resultado)) != 0 else None
    if (len(informacoes) < 1):
        return ({"success :": False, "message": "Nao existe nenhum registro para a consulta"})
    else:
        return Response(informacoes, content_type="application/json; charset=utf-8")


# Adicionar vídeo ao sistema
@app.route("/api/adicionar/<videoId>", methods=['GET', 'POST'])
def adicionarApi(videoId):
    try:
        youtube = Youtube()
        video = youtube.retornarVideo(videoId)
        learningObject = LearningObject(video)
        db.create("learningObject", learningObject)
        reg = Registro()
        reg.registrarVideoAdicionado(videoId, True)
    except:
        return ({"success:": False, "message": "Nao foi possível realizar a operação"})
    return Response({"success": True}, content_type="application/json; charset=utf-8")


# Deletar vídeo do sistema
@app.route("/api/excluir/<videoId>/", methods=['GET', 'POST'])
def excluirVideoApi(videoId):
    try:
        [video] = db.filter_by('learningObject', {"geral.id": videoId})
        db.delete("learningObject", video)
        reg = Registro()
        reg.registrarVideoExcluido(videoId, True)
        return Response({"success": True}, content_type="application/json; charset=utf-8")
    except:
        return {"success": "false", "message": "Falha ao executar operação"}


# Editar vídeo salvo no sistema
@app.route("/api/editar/<videoId>/<campo>/<dados>", methods=['GET', 'POST'])
def editarVideoApi(videoId, campo, dados):
    try:
        if campo == "geral-id": raise Exception
        [video] = db.filter_by('learningObject', {"geral.id": videoId})
        videoAntigo = copy.deepcopy(video)
        secoes = str.split(campo, "-")
        if len(secoes) == 2:
            video[secoes[0]][secoes[1]] = dados
        elif len(secoes) == 3:
            video[secoes[0]][secoes[1]][secoes[2]] = dados
        else: raise Exception
        db.update("learningObject", video)
        reg = Registro()
        reg.registrarVideoAtualizado(videoAntigo, video, True)
        return Response({"success": True}, content_type="application/json; charset=utf-8")
    except:
        return ({"success:": False, "message": "Nao foi possível realizar a operação de atualização"})


# Retornar objeto de alteção
@app.route("/api/registro-alteracao/<registroId>", methods=['GET'])
@login_required
def retornarRegistroAlteracao(registroId):
    try:
        video = db.read('registro', registroId)
        return Response(json.dumps(video, default=json_util.default, ensure_ascii=False), content_type="application/json; charset=utf-8")
    except:
        return {"success": "false", "message": "Falha ao executar operacao"}
   
# Mostrar Documentação da API
@app.route("/doc-api", methods=['GET'])
@login_required
def documentacaoApi():
    return render_template('doc-api.html')



# Pesquisar video
@app.route("/api/lom/<termo>", methods=['GET'])
@login_required
def LomApi(termo):
    video = None
    youtube = Youtube()
    try:
        video = youtube.retornarVideo(termo)
        learningObject = LearningObject(video)
        db.create("learningObject", learningObject)
    except Exception as e:
        return {"ERRO"}
    return "ok"

# Pesquisar video
@app.route("/api/youtube/<termo>", methods=['GET'])
@login_required
def pesquisarApi(termo):
    video = None
    youtube = Youtube()
    try:
        video = youtube.retornarVideo(termo)
    except Exception as e:
        return {"ERRO"}
    return Response(json.dumps(video, default=json_util.default, ensure_ascii=False), content_type="application/json; charset=utf-8")


