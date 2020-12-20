# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 13:28:13 2020

@author: Carolina Colina Zamorano
"""

import sqlite3
import sys
import math
import time
import os

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QTableWidgetItem
from Ordenes_ui import Ui_MainWindow
from PyQt5.QtCore import QThread
from PyQt5.QtGui import *



class OrdenesWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        # Método encargado de generar la interfaz
        self.setupUi(self)
        #uic.loadUi("Ordenes.ui", self)
        self.labelOP = QtWidgets.QLabel(self.frame)
        self.setNombreOperario()
        self.setNombreServicio()
        self.setHora()
        self.generarOrdenes()
        self.btn_buscarMaterial.clicked.connect(self.buscar)
        global maquinas, carros


    # Función para conecetar con la base de datos
    @staticmethod
    def conectarBD():
        con = sqlite3.connect('Y:\LucErik.db')
        cursor = con.cursor()
        return cursor

    def buscar(self):
        os.system('python BuscarMaterial.py')


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
    def generarOrdenes(self):
        # Conexión con la base de datos
        global carros_llevar, carros, ubicacion, cub_disponibles
        carros = 0
        cub_disponibles = 0

        cursor = OrdenesWindow.conectarBD()

        listaOrdenes = []
        print(listaOrdenes)


        cursor.execute("SELECT * FROM MAQUINAS")
        maquinas = cursor.fetchall()
        print("maquinas: ", maquinas)

        for i in range(len(maquinas)):
            print("")
            print("Máquina: ", maquinas[i][0])
            cub = maquinas[i][4] - maquinas[i][5]
            print("Cubiertas", cub)

            sql = "SELECT * FROM HUECOS WHERE ID ='" + maquinas[i][0] + "'"
            cursor.execute(sql)
            huecos = cursor.fetchall()[0]
            print("Tabla huecos: ", huecos)
            # print("huecos[0][1]: ", huecos[0][1])

            maquina = maquinas[i][0]
            material = maquinas[i][2]
            pendientes = maquinas[i][4] - maquinas[i][5]
            prioridad = maquinas[i][7]
            print("prioridad:", prioridad)

            columna = 1
            totales = 0
            huecos_totales = maquinas[i][1]
            huecos_disponibles = 0
            print("Huecos que hay en total:", huecos_totales)

            while columna < 11:
                # Si coincide el material
                if huecos[columna] == maquinas[i][2]:
                    totales = totales + huecos[columna + 1]
                    print("Talones totales en la máquina:", totales)
                    columna = columna + 2
                else:
                    columna = columna + 2
                if huecos[columna] == 'VACIO':
                    huecos_disponibles = huecos_disponibles + 1
                    print("Huecos vacíos en máquina:", huecos_disponibles)

            totales = totales / 2
            print("¿Para cuántas cubiertas tengo material?", totales)

            if totales < cub:
                carros_totales = math.ceil((maquinas[i][4] - maquinas[i][5]) * 2 / 140)
                print("Carros totales a llevar:", carros_totales)

                columna = 1
                #cub_disponibles = 0

                ubicacion = ""
                while columna < 11:
                    if huecos[columna] == maquinas[i][2]:
                        cub_disponibles = cub_disponibles + huecos[columna + 1]
                        print("cub_disponibles:", cub_disponibles)
                        carros_disponibles = math.floor(cub_disponibles / 140)
                        print("Carros que hay en máquina:", carros_disponibles)
                        carros_llevar = carros_totales - carros_disponibles
                        print("Carros totales a llevar - carros que hay en máquina: ", carros_llevar)
                        columna = columna + 2
                    else:
                        columna = columna + 2

                print("")
                print("huecos disponibles: ", huecos_disponibles)
                print("carros a llevar", carros_llevar)
                if huecos_disponibles > carros_llevar or huecos_disponibles == carros_llevar:
                    carros = carros_llevar
                    print("carros", carros)
                else:
                    carros = huecos_disponibles
                    print("carros", carros)

            # AÑADIR A LA TABLA MATERIALES PARA QUE LOS ENCUENTRE

                sql = "SELECT * FROM MATERIALES WHERE CODIGO='" + maquinas[i][2] + "' "
                cursor.execute(sql)
                materiales = cursor.fetchall()

                stock = 0
                for c in range(len(materiales)):
                    # Guarda en ubicación donde más disponibles haya
                    print("materiales[c][3]", materiales[c][3])
                    if materiales[c][3] > stock:
                        stock = materiales[c][3]
                        ubicacion = materiales[c][2]
                        print("ubicacion", ubicacion)
                        print("stock", stock)

                listaOrdenes.append((maquina, material, carros, ubicacion, stock, cub_disponibles, pendientes, prioridad))

                print("listaOrdenes", listaOrdenes)

        """ ORDENAR LAS ÓRDENES ANTES DE VISUALIZARLAS """
        # Coloca en primer lugar las que menos material tienen para hacer cubiertas
        # Si coincide, pone en primer lugar la que mayor prioridad tiene
        listaOrdenesOrdenada = sorted(listaOrdenes, key=lambda x: (x[5], -x[7]))
        print("listaOrdenesOrdenada", listaOrdenesOrdenada)

        # Añado las órdenes a la tabla
        self.visualizarOrdenes(listaOrdenesOrdenada)
        # self.visualizarOrdenes(listaOrdenes)

    def visualizarOrdenes(self, listaOrdenesOrdenada):
        # def visualizarOrdenes(self, listaOrdenes):
        for fila in range(len(listaOrdenesOrdenada)):
            for columna in range(8):
                self.tableWidget.setItem(fila, columna, QtWidgets.QTableWidgetItem(str(listaOrdenesOrdenada[fila][columna])))
                # Si el número de cubiertas que puede hacer con el material que tiene es inferior a 20 cambio el color a amarillo
                if listaOrdenesOrdenada[fila][5] < 20 or listaOrdenesOrdenada[fila][5] == 20:
                    self.tableWidget.item(fila, columna).setBackground(QColor("gold"))
                # Si no hay material disponible en stock cambio a rojo
                if listaOrdenesOrdenada[fila][4] == 0:
                    self.tableWidget.item(fila, columna).setBackground(QColor("red"))



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = OrdenesWindow()
    window.show()
    app.exec_()
