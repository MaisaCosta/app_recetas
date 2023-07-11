from flask import  render_template, request, session, redirect 
from app_recetas import app

@app.route( '/recetas', methods = ['GET'] )
def desplegar_recetas():
    return render_template( 'recetas.html')

@app.route('/formulario/receta', methods = ['GET'] )
def desplegar_formulario_receta():
    return render_template('formulario_receta.html' )

@app.route('/crear/receta', methods = ['POST'] )
def nueva_receta():
    return render_template('formulario_receta.html' )
    data = {
        **request.form,
        "id_usuario" : session('id_usuario' )
    }
    id_receta = Receta.crear_uno( data)
    return redirect('/recetas')