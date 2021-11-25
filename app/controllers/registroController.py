from app import app
from flask import render_template
from app import db
from flask_login import login_required

# Mostrar histórico de registros
@app.route("/registros", methods=['GET'])
@login_required
def mostrarRegistros():
    registros = db.list("registro")
    if len(list(registros)) != 0:
        registros = []
        for registro in registros:
            registros.append(registro)
    else:
        registros = None
    return render_template('registros.html', registros=registros)
