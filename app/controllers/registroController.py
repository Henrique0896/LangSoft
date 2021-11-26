from app import app, db
from flask import render_template
from flask_login import login_required

# Mostrar histórico de registros
@app.route("/registros", methods=['GET'])
@login_required
def mostrarRegistros():
    try:
        registros = db.list("registro")
    except: 
        registros = None
    return render_template('registros.html', registros=registros)
