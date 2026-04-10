from tkinter import *
from tkinter import messagebox
import sqlite3
import hashlib

# 🛰️ SOBERANÍA DE RUTA
RUTA_BBDD = r"E:\Descargas\ESTUDIO\PROGRAMACION\Base_Practica_Juan"

# --- MOTOR DE DATOS (BACK-END) ---

def consulta(query, parametros=(), mensaje_exito=None):
    """Función Maestra: Centraliza la conexión y asegura el cierre del búnker"""
    try:
        with sqlite3.connect(RUTA_BBDD) as con:
            cursor = con.cursor()
            resultado = cursor.execute(query, parametros)
            con.commit()
            if mensaje_exito: messagebox.showinfo("Búnker", mensaje_exito)
            return resultado.fetchall()
    except Exception as e:
        messagebox.showerror("Error de Sistema", f"Fallo en la operación: {e}")
    return None

def encriptar_pass(password):
    """Transforma la entrada humana en un Hash SHA-256 indescifrable"""
    return hashlib.sha256(password.encode()).hexdigest()

def conexionBBDD():
    sql = '''CREATE TABLE IF NOT EXISTS DATOS_USUARIOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(50), 
        PASSWORD VARCHAR(64), APELLIDO VARCHAR(50), 
        DIRECCION VARCHAR(50), COMENTARIOS VARCHAR(100))'''
    consulta(sql, mensaje_exito="BBDD Conectada con Éxito")

def limpiarCampos():
    """Higiene de Datos: Resetea todos los campos para evitar basura"""
    for var in [miId, miNombre, miPass, miApellido, miDireccion]: var.set("")
    textoComentario.delete("1.0", END)

def ejecutar_crud(tipo):
    """Controlador Único de Operaciones CRUD"""
    # Empaquetado de datos para el búnker (Encriptamos al crear o actualizar)
    p_hash = encriptar_pass(miPass.get())
    datos = (miNombre.get(), p_hash, miApellido.get(), miDireccion.get(), textoComentario.get("1.0", END))
    
    if tipo == "crear":
        consulta("INSERT INTO DATOS_USUARIOS VALUES(NULL,?,?,?,?,?)", datos, "Registro Blindado")
        limpiarCampos()
    elif tipo == "leer":
        res = consulta(f"SELECT * FROM DATOS_USUARIOS WHERE ID={miId.get()}")
        if res:
            res = res[0] # Extraemos la primera fila
            variables = [miId, miNombre, miPass, miApellido, miDireccion]
            for i, var in enumerate(variables):
                if i == 2: # Si es el campo Password
                    var.set("********") # Higiene visual: No mostramos el Hash
                else:
                    var.set(res[i])
            textoComentario.delete("1.0", END)
            textoComentario.insert("1.0", res[5])
    elif tipo == "actualizar":
        consulta(f"UPDATE DATOS_USUARIOS SET NOMBRE=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=? WHERE ID={miId.get()}", datos, "Registro Actualizado")
    elif tipo == "borrar":
        if messagebox.askquestion("BBDD", "¿Confirmas la purga del registro?") == "yes":
            consulta(f"DELETE FROM DATOS_USUARIOS WHERE ID={miId.get()}", mensaje_exito="Registro Eliminado")
            limpiarCampos()

# --- INTERFAZ DE USUARIO (FRONT-END) ---

root = Tk()
root.title("Gestor de Sabiduría - Rango SSS")

# 1. ARQUITECTURA DE MENÚS DINÁMICOS (Eficiencia total)
config_menus = {
    "BBDD": {"Conectar": conexionBBDD, "Salir": lambda: root.destroy() if messagebox.askquestion("Salir", "¿Deseas salir?")=="yes" else None},
    "Edición": {"Limpiar Campos": limpiarCampos},
    "CRUD": {
        "Crear": lambda: ejecutar_crud("crear"),
        "Leer": lambda: ejecutar_crud("leer"),
        "Actualizar": lambda: ejecutar_crud("actualizar"),
        "Borrar": lambda: ejecutar_crud("borrar")
    },
    "Ayuda": {"Acerca de...": lambda: messagebox.showinfo("Búnker", "Versión 2026 - Arquitectura SSS")}
}

barraMenu = Menu(root)
root.config(menu=barraMenu)

for nombre, opciones in config_menus.items():
    menu_obj = Menu(barraMenu, tearoff=0) # tearoff=0 centralizado aquí
    barraMenu.add_cascade(label=nombre, menu=menu_obj)
    for etiqueta, comando in opciones.items():
        menu_obj.add_command(label=etiqueta, command=comando)

# 2. CAMPOS Y GRID (Con correcciones estéticas de Juan)
miFrame = Frame(root); miFrame.pack(padx=20, pady=20)
miId, miNombre, miPass, miApellido, miDireccion = [StringVar() for _ in range(5)]

# Tupla: (Etiqueta, Variable, Caracter_Show, Es_Nombre)
campos = [
    ("Id:", miId, None, False), 
    ("Nombre:", miNombre, None, True), 
    ("Pass:", miPass, "*", False), 
    ("Apellido:", miApellido, None, False), 
    ("Dirección:", miDireccion, None, False)
]

for i, (txt, var, char, es_nombre) in enumerate(campos):
    Label(miFrame, text=txt).grid(row=i, column=0, sticky="e", padx=5, pady=5)
    cuadro = Entry(miFrame, textvariable=var, show=char)
    cuadro.grid(row=i, column=1)
    if es_nombre:
        cuadro.config(fg="red", justify="right")

Label(miFrame, text="Comentarios:").grid(row=5, column=0, sticky="e")
textoComentario = Text(miFrame, width=20, height=5)
textoComentario.grid(row=5, column=1, pady=10)
scroll = Scrollbar(miFrame, command=textoComentario.yview); scroll.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scroll.set)

# 3. BOTONERA AUTOMATIZADA
miFrame2 = Frame(root); miFrame2.pack(pady=10)
acciones = [("Create", "crear"), ("Read", "leer"), ("Update", "actualizar"), ("Delete", "borrar")]

for i, (txt, tipo) in enumerate(acciones):
    Button(miFrame2, text=txt, width=8, command=lambda t=tipo: ejecutar_crud(t)).grid(row=0, column=i, padx=5)

root.mainloop()
