# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 12:45:35 2020

@author: carol
"""

from Login_ui import *
import sqlite3
from PyQt5 import uic
from Ordenes_ui import *
import os
nombre = ""
servicio = ""


class LoginWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        # Método encargado de generar la interfaz
        uic.loadUi("Login.ui",self)
        #self.setupUi(self)
        self.btn_Login.clicked.connect(self.conectarBD)
        
        self.btn_acceder.clicked.connect(self.abrirOrdenesWindow)
    
        
    def conectarBD(self):
        con = sqlite3.connect('Z:\LucErik.db')
        
        # Guardo el número del operario y del servicio que ha introducido el usuario
        nop = int(self.n_operario.text())
        nsr = int (self.n_servicio.text())
        
        cursorOperarios = con.cursor()
        # Obtengo los datos de la tabla Operarios
        cursorOperarios.execute('SELECT NOMBRE, NUM_OPERARIO FROM OPERARIOS')
        listaOperarios = cursorOperarios.fetchall()
        
        cursorServicios = con.cursor()
        # Obtengo los datos de la tabla Servicios
        cursorServicios.execute('SELECT NOMBRE, ID FROM SERVICIOS')
        listaServicios = cursorServicios.fetchall()
        
        # Una vez guardados los datos cierro la conexión con la base de datos
        con.close()
        
        # Recorro la lista de operarios, obtengo el nombre del operario y lo muestro en pantalla
        for i in listaOperarios:
            if(i[1] == nop):
                self.label_Nombre.setText(i[0])
                self.label_Nombre.setVisible(True)
                # Hago visible el botón Acceder que abrirá la ventana con las órdenes
                self.btn_acceder.setVisible(True)
                
                # Guardo el nombre del operario en una variable globar
                name = i[0]
                self.setNombre(name)
        
        # Recorro la lista de servicios y obtengo el nombre
        for a in listaServicios:
            if(a[1] == nsr):
                service = a[0]
                # Guardo el nombre del servicio en una variable global
                self.setServicio(service)
                
    # Guarda el nombre del operario
    def setNombre(self, name):
        global nombre
        nombre = name
    
    # Guarda el nombre del servicio
    def setServicio(self, service):
        global servicio
        servicio = service

         
    # La ventana actual se cierra y se abre la ventana con el listado de las órdenes.
    def abrirOrdenesWindow(self):
        self.close()
        # Abro la ventana con las órdenes y le paso el nombre del operario y el nombre del servicio
        os.system('python Ordenes.py' + ' ' + nombre + ' ' + servicio)

      
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = LoginWindow()
    window.show()
    app.exec_()