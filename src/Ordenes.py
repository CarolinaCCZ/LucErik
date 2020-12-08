# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 13:28:13 2020

@author: carol
"""


import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5 import uic
import Login as lg
from Ordenes_ui import *



class OrdenesWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        # Método encargado de generar la interfaz
        #self.setupUi(self)
        uic.loadUi("Ordenes.ui",self)
        self.labelOP = QtWidgets.QLabel(self.frame)
        self.setNombreOperario()
        self.setNombreServicio()
        self.setHora()
        self.mostarOrdenes()
        
    
    
    # Función para concetar con la base de datos
    def conectarBD(self):
        con = sqlite3.connect('Z:\LucErik.db')
        cur = con.cursor()
        return cur, con
        

    # Función para añadir el nombre del Operario
    def setNombreOperario(self):
        # Nombre del Operario
        nombreOP = sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3]
        self.nombreOP.setText(nombreOP)
       
    # Función para añadir el nombre del Servicio
    def setNombreServicio(self):
        # Nombre del servicio
        serv = sys.argv[4]
        self.servicio.setText(serv)
    
    # Función que crea el Timer para la hora
    def setHora(self):
        # Creamos el 'Timer'
        timer = QTimer(self)
        timer.timeout.connect(self.displayTime)
        timer.start(1000)
        
    # Función para mostrar la hora
    def displayTime(self):
        currentTime = QTime.currentTime()
        displayText = currentTime.toString('hh:mm:ss')
        self.hora.setText(displayText)
        
    # Función que muestra las órdenes en una tabla en pantalla   
    def mostarOrdenes(self):
        # Conexión con la base de datos
        cur, con = self.conectarBD()
        cur.execute('SELECT * FROM ORDENES')
        # Obtengo el listado de las órdenes
        listaOrdenes = cur.fetchall()
        
        # Una vez guardados los datos cierro la conexión con la base de datos
        con.close()
        
        # Añado las órdenes a la tabla
        for fila in range(len(listaOrdenes)):
            for columna in range(7):
                # Si el valor es un int debo convertirlo a string para que lo inserte en la tabla
                if (type(listaOrdenes[fila][columna]) == int):
                    celda = str(listaOrdenes[fila][columna])
                    self.tableWidget.setItem(fila, columna, QTableWidgetItem(celda))
                else:
                    self.tableWidget.setItem(fila, columna, QTableWidgetItem(listaOrdenes[fila][columna]))
        
 
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = OrdenesWindow()
    window.show()
    app.exec_()