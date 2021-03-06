from flask import Flask, flash, render_template, redirect, url_for, request, session
from dao.DAOUsuario import DAOUsuario


app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = DAOUsuario()
ruta='/usuario'

@app.route('/')
def principal():
    return render_template('index.html')

@app.route(ruta+'/IniciarSesion/')
def iniciarsesion():
    return render_template('/usuario/verificarusuario.html')

@app.route(ruta+'/Pagina_Alumno/')
def paginaalumno():
    return render_template('/usuario/PaginaAlumno.html')

@app.route(ruta+'/Pagina_Profesor/')
def paginaprofesor():
    return render_template('/usuario/PaginaProfesor.html')

@app.route(ruta+'/')
def index():
    data = db.read(None)

    return render_template('usuario/index.html', data = data)

@app.route(ruta+'/Registrarse/')
def registrarse():
    return render_template('/usuario/registrarse.html')

@app.route(ruta+'/anadirusuario', methods = ['POST', 'GET'])
def anadirusuario():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("Nuevo usuario creado")
        else:
            flash("ERROR, al crear usuario")

        return redirect(url_for('principal'))
    else:
        return redirect(url_for('principal'))



@app.route(ruta+'/verificarusuario', methods = ['POST', 'GET'])
def verificarusuario():
    if request.method == 'POST' and request.form['save']:
        #guardamos los datos que necesitamos para la funcion de dao 
        login = request.form['login']
        clave = request.form['clave']
        #Validamos contrasena y correo y si funciona devuelve numero de fila i
        i=db.CompararDatos(request.form,login=login,clave=clave)
        #Obtenemos el tipo con i
        tipo=db.BuscarTipo(request.form,numero=i)
        if tipo=="('Profesor',)": #Si es un profesor, redireccionamos a la url para profesor
            return redirect(url_for('paginaprofesor'))
            print("Usted es un profesor") #en consola porque aqui no aparece flash
        elif tipo=="('Alumno',)":
            return redirect(url_for('paginaalumno'))
            print("Usted es un alumno") #en consola porque aqui no aparece flash 
        else:
            return redirect(url_for('principal')) #No esta en el sistema, por lo cual lo redirigimos a la principal
            print("Usted no se encuentra registrado") #en consola porque aqui no aparece flash


@app.route(ruta+'/update/<int:id>/')
def update(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('usuario/update.html', data = data)

@app.route(ruta+'/updateusuario', methods = ['POST'])
def updateusuario():
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('Se actualizo correctamente')
        else:
            flash('ERROR en actualizar')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route(ruta+'/delete/<int:id>/')
def delete(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('usuario/delete.html', data = data)

@app.route(ruta+'/deleteusuario', methods = ['POST'])
def deleteusuario():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('Usuario eliminado')
        else:
            flash('ERROR al eliminar')
        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0",debug=True)
