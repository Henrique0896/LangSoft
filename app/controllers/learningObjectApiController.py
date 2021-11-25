from app import app
from flask import render_template, redirect, url_for
from app import db
from app.models.keys import keys
from ..models.tables import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from flask_login import login_required
from app.models.learningObject import LearningObject


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


# Mostrar Documentação da API
@app.route("/doc-api", methods=['GET'])
@login_required
def documentacaoApi():

    return render_template('docApi.html')