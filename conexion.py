
import sqlite3
def conectar():
    miconexion=sqlite3.connect("cruddb")
    cursor=miconexion.cursor()
    try:
        sql="""
        CREATE TABLE IF NOT EXISTS personas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dni TEXT NOT NULL UNIQUE,
            edad INTEGER,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            direccion TEXT DEFAULT "no tiene",
            correo TEXT NOT NULL UNIQUE
        )
        """
        cursor.execute(sql)
        
        return miconexion
    
    except Exception as ex:
        print("Error de conexion:",ex)
        
    finally:
        cursor.close()