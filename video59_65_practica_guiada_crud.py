from tkinter import *
from tkinter import messagebox
import sqlite3

#  SOBERANÍA DE RUTA
RUTA_BBDD = r"E:\Descargas\ESTUDIO\PROGRAMACION\Base_Practica_Juan"

root = Tk()
root.title("Práctica Guiada BBDD - Búnker")

# --- FUNCIONES LÓGICAS ---

def conexionBBDD():
    miConexion = sqlite3.connect(RUTA_BBDD)
    miCursor = miConexion.cursor()
    try:
        miCursor.execute('''CREATE TABLE DATOS_USUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50), PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(50), DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))''')
        messagebox.showinfo("BBDD", "BBDD creada con éxito")
    except:
        messagebox.showwarning("¡Atención!", "La BBDD ya existe")
    miConexion.close()

def salirAplicacion():
    valor = messagebox.askquestion("Salir", "¿Deseas salir del búnker?")
    if valor == "yes":
        root.destroy()

def limpiarCampos():
    miId.set(""); miNombre.set(""); miApellido.set(""); miPass.set(""); miDireccion.set("")
    textoComentario.delete("1.0", END)

def crear():
    miConexion = sqlite3.connect(RUTA_BBDD)
    miCursor = miConexion.cursor()
    datos = (miNombre.get(), miPass.get(), miApellido.get(), miDireccion.get(), textoComentario.get("1.0", END))
    miCursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL,?,?,?,?,?)", (datos))
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro insertado con éxito")
    limpiarCampos()
    miConexion.close()

def leer():
    miConexion = sqlite3.connect(RUTA_BBDD)
    miCursor = miConexion.cursor()
    try:
        miCursor.execute(f"SELECT * FROM DATOS_USUARIOS WHERE ID={miId.get()}")
        elUsuario = miCursor.fetchall()
        for usuario in elUsuario:
            miId.set(usuario[0]); miNombre.set(usuario[1]); miPass.set(usuario[2])
            miApellido.set(usuario[3]); miDireccion.set(usuario[4])
            textoComentario.delete("1.0", END)
            textoComentario.insert("1.0", usuario[5])
        miConexion.commit()
    except:
        messagebox.showerror("Error", "ID no encontrado")
    miConexion.close()

def actualizar():
    miConexion = sqlite3.connect(RUTA_BBDD)
    miCursor = miConexion.cursor()
    datos = (miNombre.get(), miPass.get(), miApellido.get(), miDireccion.get(), textoComentario.get("1.0", END))
    miCursor.execute(f"UPDATE DATOS_USUARIOS SET NOMBRE=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=? WHERE ID={miId.get()}", (datos))
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro actualizado")
    miConexion.close()

def eliminar():
    miConexion = sqlite3.connect(RUTA_BBDD)
    miCursor = miConexion.cursor()
    try:
        miCursor.execute(f"DELETE FROM DATOS_USUARIOS WHERE ID={miId.get()}")
        miConexion.commit()
        messagebox.showinfo("BBDD", "Registro borrado")
        limpiarCampos()
    except:
        messagebox.showerror("Error", "No se pudo eliminar")
    miConexion.close()

# --- INTERFAZ ---
barraMenu = Menu(root)
root.config(menu=barraMenu)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Limpiar campos", command=limpiarCampos)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# --- CAMPOS ---
miFrame = Frame(root)
miFrame.pack()

miId, miNombre, miPass, miApellido, miDireccion = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()

Label(miFrame, text="Id:").grid(row=0, column=0, sticky="e", padx=10, pady=10)
Entry(miFrame, textvariable=miId).grid(row=0, column=1, padx=10, pady=10)

Label(miFrame, text="Nombre:").grid(row=1, column=0, sticky="e", padx=10, pady=10)
cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

Label(miFrame, text="Password:").grid(row=2, column=0, sticky="e", padx=10, pady=10)
Entry(miFrame, textvariable=miPass, show="*").grid(row=2, column=1, padx=10, pady=10)

Label(miFrame, text="Apellido:").grid(row=3, column=0, sticky="e", padx=10, pady=10)
Entry(miFrame, textvariable=miApellido).grid(row=3, column=1, padx=10, pady=10)

Label(miFrame, text="Dirección:").grid(row=4, column=0, sticky="e", padx=10, pady=10)
Entry(miFrame, textvariable=miDireccion).grid(row=4, column=1, padx=10, pady=10)

Label(miFrame, text="Comentarios:").grid(row=5, column=0, sticky="e", padx=10, pady=10)
textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)


scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

# --- BOTONES ---
miFrame2 = Frame(root)
miFrame2.pack()
Button(miFrame2, text="Create", command=crear).grid(row=0, column=0, padx=10, pady=10)
Button(miFrame2, text="Read", command=leer).grid(row=0, column=1, padx=10, pady=10)
Button(miFrame2, text="Update", command=actualizar).grid(row=0, column=2, padx=10, pady=10)
Button(miFrame2, text="Delete", command=eliminar).grid(row=0, column=3, padx=10, pady=10)

root.mainloop()
