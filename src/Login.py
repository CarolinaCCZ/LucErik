# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 20:55:53 2020

@author: Carolina Colina Zamorano
"""

import os
import sqlite3
import sys
import time

from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QThread

nombre: str = ""
servicio: str = ""


class IncrementarTalonesFabricados(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            os.system('python IncrementarTalonesFabricados.py')
            time.sleep(5)


class DecrementarTalonesConsumidos(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            os.system('python DecrementarTalonesConsumidos.py')
            time.sleep(5)


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        # Método encargado de generar la interfaz
        uic.loadUi("Login.ui", self)
        # self.setWindowTitle("Título")
        # self.showMaximized()

        try:
            self.hilo1 = IncrementarTalonesFabricados()
            self.hilo1.start()
            self.hilo2 = DecrementarTalonesConsumidos()
            self.hilo2.start()
        except (KeyboardInterrupt, SystemExit):
            self.hilo1.terminate()
            self.hilo2.terminate()
            sys.exit()

        self.btn_Login.clicked.connect(self.conectarBD)
        self.btn_acceder.clicked.connect(self.abrirOrdenesWindow)

        time.sleep(1)

    def conectarBD(self):

        global con, cursorServicios, cursorOperarios
        try:
            con = sqlite3.connect('Y:\LucErik.db')
            cursorOperarios = con.cursor()
            cursorServicios = con.cursor()
        except sqlite3.OperationalError:
            sys.exit()

        # Guardo el número del operario y del servicio que ha introducido el usuario
        nop = int(self.n_operario.text())
        nsr = int(self.n_servicio.text())

        # Obtengo los datos de la tabla Operarios
        cursorOperarios.execute('SELECT NOMBRE, NUM_OPERARIO FROM OPERARIOS')
        listaOperarios = cursorOperarios.fetchall()

        # Obtengo los datos de la tabla Servicios
        cursorServicios.execute('SELECT NOMBRE, ID FROM SERVICIOS')
        listaServicios = cursorServicios.fetchall()

        # Una vez guardados los datos cierro la conexión con la base de datos
        con.close()

        # Recorro la lista de operarios, obtengo el nombre del operario y lo muestro en pantalla
        for i in listaOperarios:
            if i[1] == nop:
                self.label_Nombre.setText(i[0])
                self.label_Nombre.setVisible(True)
                # Hago visible el botón Acceder que abrirá la ventana con las órdenes
                self.btn_acceder.setVisible(True)

                # Guardo el nombre del operario en una variable global
                name = i[0]
                self.setNombre(name)

        # Recorro la lista de servicios y obtengo el nombre
        for a in listaServicios:
            if a[1] == nsr:
                service = a[0]
                # Guardo el nombre del servicio en una variable global
                self.setServicio(service)

    # Guarda el nombre del operario
    @staticmethod
    def setNombre(name):
        global nombre
        nombre = name

    # Guarda el nombre del servicio
    @staticmethod
    def setServicio(service):
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
