from tkinter import *
from tkinter import ttk # se tiene que importat ttk
from tkinter import messagebox
import PersonaDatos as crud

#crear ventana
v=Tk()
v.title("Aplicacion con Base de Datos")
#Poner la ventana en el centro
ancho=1150
alto=500
x_v=v.winfo_screenwidth() //2- ancho//2
y_v=v.winfo_screenheight()//2-alto//2
pos=str(ancho)+"x"+str(alto)+"+"+str(x_v)+"+"+str(y_v)
v.geometry(pos)

# #no dimensionar
# v.resizable(0,0)
# #Que este del tamaño de la patanalla
# v.state("zoomed")

v.configure(bg="#fff")


######## VARIABLES ##########
txt_id= StringVar()
txt_dni= StringVar()
txt_nombre= StringVar()
txt_apellido= StringVar()
txt_direccion= StringVar()
txt_correo= StringVar()
txt_edad= StringVar()

######## FUNCIONES ##########
def creditos():
    messagebox.showinfo("Creditos",
                        """
                        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                        Creado por : Juan Carlos Zuñiga Perez
                        Ingeniero en Control y Automatizacion
                        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                    Gracias por ver
                                        ♥♥♥♥♥♥
                        """)
    
def salir():
    res=messagebox.askquestion("Salir","¿Desea salir de la aplicacion?")
    if res =='yes':
        v.destroy()
        
def llenartabla():
    tabla.delete(*tabla.get_children())
    res=crud.FindAll()
    personas=res.get("Personas")
    #la variable personas retorna una lista con tuplas 
    #en su interior por lo que al iterarla , estamos,
    #iterando una lista
    for fila in personas:
        row=list(fila)
        row.pop(0)
        row=tuple(row)
        tabla.insert("",END,text=id,values=row)

def limpiarcampos():
    txt_edad.set("")
    txt_apellido.set("")
    txt_nombre.set("")
    txt_dni.set("")
    txt_direccion.set("")
    txt_correo.set("")
    e_dni.focus()

def guardar():
    if txt_edad.get().isnumeric():
        per={"dni":txt_dni.get(),"edad":int(txt_edad.get()),"nombre":txt_nombre.get(),
             "apellido":txt_apellido.get(),"direccion":txt_direccion.get(),"correo":txt_correo.get()}
        res=crud.save(per)
        
        if res.get("respuesta"):
            llenartabla()
            messagebox.showinfo("OK",res.get("mensaje"))
            limpiarcampos()
        else:
             messagebox.showerror("ERROR",res.get("mensaje"))
    else:
        txt_edad.set("")
        e_edad.focus()
        messagebox.showerror("ERROR","La edad debe ser numerica")
        

def consultar():
    if txt_dni.get()!="":
        res= crud.Find(txt_dni.get())
        if res.get("respuesta"):
            persona=res.get("Persona")
            txt_nombre.set(persona.get("nombre"))
            txt_apellido.set(persona.get("apellido"))
            txt_edad.set(persona.get("edad"))
            txt_direccion.set(persona.get("direccion"))
            txt_correo.set(persona.get("correo"))
        else:
            e_dni.focus()
            limpiarcampos()
            messagebox.showerror("ERROR","No eixste la persona")
    else:
        e_dni.focus()
        limpiarcampos()
        messagebox.showerror("ERROR","No eixste la persona")
        
        
def actualizar():
    if txt_edad.get().isnumeric():
        per={"dni":txt_dni.get(),"edad":int(txt_edad.get()),"nombre":txt_nombre.get(),
             "apellido":txt_apellido.get(),"direccion":txt_direccion.get(),"correo":txt_correo.get()}
        res=crud.Update(per)
        
        if res.get("Respuesta"):
            llenartabla()
            messagebox.showinfo("OK",res.get("mensaje"))
            limpiarcampos()
        else:
             messagebox.showerror("ERROR",res.get("mensaje"))
    else:
        txt_edad.set("")
        e_edad.focus()
        messagebox.showerror("ERROR","La edad debe ser numerica")
                   
######## FIN FUNCIONES ##########


######## GUI #########
#AGREGAR CUADROS
fuente=("Verdana",12)
Label(v,text="DNI:",anchor="w",justify="left",width=10,bg="lightgreen",font=fuente).grid(row=0,column=0,padx=10,pady=10)
Label(v,text="Nombre:",anchor="w",justify="left",width=10,bg="#fff",font=fuente).grid(row=1,column=0,padx=10,pady=10)
Label(v,text="Apellido:",anchor="w",justify="left",width=10,bg="#fff",font=fuente).grid(row=2,column=0,padx=10,pady=10)
Label(v,text="Direccion:",anchor="w",justify="left",width=10,bg="#fff",font=fuente).grid(row=3,column=0,padx=10,pady=10)
Label(v,text="Correo:",anchor="w",justify="left",width=10,bg="#fff",font=fuente).grid(row=4,column=0,padx=10,pady=10)
Label(v,text="Edad:",anchor="w",justify="left",width=10,bg="#fff",font=fuente).grid(row=5,column=0,padx=10,pady=10)

