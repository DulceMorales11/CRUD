from  flask import Flask, render_template, request, redirect, url_for, jsonify
from controller.controllerPaciente import *


#Para subir archivo tipo foto al servidor
import os
from werkzeug.utils import secure_filename 


#Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
app = Flask(__name__)
application = app

msg  =''
tipo =''


#Creando mi decorador para el home, el cual retornara la Lista de Carros
@app.route('/', methods=['GET','POST'])
def inicio():
    return render_template('public/layout.html', miData = listaPaciente())


#RUTAS
@app.route('/registrar-paciente', methods=['GET','POST'])
def addPaciente():
    return render_template('public/acciones/add.html')


 
#Registrando nuevo paciente
@app.route('/pacientes', methods=['POST'])
def formAddPacientes():
    if request.method == 'POST':
        nombre               = request.form['Nombre']
        apellido_paterno     = request.form['Apellido_paterno']
        apellido_materno     = request.form['Apellido_materno']
        edad                 = request.form['Edad']
        direccion            = request.form['Direccion']
        codigo_postal        = request.form['Codigo_postal']
        telefono             = request.form['Telefono']
        tipo_sangre          = request.form['Tipo_sangre']
        fecha_nacimiento     = request.form['Fecha_nacimiento']

        resultData = registrarPaciente(nombre, apellido_paterno, apellido_materno, edad, direccion, codigo_postal, telefono, tipo_sangre, fecha_nacimiento)
        
        if(resultData ==1):
            return render_template('public/layout.html', miData = listaPaciente(), msg='El Registro fue un éxito', tipo=1)
    else:
            return render_template('public/layout.html', msg = 'Metodo HTTP incorrecto', tipo=1)   
    #else:
            #return render_template('public/layout.html', msg = 'Debe cargar una foto', tipo=1)
        
    # if(request.files['foto'] !=''):
       # file     = request.files['foto'] #recibiendo el archivo
        # nuevoNombreFile = recibeFoto(file) #Llamado la funcion que procesa la imagen
        
       
            


@app.route('/form-update-paciente/<string:id>', methods=['GET','POST'])
def formViewUpdate(id):
    if request.method == 'GET':
        resultData = updatePaciente(id)
        if resultData:
            return render_template('public/acciones/update.html',  dataInfo = resultData)
        else:
            return render_template('public/layout.html', miData = listaPaciente(), msg = 'El paciente no se encuntra', tipo= 1)
    
    return render_template('public/layout.html', miData = listaPaciente(), msg = 'Metodo HTTP incorrecto', tipo=1)          
 
   
  
@app.route('/ver-detalles-del-paciente/<int:id>', methods=['GET', 'POST'])
def viewDetallePaciente(id):
    msg =''
    if request.method == 'GET':
        resultData = detallesdelPaciente(id) #Funcion que almacena los detalles del carro
        
        if resultData:
            return render_template('public/acciones/view.html', infoPaciente = resultData, msg='Detalles del Paciente', tipo=1)
        else:
            return render_template('public/acciones/layout.html', msg='El paciente no se encuentra', tipo=1)
    return redirect(url_for('inicio'))
    

@app.route('/actualizar-paciente/<string:id>', methods=['POST'])
def  formActualizarPaciente(id):
    if request.method == 'POST':
        nombre               = request.form['Nombre']
        apellido_paterno     = request.form['Apellido_paterno']
        apellido_materno     = request.form['Apellido_materno']
        edad                 = request.form['Edad']
        direccion            = request.form['Direccion']
        codigo_postal        = request.form['Codigo_postal']
        telefono             = request.form['Telefono']
        tipo_sangre          = request.form['Tipo_sangre']
        fecha_nacimiento     = request.form['Fecha_nacimiento']

        resultData = recibeActualizarPaciente (nombre, apellido_paterno, apellido_materno, edad, direccion, codigo_postal, telefono, tipo_sangre, fecha_nacimiento, id)
        return render_template('public/layout.html', miData = listaPaciente(), msg='Datos del paciente actualizados', tipo=1)
    
    else:
            msg ='No se actualizo el registro'
            return render_template('public/layout.html', miData = listaPaciente(), msg='No se pudo actualizar', tipo=1)
        
        
        


#Eliminar paciente
@app.route('/borrar-paciente', methods=['GET', 'POST'])
def formViewBorrarPaciente():
    if request.method == 'POST':
        id         = request.form['id']
        #nombreFoto      = request.form['nombreFoto']
        resultData      = eliminarPaciente(id) #nombreFoto 

        if resultData ==1:
            #Nota: retorno solo un json y no una vista para evitar refescar la vista
            return jsonify([1])
            #return jsonify(["respuesta", 1])
        else: 
            return jsonify([0])




def eliminarPaciente(id=''): #, nombreFoto=''
        
    conexion_MySQLdb = connectionBD() #Hago instancia a mi conexion desde la funcion
    cur              = conexion_MySQLdb.cursor(dictionary=True)
    
    cur.execute('DELETE FROM pacientes WHERE id=%s', (id,))
    conexion_MySQLdb.commit()
    resultado_eliminar = cur.rowcount

    return resultado_eliminar




@app.route ('/descargar_pdf' , methods=['GET'])
def descargar_pdf():
    return render_template ('public/acciones/view.html')
       
  
  
#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('inicio'))
    

    
    
    
if __name__ == "__main__":
    app.run(debug=True, port=4000)
