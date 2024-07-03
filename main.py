
import PersonaDatos as per

# #INSERTAR UNA PERSONA
# persona={
#          "dni":"123465",
#          "edad":24,
#          "nombre":"juan",
#          "apellido":"Perex",
#          "direccion":"Indios Verdes 201",
#          "correo":"ja2@hotma3il.com"}

# res=per.save(persona)
# print(res)

# QUERY DE TODAS LAS PERSONAS
res=per.FindAll()
print(res.get('Personas'))

# QUERY BUSCAR UNA SOLA PERSONA A TRAVES DEL DNI
# res=per.Find("1234")
# print(res)

# #ACTUALIZAR DATOS DE PERSONA
# persona = {'dni': '12345', 'edad': 24, 'nombre': 'JUNITO',
#           'apellido': 'GOD', 'direccion': 'Indios Verdes 666', 
#           'correo': 'a@hotmail.coam'}
# res=per.Update(persona)
# print(res)
# res3=per.Find("12345")
# print(res3)

# #DELETE
# res=per.Delete(1)
# print(res)

