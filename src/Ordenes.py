# -*- coding: utf-8 -*-
"""
Clase que muestra las órdenes en función de la necesidad de cada máquina
Las órdenes se muestran por orden de necesidad y prioridad

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
from PyQt5.QtCore import pyqtSlot


class OrdenesWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        # Método encargado de generar la interfaz
        self.setupUi(self)
        self.setNombreOperario()
        self.setNombreServicio()
        self.setHora()
        self.generarOrdenes()
        self.btn_buscarMaterial.clicked.connect(self.buscar)
        self.btn_llevarMaterial.clicked.connect(self.llevarMaterial)
        self.btn_actualizar.clicked.connect(self.generarOrdenes)
        # global maquinas, carros, listaOrdenes, carros_llevar, ubicacion, cub_disponibles

    """ Función para conecetar con la base de datos """
    @staticmethod
    def conectarBD():
        global con, cur
        try:
            con = sqlite3.connect('Y:\LucErik.db')
            cur = con.cursor()
        except sqlite3.OperationalError:
            sys.exit()
        return cur

    """ Función para añadir el nombre del Operario """
    def setNombreOperario(self):
        # Nombre del Operario
        nombreOP = sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3]
        self.nombreOP.setText(nombreOP)

    """ Función para añadir el nombre del Servicio """
    def setNombreServicio(self):
        # Nombre del servicio
        serv = sys.argv[4]
        self.servicio.setText(serv)

    """ Función que crea el Timer para la hora """
    def setHora(self):
        # Creamos el 'Timer'
        timer = QTimer(self)
        timer.timeout.connect(self.displayTime)
        timer.start(1000)

    """ Función para mostrar la hora """
    def displayTime(self):
        currentTime = QTime.currentTime()
        displayText = currentTime.toString('hh:mm:ss')
        self.hora.setText(displayText)

    """ FUNCIÓN QUE GENERA LAS ÓRDENES """
    def generarOrdenes(self):
        # Conexión con la base de datos
        cursor = OrdenesWindow.conectarBD()

        # Inicializamos la lista de órdenes
        listaOrdenes = []

        # Se obtiene la tabla MÁQUINAS
        cursor.execute("SELECT * FROM MAQUINAS")
        maquinas = cursor.fetchall()
        print("maquinas: ", maquinas)

        # Recorro la tabla máquinas para ver cuál necesita material
        for i in range(len(maquinas)):
            print("")
            print("Máquina: ", maquinas[i][0])
            # Cubiertas que faltan por hacer
            cub = maquinas[i][4] - maquinas[i][5]
            print("Cubiertas que faltan por hacer", cub)

            # Obtenemos los huecos pertenecientes a la máquina que estamos tratando
            print(maquinas[i][0])
            sql = "SELECT * FROM HUECOS WHERE ID ='" + maquinas[i][0] + "'"
            cursor.execute(sql)
            huecos = cursor.fetchall()
            print("Tabla huecos: ", huecos)

            maquina = maquinas[i][0]
            material = maquinas[i][2]
            pendientes = maquinas[i][4] - maquinas[i][5]
            prioridad = maquinas[i][7]

            cub_disponibles = 0
            huecos_totales = maquinas[i][1]
            huecos_disponibles = 0
            talones_disponibles = 0
            carros_llevar = 0
            print("Huecos que hay en total:", huecos_totales)

            # Recorro los huecos para la máquina que estoy evaluando
            for b in range(len(huecos)):
                # Cuento los talones totales de ese material que hay en la máquina
                if huecos[b][2] == maquinas[i][2]:
                    cub_disponibles = cub_disponibles + huecos[b][3]
                # Cuento los huecos ocupados
                if huecos[b][2] == 'VACIO':
                    huecos_disponibles = huecos_disponibles + 1
            print("Huecos disponibles", huecos_disponibles)

            cub_disponibles = int(cub_disponibles / 2)
            print("¿Para cuántas cubiertas tengo material?", cub_disponibles)

            # Vamos a calcular el número de carros que tenemos que llevar
            # Si el número de cubiertas que puedo hacer (cub_disponibles) es menor que el número de cubiertas pendientes (cub)
            if cub_disponibles < cub:
                # Cada cubierta necesita 2 talones
                # Cuento los talones que tengo que llevar
                talonesTotales_llevar = (maquinas[i][4] - maquinas[i][5]) * 2
                print("Talones totales a llevar", talonesTotales_llevar)

                # Cuento los talones que ya tengo en la máquina de ese material
                for c in range(len(huecos)):
                    # Si coincide el material sumo el número de talones
                    if huecos[c][2] == maquinas[i][2]:
                        talones_disponibles = talones_disponibles + huecos[c][3]
                        print("talones disponibles:", talones_disponibles)
                        # Talones que tengo que llevar menos los que tengo disponibles en la máquina
                        talones_llevar = talonesTotales_llevar - talones_disponibles
                        print("Talones a llevar", talones_llevar)
                        # Sabiendo que cada carro contiene 140 talones, calculo el número de carro que tengo que llevar
                        carros_totales = math.ceil(talones_llevar / 140)
                        print("Carros a totales", carros_totales)
                        # Puedo llevar como máximo tantos carros como huecos vacío haya
                        if carros_totales <= huecos_disponibles:
                            carros_llevar = carros_totales
                        else:
                            carros_llevar = huecos_disponibles

                        print("Carros llevar", carros_llevar)

                # Busco en la tabla materiales el stock de ese material y su ubicación
                sql = "SELECT * FROM MATERIALES WHERE CODIGO='" + maquinas[i][2] + "' "
                cursor.execute(sql)
                materiales = cursor.fetchall()

                stock = 0
                ubicacion = ""
                for d in range(len(materiales)):
                    # Guarda en ubicación donde más disponibles haya
                    print("materiales[d][3]", materiales[d][3])
                    if materiales[d][3] > stock:
                        stock = materiales[d][3]
                        ubicacion = materiales[d][2]
                        print("ubicacion", ubicacion)
                        print("stock", stock)

                # SI EL NÚMERO DE CUBIERTAS QUE TIENE PARA HACER ES MAYOR O IGUAL QUE 210 NO GENERA ORDEN
                if cub_disponibles < 140 and carros_llevar > 0:
                    listaOrdenes.append(
                        (maquina, material, carros_llevar, ubicacion, stock, cub_disponibles, pendientes, prioridad))

                    print("listaOrdenes", listaOrdenes)

        # ORDENAR LAS ÓRDENES ANTES DE VISUALIZARLAS
        # Coloca en primer lugar las que menos material tienen para hacer cubiertas
        # Si coincide, pone en primer lugar la que mayor prioridad tiene
        listaOrdenesOrdenada = sorted(listaOrdenes, key=lambda x: (x[5], -x[7]))
        print("listaOrdenesOrdenada", listaOrdenesOrdenada)

        # Añado las órdenes a la tabla
        self.visualizarOrdenes(listaOrdenesOrdenada)



        """row = self.tableWidget.currentRow()
        print("row seleccionada: ", row)
        if row != -1:
            self.btn_llevarMaterial.setEnabled(True)
        else:
            self.btn_llevarMaterial.setEnabled(False)"""

    """ FUNCIÓN QUE AÑADE A LA TABLA Y MUESTRA EN PANTALLA LAS ÓRDENES GENERADAS """
    def visualizarOrdenes(self, listaOrdenesOrdenada):
        self.tableWidget.setRowCount(len(listaOrdenesOrdenada))
        for fila in range(len(listaOrdenesOrdenada)):
            for columna in range(8):
                # Añado la orden a la tabla
                self.tableWidget.setItem(fila, columna,
                                         QtWidgets.QTableWidgetItem(str(listaOrdenesOrdenada[fila][columna])))
                # Si el número de cubiertas que puede hacer con el material que tiene es inferior a 20 cambio el color a amarillo
                if listaOrdenesOrdenada[fila][5] < 20 or listaOrdenesOrdenada[fila][5] == 20:
                    self.tableWidget.item(fila, columna).setBackground(QColor("gold"))
                # Si no hay material disponible en stock cambio a rojo
                if listaOrdenesOrdenada[fila][4] == 0:
                    self.tableWidget.item(fila, columna).setBackground(QColor("red"))
        self.tableWidget.clearSelection()

        # Controla que se haya seleccionado una fila de la tabla para habilitar los botones llevar material y buscar meterial
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidget.selectionModel().selectionChanged.connect(self.itemSeleccionado)

    @pyqtSlot()
    def itemSeleccionado(self):
        self.btn_llevarMaterial.setEnabled(
            bool(self.tableWidget.selectionModel().selectedRows()))
        self.btn_buscarMaterial.setEnabled(
            bool(self.tableWidget.selectionModel().selectedRows()))


    """ Función para llevar el material """

    def llevarMaterial(self):
        # Obtengo la fila seleccionada
        row = self.tableWidget.currentRow()
        # Saco la máquina
        maquina = self.tableWidget.item(row, 0).text()
        print("maquina", maquina)
        # Saco el material
        material = self.tableWidget.item(row, 1).text()
        print("material", material)
        # Saco los carros máximos que hay que llevar
        max_carros = int(self.tableWidget.item(row, 2).text())
        print("max_carros", max_carros)
        # Saco la ubicación
        ubicacion = self.tableWidget.item(row, 3).text()
        print("ubicación", ubicacion)

        cursor = OrdenesWindow.conectarBD()

        sql = "SELECT * FROM MATERIALES WHERE CODIGO= '" + material + "' AND ORIGEN='" + ubicacion + "'"
        cursor.execute(sql)
        resul = cursor.fetchall()
        print("resul", resul)
        total = resul[0][3] - max_carros
        print("total", total)


        # Primero descuento el material que he cogido
        sql = "UPDATE MATERIALES SET STOCK='" + str(total) + "' WHERE CODIGO= '" + str(
            material) + "' AND ORIGEN= '" + str(ubicacion) + "' "
        cursor.executescript(sql)

        # En el caso de que algún material haya quedado con stock a 0, lo eliminamos de la lista materiales
        sql = "DELETE FROM MATERIALES WHERE STOCK=0"
        cursor.executescript(sql)

        # A continuación relleno los huecos de la máquina a la que llevo el material
        sql = "SELECT * FROM HUECOS WHERE ID= '" + maquina + "' "
        cursor.execute(sql)
        huecos = cursor.fetchall()
        print("huecos", huecos)
        print("len(huecos)", len(huecos))

        cont_carros = 0
        for z in range(len(huecos)):
            print("huecos[z][0]", huecos[z][0])
            print("huecos[z][1]", huecos[z][1])
            print("huecos[z][2]", huecos[z][2])
            print("huecos[z][3]", huecos[z][3])
            print("max_carros", max_carros)
            if huecos[z][2] == 'VACIO' and cont_carros < max_carros:
                print("Es vacío")
                sql = "UPDATE HUECOS SET MATERIAL='"+material+"', CANTIDAD=140 WHERE ID='"+maquina+"' AND HUECO='"+huecos[z][1]+"' "
                cursor.executescript(sql)
                cont_carros = cont_carros + 1
            else:
                print("No es vacío")

        # Actualizo la tabla órdenes
        self.generarOrdenes()


    """ Función que busca el material en otras ubicaciones """

    def buscar(self):
        # Obtengo la fila seleccionada
        row = self.tableWidget.currentRow()
        # Saco la máquina
        maquina = self.tableWidget.item(row, 0).text()
        # Saco el material
        material = self.tableWidget.item(row, 1).text()
        # Saco los carros máximos que hay que llevar
        max_carros = self.tableWidget.item(row, 2).text()
        # Saco la ubicación
        ubicacion = self.tableWidget.item(row, 3).text()
        # Si no hay carros disponibles en ninguna parte le asigno el valor NULL para que no sea vacío
        if len(ubicacion) == 0:
            ubicacion = 'NULL'
        # Paso como argumento el material que tiene que buscar
        os.system('python BuscarMaterial.py' + " " + maquina + " " + material + " " + max_carros + " " + ubicacion)

        # Quito la selección de la fila anteriormente seleccionada
        self.tableWidget.clearSelection()



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = OrdenesWindow()
    window.show()
    app.exec_()
