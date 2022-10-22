#! /usr/bin/env python3
from alumnado import Alumnado
from repositorioAlumnos import RepositorioAlumnado
import tkinter
from tkinter import ttk
from tkinter import messagebox

class Gui():
    '''Crear la pantalla inicial, mostrando todas las notas y botones'''
    def __init__(self):
        self.iniciar_alumnado()
        self.iniciar_gui()

    def iniciar_alumnado(self):
        self.repositorio = RepositorioAlumnado()
        alumnos = self.repositorio.obtener_todo()
        self.alumnado = Alumnado(alumnos)

    def iniciar_gui(self):
        self.ventana_principal = tkinter.Tk()
        self.ventana_principal.title("Alumnado")
        botonAgregar=tkinter.Button(self.ventana_principal,text="Agregar alumno", 
                           command = self.agregar_alumno).grid(row=0, column=0)
        botonModificar=tkinter.Button(self.ventana_principal,text="Modificar",
                           command = self.modificar_alumno).grid(row=0, column=1)
        botonEliminar=tkinter.Button(self.ventana_principal, text = "Eliminar",
                           command = self.eliminar_alumno).grid(row=0, column=2)
        tkinter.Label(self.ventana_principal,text="Buscar").grid(row=1,column=0)
        self.cajaBuscar = tkinter.Entry(self.ventana_principal)
        self.cajaBuscar.grid(row=1, column=1)
        botonBuscar = tkinter.Button(self.ventana_principal, text = "Buscar",
                           command = self.buscar_alumnos).grid(row=1, column=2)
        self.treeview = ttk.Treeview(self.ventana_principal)
        self.treeview = ttk.Treeview(self.ventana_principal, 
                                     columns=("texto", "etiquetas"))
        self.treeview.heading("#0", text="id")
        self.treeview.column("#0", minwidth=0, width="40")
        self.treeview.heading("texto", text="Texto")
        self.treeview.heading("etiquetas", text="Etiquetas")
        self.treeview.grid(row=10, columnspan=3)
        self.poblar_tabla()
        botonSalir = tkinter.Button(self.ventana_principal, text = "Salir",
                command = self.salir).grid(row=11,column=1)
        self.cajaBuscar.focus()

    def poblar_tabla(self, alumnos = None):
        #Vaciamos el Treeview, si tuviera algún item:
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        #Si no recibimos la lista de notas, le asignamos todas las notas:
        if not alumnos:
            alumnos = self.alumnado.alumnos
        #Poblamos el treeview:
        for alumno in alumnos:
            item = self.treeview.insert("", tkinter.END, text=alumno.buscar_por_nombre_apellido,
                              values=(alumno.nivel, alumno.grado), iid=alumno.buscar_por_nombre_apellido)
        
    def agregar_alumno(self):
        self.modalAgregar = tkinter.Toplevel(self.ventana_principal)
        #top.transient(parent)
        self.modalAgregar.grab_set()
        tkinter.Label(self.modalAgregar, text = "Nombre: ").grid()
        self.nombre = tkinter.Entry(self.modalAgregar)
        self.nombre.grid(row=0,column=1,columnspan=2)
        self.nombre.focus()
        tkinter.Label(self.modalAgregar, text = "Apellido: ").grid(row=1)
        self.apellido = tkinter.Entry(self.modalAgregar)
        self.apellido.grid(row=1, column=1, columnspan=2)
        tkinter.Label(self.modalAgregar, text = "Nivel: ").grid(row=1)
        self.grado = tkinter.Entry(self.modalAgregar)
        self.grado.grid(row=1, column=1, columnspan=2)
        tkinter.Label(self.modalAgregar, text = "Grado: ").grid(row=1)
        self.nivel = tkinter.Entry(self.modalAgregar)
        self.nivel.grid(row=1, column=1, columnspan=2)
        botonOK = tkinter.Button(self.modalAgregar, text="Guardar",
                command=self.agregar_ok)
        self.modalAgregar.bind("<Return>", self.agregar_ok)
        botonOK.grid(row=2)
        botonCancelar = tkinter.Button(self.modalAgregar, text = "Cancelar",
                command = self.modalAgregar.destroy)
        botonCancelar.grid(row=2,column=2)

    def agregar_ok(self, event=None):
        alumno = self.alumnado.nuevo_alumno(self.texto.get(), self.etiquetas.get())
        self.modalAgregar.destroy()
        item = self.treeview.insert("", tkinter.END, text=alumno.buscar_por_nombre_apellido,
                                        values=(alumno.nivel, alumno.grado))
        #print(self.treeview.set(item))

    def modificar_alumno(self):
        if not self.treeview.selection():
            messagebox.showwarning("Sin selección",
                    "Seleccione primero el alumno a modificar")
            return False
        #id = int(self.treeview.selection()[0][1:])
        item = self.treeview.selection()        
        id = self.treeview.item(item)['text']
        #id = self.treeview.item(item, option="text")

        #Para probar:
        print(id)

        alumno = self.alumnado.buscar_por_nombre_apellido(id)
        self.modalModificar = tkinter.Toplevel(self.ventana_principal)
        self.modalModificar.grab_set()
        tkinter.Label(self.modalModificar, text = "Nombre: ").pack()
        self.texto = tkinter.Entry(self.modalModificar)
        self.texto.insert(0,alumno.texto)
        self.texto.pack()
        self.texto.focus()
        tkinter.Label(self.modalModificar, text = "Apellido: ").pack()
        self.etiquetas = tkinter.Entry(self.modalModificar)
        self.etiquetas.insert(0,nota.etiquetas)
        self.etiquetas.pack()
        tkinter.Label(self.modalModificar, text = "Nivel: ").pack()
        self.etiquetas = tkinter.Entry(self.modalModificar)
        self.etiquetas.insert(0,nota.etiquetas)
        self.etiquetas.pack()
        tkinter.Label(self.modalModificar, text = "Grado: ").pack()
        self.etiquetas = tkinter.Entry(self.modalModificar)
        self.etiquetas.insert(0,nota.etiquetas)
        self.etiquetas.pack()
        botonOK = tkinter.Button(self.modalModificar, text="Guardar",
                command=self.modificar_ok)
        self.modalModificar.bind("<Return>", self.modificar_ok)
        botonOK.pack()
        botonCancelar = tkinter.Button(self.modalModificar, text = "Cancelar",
                                       command = self.modalModificar.destroy)
        botonCancelar.pack()

    def modificar_ok(self, event=None):
        item = self.treeview.selection()        
        id = self.treeview.item(item)['text']
        print("Modificada la nota ",id)
        #id = int(self.treeview.selection()[0][1:])
        #idtree = self.treeview.selection()[0]
        self.anotador.modificar_nota(id, self.texto.get())
        self.anotador.modificar_etiquetas(id, self.etiquetas.get())
        self.treeview.set(self.treeview.selection()[0], column="texto",
                          value = self.texto.get())
        self.treeview.set(self.treeview.selection()[0], column="etiquetas",
                          value = self.etiquetas.get())
        self.modalModificar.destroy()
   
    def eliminar_nota(self):
        if not self.treeview.selection():
            messagebox.showwarning("Sin selección",
                    "Seleccione primero la nota a eliminar")
            return False
        else:
            resp = messagebox.askokcancel("Confirmar",
                    "¿Está seguro de eliminar la nota?")
            if resp:
                id = int(self.treeview.selection()[0][1:])
                self.treeview.delete(self.treeview.selection()[0])
                self.anotador.eliminar_nota(id)
            else:
                return False

    def buscar_notas(self):
        filtro = self.cajaBuscar.get()
        notas = self.anotador.buscar(filtro)
        if notas:
            self.poblar_tabla(notas)
        else:
            messagebox.showwarning("Sin resultados",
                                "Ninguna nota coincide con la búsqueda")
    
    def salir(self):
        self.repositorio.guardar_todo(self.anotador.notas)
        self.ventana_principal.destroy()

if __name__ == "__main__":
    gui = Gui()
    gui.ventana_principal.mainloop()