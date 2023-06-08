from tkinter import *
import pickle

class Libro:
    def __init__(self, isbn, nombre, editorial, precio):
        self.isbn = isbn
        self.nombre = nombre
        self.editorial = editorial
        self.precio = precio

class Ventana:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Lista de Libros")

        # Crear la lista de libros
        self.lista_libros = []

        # Cargar los libros desde el archivo
        self.cargar_libros()

        # Crear los controles de la interfaz gráfica
        self.etiqueta_isbn = Label(ventana, text="ISBN:")
        self.etiqueta_isbn.place(x = 15, y = 20)

        self.entrada_isbn = Entry(ventana)
        self.entrada_isbn.place(x = 15, y = 50)

        self.etiqueta_nombre = Label(ventana, text="Nombre:")
        self.etiqueta_nombre.place(x = 15, y = 80)

        self.entrada_nombre = Entry(ventana)
        self.entrada_nombre.place(x = 15, y = 110)

        self.etiqueta_editorial = Label(ventana, text="Editorial:")
        self.etiqueta_editorial.place(x = 15, y = 140)

        self.entrada_editorial = Entry(ventana)
        self.entrada_editorial.place(x = 15, y = 170)

        self.etiqueta_precio = Label(ventana, text="Precio:")
        self.etiqueta_precio.place(x = 15, y = 200)

        self.entrada_precio = Entry(ventana)
        self.entrada_precio.place(x = 15, y = 230)

        self.boton_aniadir = Button(ventana, text="Añadir", command=self.aniadir_libro)
        self.boton_aniadir.place(x = 300, y = 110)

        self.boton_listar = Button(ventana, text="Listar", command=self.listar_libros)
        self.boton_listar.place(x = 300, y = 80)

        self.lista_libros_gui = Listbox(ventana)
        self.lista_libros_gui.place(x = 150, y = 20)

        self.boton_modificar = Button(ventana, text="Modificar", command=self.seleccionar_libro)
        self.boton_modificar.place(x = 300, y = 50)

        self.boton_aceptar = Button(ventana, text="Aceptar", command=self.aceptar_modificacion, state=DISABLED)
        self.boton_aceptar.place(x = 300, y = 20)

        # Cerrar la ventana guardando los libros en el archivo
        self.ventana.protocol("WM_DELETE_WINDOW", self.guardar_libros)

        # Variables para almacenar el libro seleccionado
        self.libro_seleccionado = None
        self.indice_seleccionado = None

    def aniadir_libro(self):
        isbn = self.entrada_isbn.get()
        nombre = self.entrada_nombre.get()
        editorial = self.entrada_editorial.get()
        precio = self.entrada_precio.get()
        nuevo_libro = Libro(isbn, nombre, editorial, precio)
        self.lista_libros.append(nuevo_libro)
        self.entrada_isbn.delete(0, END)
        self.entrada_nombre.delete(0, END)
        self.entrada_editorial.delete(0, END)
        self.entrada_precio.delete(0, END)
        print("Libro añadido:", nuevo_libro.nombre)

    def listar_libros(self):
        self.lista_libros_gui.delete(0, END)
        for libro in self.lista_libros:
            self.lista_libros_gui.insert(END, libro.nombre)

    def seleccionar_libro(self):
        seleccion = self.lista_libros_gui.curselection()
        if len(seleccion) > 0:
            self.indice_seleccionado = seleccion[0]
            self.libro_seleccionado = self.lista_libros[self.indice_seleccionado]
            self.entrada_isbn.delete(0, END)
            self.entrada_nombre.delete(0, END)
            self.entrada_editorial.delete(0, END)
            self.entrada_precio.delete(0, END)
            self.entrada_isbn.insert(END, self.libro_seleccionado.isbn)
            self.entrada_nombre.insert(END, self.libro_seleccionado.nombre)
            self.entrada_editorial.insert(END, self.libro_seleccionado.editorial)
            self.entrada_precio.insert(END, self.libro_seleccionado.precio)
            self.boton_aceptar.configure(state=NORMAL)

    def aceptar_modificacion(self):
        isbn = self.entrada_isbn.get()
        nombre = self.entrada_nombre.get()
        editorial = self.entrada_editorial.get()
        precio = self.entrada_precio.get()
        self.libro_seleccionado.isbn = isbn
        self.libro_seleccionado.nombre = nombre
        self.libro_seleccionado.editorial = editorial
        self.libro_seleccionado.precio = precio
        self.lista_libros_gui.delete(self.indice_seleccionado)
        self.lista_libros_gui.insert(self.indice_seleccionado, self.libro_seleccionado.nombre)
        self.boton_aceptar.configure(state=DISABLED)
        print("Libro modificado:", self.libro_seleccionado.nombre)

    def guardar_libros(self):
        with open("libros.pkl", "wb") as archivo:
            pickle.dump(self.lista_libros, archivo)
        self.ventana.destroy()

    def cargar_libros(self):
        try:
            with open("libros.pkl", "rb") as archivo:
                self.lista_libros = pickle.load(archivo)
        except FileNotFoundError:
            print("No se encontró el archivo de libros.")

# Crear la ventana de la aplicación
ventana_principal = Tk()

# Crear la instancia de la aplicación
app = Ventana(ventana_principal)

# Ejecutar la aplicación
ventana_principal.mainloop()
