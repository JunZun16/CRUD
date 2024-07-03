
import conexion as con

def save(persona):

    persona=dict(persona)   #el resultado recibido tiene que ser un dicc
    
    try:
        db=con.conectar()   #nos conectamos para verificar que hay conexion
        cursor=db.cursor()  #generamos el cursos que sirve para modificar la bd

        columnas=tuple(persona.keys())  #estas son las columnas y tienen que estar en una tupla
        valores=tuple(persona.values())  #estos son los valores igual tiene que ser tupla
        sql="""
        INSERT INTO personas {campos} VALUES(?,?,?,?,?,?)
        """.format(campos=columnas) #definimos el formato en el que entraran los valores
        
        cursor.execute(sql,(valores))   #generamos la query
        
        creada=cursor.rowcount>0    #generamos una variable para ver si hemos creado la nueva insercion
        db.commit()           #confirmamos la query  
        
        if creada:
            return{"respuesta":creada,"mensaje":"Persona Registrada"}
        else:
            return{"respuesta":creada,"mensaje":"Persona NO Registrada"}
        
    except Exception as ex: #si no se genera la conexion va mostar un error
        if "UNIQUE" in str(ex) and "dni" in str(ex):
            mensaje="Ya existe una persona con ese dni"
        elif "UNIQUE" in str(ex) and "correo" in str(ex):
            mensaje="Ya existe una persona con ese correo"
        
        else:
            mensaje=str(ex)
        return{"respuesta":False,"mensaje de error":mensaje}
    
    finally:    #al final de todo el proceso siempre va cerrar el cursos y la base
        cursor.close()        #cerramos el cursor
        db.close()            #cerramos el cursor   

def FindAll():
    try:
        db=con.conectar()
        cursor=db.cursor()
        cursor.execute("SELECT * FROM personas")
        personas=cursor.fetchall()
        if personas:
            cursor.close()
            db.close()
            return{"respuesta":True,"Personas":personas,"Mensaje":"Listado de personas"}
        
        else:
            cursor.close()
            db.close()
            return{"respuesta":False,"Personas":personas,"Mensaje":"Listado de personas"}
        
    except Exception as ex:
        cursor.close()
        db.close()
        return{"respuesta":False,"Mensaje":str(ex)}
        
def Find(dni):
    try:
        db=con.conectar()
        #El cursor hace la solicitud para la base
        cursor=db.cursor()
        cursor.execute("SELECT * FROM personas WHERE dni='{dniPersona}'".format(dniPersona=dni))
        dniresultado=cursor.fetchall()
        if dniresultado:
            info=dniresultado[0]
            persona={"id":info[0],"dni":info[1],"edad":info[2],"nombre":info[3],"apellido":info[4],
                     "direccion":info[5],"correo":info[6]}
            cursor.close()
            db.close()
            return{"Mensaje":"Persona Encontrada","respuesta":True,"Persona":persona}
        else:
            cursor.close()
            db.close()
            return{"respuesta":False,"Mensaje":"No existe la persona"}
        
    except Exception as ex:
        cursor.close()
        db.close()
        return{"respuesta":False,"Mensaje":str(ex)}
        
def Update(persona):
    try:
        db=con.conectar()
            #El cursor hace la solicitud para la base
        cursor=db.cursor()
        persona=dict(persona)
        dniPersona=persona.get('dni')
        persona.pop('dni')
        valores=tuple(persona.values())
        sql="""
        UPDATE personas
        SET edad=?,nombre=?,apellido=?,direccion=?,correo=?
        WHERE dni='{dni}'
        """.format(dni=dniPersona)
        cursor.execute(sql,(valores))
        modificada=cursor.rowcount>0
        db.commit()   
        cursor.close()
        db.close()
        if modificada:
            return{"Respuesta":modificada,"mensaje":"Persona Actualizada"}
        else:
            return{"Respuesta":modificada,"mensaje":"No existe persona con ese DNI"}
        
    except Exception as ex:
        if "UNIQUE" in str(ex) and "correo" in str(ex):
            mensaje="Ya existe una persona con ese correo"
        else:
            mensaje=str(ex)
        cursor.close()
        db.close()
        return{"respuesta":False,"Mensaje":str(ex)}

def Delete(idPersona):
    try:
        db=con.conectar()
        cursor=db.cursor()
        
        sql="""
        DELETE FROM personas WHERE id='{id}'
        """.format(id=idPersona)
        
        cursor.execute(sql)
        eliminada=cursor.rowcount>0
        db.commit()   
        cursor.close()
        db.close()
        if eliminada:
            return{"Respuesta":eliminada,"mensaje":"Persona Borrada"}
        else:
            return{"Respuesta":eliminada,"mensaje":"No existe persona con ese ID"}
        
    except Exception as ex:
        cursor.close()
        db.close()
        return{"respuesta":False,"Mensaje de Excepcion":str(ex)}