#AGREGAR CUADROS DE INPUTS

e_dni=ttk.Entry(v,font=fuente,textvariable=txt_dni)
e_nombre=ttk.Entry(v,font=fuente,textvariable=txt_nombre)
e_apellido=ttk.Entry(v,font=fuente,textvariable=txt_apellido)
e_direccion=ttk.Entry(v,font=fuente,textvariable=txt_direccion)
e_correo=ttk.Entry(v,font=fuente,textvariable=txt_correo)
e_edad=ttk.Entry(v,font=fuente,textvariable=txt_edad)

e_dni.grid(row=0,column=1)
e_nombre.grid(row=1,column=1)
e_apellido.grid(row=2,column=1)
e_direccion.grid(row=3,column=1)
e_correo.grid(row=4,column=1)
e_edad.grid(row=5,column=1)

e_dni.focus()
e_nombre.focus()
e_apellido.focus()
e_direccion.focus()
e_correo.focus()
e_edad.focus()


iconNew = PhotoImage(file="new.png")
iconsearch = PhotoImage(file="search.png")
iconupdate = PhotoImage(file="update.png")
icondelete = PhotoImage(file="delete.png")

#AGREGAR BOTONES
ttk.Button(v,text="Guardar",command=guardar,image=iconNew,compound=LEFT).place(x=10,y=280)
ttk.Button(v,text="Consultar",command=consultar,image=iconsearch,compound=LEFT).place(x=120,y=280)
ttk.Button(v,text="Actualizar",command=actualizar,image=iconupdate,compound=LEFT).place(x=230,y=280)
ttk.Button(v,text="Eliminar",command=None,image=icondelete,compound=LEFT).place(x=340,y=280)

###TABLA DE DATOS
#TITULO
titulo=Label(v,text="LISTA DE PERSONA",font=("Arial",16),bg="#fff").place(x=700,y=10)
#DECLARAR TABLA
tabla=ttk.Treeview(v)
tabla.place(x=450,y=40)
#DECLARAR COLUMNAS
tabla["columns"]=("DNI","EDAD","NOMBRE","APELLIDO","DIRECCION","CORREO")
tabla.column("#0",width=0,stretch=NO)
tabla.column("DNI",width=100,anchor=CENTER)
tabla.column("EDAD",width=100,anchor=CENTER)
tabla.column("NOMBRE",width=100,anchor=CENTER)
tabla.column("APELLIDO",width=100,anchor=CENTER)
tabla.column("DIRECCION",width=150,anchor=CENTER)
tabla.column("CORREO",width=130,anchor=CENTER)
#ENCABEZADOSDE COLUMNAS
tabla.heading("#0",text="")
tabla.heading("DNI",text="DNI")
tabla.heading("EDAD",text="Edad")
tabla.heading("NOMBRE",text="Nombre")
tabla.heading("APELLIDO",text="Apellido")
tabla.heading("DIRECCION",text="Direccion")
tabla.heading("CORREO",text="Correo")
#MENU #LA PARTE DE HASTA ARRIBA
menuTop=Menu(v)         #barra de menu
m_archivo=Menu(menuTop,tearoff=0)
m_archivo.add_command(label="Creditos",command=creditos)
m_archivo.add_command(label="Salir",command=salir)
menuTop.add_cascade(label="Archivo",menu=m_archivo)

m_limpiar=Menu(menuTop,tearoff=0)
m_limpiar.add_command(label="Limpiar Campos")
menuTop.add_cascade(label="Limpiar",menu=m_limpiar)

m_crud=Menu(menuTop,tearoff=0)
m_crud.add_command(label="Guardar    ",image=iconNew,compound=RIGHT)
m_crud.add_command(label="Consultar  ",image=iconsearch,compound=RIGHT)
m_crud.add_command(label="Actualizar ",image=iconupdate,compound=RIGHT)
m_crud.add_command(label="Eliminar   ",image=icondelete,compound=RIGHT)
menuTop.add_cascade(label="CRUD",menu=m_crud)

v.config(menu=menuTop)

llenartabla()
v.mainloop() #metodo para renderizar los cambios en pantalla


