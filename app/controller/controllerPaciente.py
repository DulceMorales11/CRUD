from random import sample
from conexionBD import *  #Importando conexion BD



#Creando una funcion para obtener la lista de carros.
def listaPaciente():
    conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
    cur      = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM pacientes ORDER BY id DESC"
    cur.execute(querySQL) 
    resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
    totalBusqueda = len(resultadoBusqueda) #Total de busqueda
    
    cur.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD    
    return resultadoBusqueda




def updatePaciente(id=''):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM pacientes WHERE id = %s LIMIT 1", [id])
        resultQueryData = cursor.fetchone() #Devolviendo solo 1 registro
        return resultQueryData
    
    
    
def registrarPaciente(nombre='', apellido_paterno='', apellido_materno='', edad='', direccion='', codigo_postal='', telefono='', tipo_sangre='', fecha_nacimiento='' ):       
        conexion_MySQLdb = connectionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
            
        sql         = ("INSERT INTO pacientes(nombre, apellido_paterno, apellido_materno, edad, direccion, codigo_postal, telefono, tipo_sangre, fecha_nacimiento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        valores     = (nombre, apellido_paterno, apellido_materno, edad, direccion, codigo_postal, telefono, tipo_sangre, fecha_nacimiento )
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        
        resultado_insert = cursor.rowcount #retorna 1 o 0
        ultimo_id        = cursor.lastrowid #retorna el id del ultimo registro
        return resultado_insert
  

def detallesdelPaciente(id):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM pacientes WHERE id ='%s'" % (id))
        resultadoQuery = cursor.fetchone()
        cursor.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        
        return resultadoQuery
    
    

def  recibeActualizarPaciente(nombre, apellido_paterno, apellido_materno, edad, direccion, codigo_postal, telefono, tipo_sangre, fecha_nacimiento, id):
        conexion_MySQLdb = connectionBD()
        cur = conexion_MySQLdb.cursor(dictionary=True)
        cur.execute("""
            UPDATE pacientes
            SET 
                nombre           = %s,
                apellido_paterno = %s,
                apellido_materno = %s,
                edad             = %s,
                direccion        = %s,
                codigo_postal    = %s,
                telefono         = %s,
                tipo_sangre      = %s,
                fecha_nacimiento = %s 
                WHERE id=%s
            """, (nombre, apellido_paterno, apellido_materno, edad, direccion, codigo_postal, telefono, tipo_sangre, fecha_nacimiento, id))
        conexion_MySQLdb.commit()
        
        cur.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        resultado_update = cur.rowcount #retorna 1 o 0
        return resultado_update
 

#Crear un string aleatorio para renombrar la foto 
# y evitar que exista una foto con el mismo nombre
#def stringAleatorio():
    #string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    #longitud         = 30
    #secuencia        = string_aleatorio.upper()
    #resultado_aleatorio  = sample(secuencia, longitud)
    #string_aleatorio     = "".join(resultado_aleatorio)
    #return string_aleatorio