#! /usr/bin/env python3
from alumnado import Alumnado
from alumno import Alumno
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
                           command = self.buscar_alumno).grid(row=1, column=2)
        self.treeview = ttk.Treeview(self.ventana_principal)
        self.treeview = ttk.Treeview(self.ventana_principal, 
                                     columns=("nombre", "apellido", "nivel", "grado"))
        self.treeview.heading("#0", text="id")
        self.treeview.column("#0", minwidth=0, width="40")
        self.treeview.heading("nombre", text="Nombre")
        self.treeview.heading("apellido", text="Apellido")
        self.treeview.heading("nivel", text="Nivel")
        self.treeview.heading("grado", text="Grado")
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
            alumnos = self.alumnado.lista_alumnos
        #Poblamos el treeview:
        for alumno in alumnos:
            item = self.treeview.insert("", tkinter.END, text=alumno.id,
                              values=(alumno.nombre, alumno.apellido, alumno.nivel, alumno.grado), iid=alumno.id)
            #item = self.treeview.insert("", tkinter.END, text=alumno.buscar_por_nombre_apellido,
            #                  values=(alumno.nivel, alumno.grado), iid=alumno.buscar_por_nombre_apellido)
        
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
        tkinter.Label(self.modalAgregar, text = "Nivel: ").grid(row=2)
        self.nivel = tkinter.Entry(self.modalAgregar)
        self.nivel.grid(row=2, column=1, columnspan=2)
        tkinter.Label(self.modalAgregar, text = "Grado: ").grid(row=3)
        self.grado = tkinter.Entry(self.modalAgregar)
        self.grado.grid(row=3, column=1, columnspan=2)
        botonOK = tkinter.Button(self.modalAgregar, text="Guardar",
                command=self.agregar_ok)
        self.modalAgregar.bind("<Return>", self.agregar_ok)
        botonOK.grid(row=4)
        botonCancelar = tkinter.Button(self.modalAgregar, text = "Cancelar",
                command = self.modalAgregar.destroy)
        botonCancelar.grid(row=4,column=2)

    def agregar_ok(self, event=None):
        alumno = self.alumnado.nuevo_alumno(self.nombre.get(), self.apellido.get(), self.nivel.get(), self.grado.get())
        self.modalAgregar.destroy()
        item = self.treeview.insert("", tkinter.END, text=alumno.id,
                                        values=(alumno.nombre, alumno.apellido, alumno.nivel, alumno.grado))
        #print(self.treeview.set(item))

    def modificar_alumno(self):
        if not self.treeview.selection():
            messagebox.showwarning("Sin selección",
                    "Seleccione primero el alumno a modificar")
            return False
        
        item = self.treeview.selection()        
        id_alumno = int(self.treeview.item(item)['text'])
        alumno = self.alumnado._buscar_por_id(id_alumno)
        self.modalModificar = tkinter.Toplevel(self.ventana_principal)
        self.modalModificar.grab_set()
        tkinter.Label(self.modalModificar, text = "Nivel: ").pack()
        self.nivel = tkinter.Entry(self.modalModificar)
        self.nivel.insert(0, alumno.nivel)
        self.nivel.pack()
        tkinter.Label(self.modalModificar, text = "Grado: ").pack()
        self.grado = tkinter.Entry(self.modalModificar)
        self.grado.insert(0, alumno.grado)
        self.grado.pack()
        botonOK = tkinter.Button(self.modalModificar, text="Guardar", command=self.modificar_ok)
        self.modalModificar.bind("<Return>", self.modificar_ok)
        botonOK.pack()
        botonCancelar = tkinter.Button(self.modalModificar, text = "Cancelar", command = self.modalModificar.destroy)
        botonCancelar.pack()

    def modificar_ok(self, event = None):
        item = self.treeview.selection()        
        id_alumno = int(self.treeview.item(item)['text'])
        resultado = self.alumnado.modificar(self.nivel.get(), self.grado.get(),id_alumno)
        if resultado:
            self.treeview.set(self.treeview.selection()[0], column="nivel", value=self.nivel.get())
            self.treeview.set(self.treeview.selection()[0], column="grado", value=self.grado.get())
            self.modalModificar.destroy()
        else:
            messagebox.showwarning("Error", "Error al modificar alumno")


   
    def eliminar_alumno(self):
        if not self.treeview.selection():
            messagebox.showwarning("Sin selección",
                    "Seleccione el alumno a eliminar")
            return False
        else:
            resp = messagebox.askokcancel("Confirmar",
                    "¿Está seguro de querer eliminar al alumno del sistema?")
            if resp:
                id_alumno = int(self.treeview.selection()[0])
                self.treeview.delete(self.treeview.selection()[0])
                self.alumnado.eliminar_alumno(id_alumno)
            else:
                return False

    def buscar_alumno(self):
        filtro = self.cajaBuscar.get()
        alumno = self.alumnado.buscar(filtro)
        if alumno:
            self.poblar_tabla(alumno)
        else:
            messagebox.showwarning("Sin resultados",
                                "Ningun alumno coincide con la búsqueda")
    
    def salir(self):
        self.repositorio.guardar_todo(self.alumnado.lista_alumnos)
        self.ventana_principal.destroy()

if __name__ == "__main__":
    gui = Gui()
    gui.ventana_principal.mainloop()