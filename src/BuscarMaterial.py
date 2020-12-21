
import os
import sqlite3
import sys
import time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import *
from BuscarMaterial_ui import Ui_MainWindow


class BuscarMaterialWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        # Método encargado de generar la interfaz
        #uic.loadUi("BuscarMaterial.ui", self)
        #self.cargarInterfaz()
        #self.ui = Ui_MainWindow()
        #self.ui.setupUi(self)
        #self.ui.btn_Recoger.clicked(self.recogerMaterial())
        self.tabla()
        self.btn_Recoger.clicked.connect(self.recogerMaterial)
        self.btn_Volver.clicked.connect(self.volver)
        global maq, material, max_carros



    def conectarBD(self):
        con = sqlite3.connect('Y:\LucErik.db')
        cursor = con.cursor()
        return cursor

    def volver(self):
        self.close()

    def recogerMaterial(self):
        # Recorro la tabla
        maquina = sys.argv[1]
        filas = self.tableWidget.rowCount()
        print("filas: ", filas)
        for i in range(filas):
            widget = self.tableWidget.cellWidget(i, 3)
            valor = int(widget.currentText())
            print("Valor: ", valor)
            print("Quitar:", valor)
            # Si el valor es mayor que 0
            if valor > 0:
                print("Guardo los datos")
                # Guardo los datos
                material = self.tableWidget.item(i, 0).text()
                print("Material: ", material)
                ubicacion = self.tableWidget.item(i, 1).text()
                print("Ubicación:", ubicacion)
                stock = int(self.tableWidget.item(i, 2).text()) - valor
                print("Stock:", stock)


                # Descuento el material de donde lo he cogido: tabla MATERIALES
                cursor = self.conectarBD()
                # Si la RTB se ha quedado sin stock borro el registro de la tabla MATERIALES
                if (stock == 0):
                    sql = "DELETE FROM MATERIALES WHERE CODIGO= '"+str(material)+"' AND ORIGEN= '"+str(ubicacion)+"'"
                    cursor.executescript(sql)

                # Sino, actualizo el material
                else:
                    sql = "UPDATE MATERIALES SET STOCK='"+str(stock)+"' WHERE CODIGO= '"+str(material)+"' AND ORIGEN= '"+str(ubicacion)+"' "
                    cursor.executescript(sql)


                """En el caso de que lo haya recogido de una máquina actualizo sus huecos"""
                """Dejo vacíos los huecos de donde he quitado carros"""
                # Recorro la tabla huecos y pongo el material encontrado a VACIO tantas veces como carros se hayan quitado
                sql = "SELECT * FROM HUECOS WHERE ID= '"+str(ubicacion)+"' "
                cursor.execute(sql)
                resul = cursor.fetchall()
                field_names = [i[0] for i in cursor.description]
                print("resul", resul)
                # De esta forma no guarda valores vacíos en huecos
                if len(resul) != 0:
                    huecos = resul
                    print("HUECOS: ", huecos)

                    columna = 3
                    v = valor
                    while columna < 11 and v > 0:
                        if huecos[0][columna] == material:
                            print("huecos[0][columna]", huecos[0][columna])
                            print("huecos[0][columna+1]", huecos[0][columna+1])
                            print("field_names[columna]", field_names[columna])
                            print("huecos[0][0]", huecos[0][0])
                            print("Máquina a la que llevar: ", maquina)

                            # Lo llevo a la máquina que corresponde
                            sql = "SELECT * FROM HUECOS WHERE ID= '"+maquina+"' "
                            cursor.execute(sql)
                            destino = cursor.fetchall()
                            print("Destino", destino)
                            field_namesDestino = [i[0] for i in cursor.description]
                            c = 1
                            añadido = False
                            while c < 11:
                                print("c", c)
                                print("destino[0][c]", destino[0][c])
                                print("field_namesDestino[c]", field_namesDestino[c])
                                print("field_namesDestino[c+1]", field_namesDestino[c+1])
                                print("huecos[0][columna]", huecos[0][columna])
                                print("huecos[0][columna+1]", huecos[0][columna+1])
                                if destino[0][c] == 'VACIO':
                                    print("Aquí")
                                    sql = "UPDATE HUECOS SET '"+field_namesDestino[c]+"'='"+huecos[0][columna]+"' WHERE ID='"+maquina+"' "
                                    cursor.executescript(sql)
                                    print("Aquí")
                                    sql = "UPDATE HUECOS SET '" + field_namesDestino[c+1] + "'='" + str(huecos[0][
                                        columna+1]) + "' WHERE ID='" + maquina + "' "
                                    cursor.executescript(sql)
                                    print("Aquí")
                                    print("destino[0][c]", destino[0][c])
                                    break
                                    c = c + 2
                                else:
                                    c = c + 2

                            # Borro de la máquina a la que se los he quitado
                            sql = "UPDATE HUECOS SET '"+field_names[columna]+"'='VACIO' WHERE ID='"+str(huecos[0][0])+"' "
                            cursor.executescript(sql)
                            sql = "UPDATE HUECOS SET '"+field_names[columna+1]+"'=0 WHERE ID='"+str(huecos[0][0])+"' "
                            cursor.executescript(sql)

                            v = valor - 1
                            print("valor", v)
                            columna = columna + 2
                        else:
                            columna = columna + 2

        self.close()


    # Cargo los datos en la tabla
    def tabla(self):
        maq = sys.argv[1]
        print("Maquina: ", str(maq))
        material = sys.argv[2]
        print("Material: ", material)
        max_carros = int(sys.argv[3])
        ubicacion = sys.argv[4]


        cursor = self.conectarBD()
        sql = "SELECT CODIGO, ORIGEN, STOCK FROM MATERIALES WHERE CODIGO= '"+material+"' AND ORIGEN<> '"+ubicacion+"' "
        cursor.execute(sql)
        items_materiales = cursor.fetchall()
        print("Materiales de tabla: ", items_materiales)

        items_huecos = []

        # De esta forma en la tabla no muestra el stock de ese material que hay en la propia máquina, es decir, la que está seleccionada
        sql = "SELECT ID FROM MAQUINAS WHERE ID<> '"+maq+"' AND MAT_ACTUAL= '"+str(material)+"' OR MAT_PROX= '"+str(material)+"' "
        cursor.execute(sql)
        id_maquina = cursor.fetchall()
        print("id_maquina", id_maquina)

        for a in range(len(id_maquina)):
            sql = "SELECT * FROM HUECOS WHERE ID= '"+str(id_maquina[a][0])+"' "
            cursor.execute(sql)
            items_huecos = items_huecos + cursor.fetchall()
            print("Materiales en huecos: ", items_huecos)


        cont_carros = 0
        for b in range (len(items_huecos)):
            print("b: ", b)
            # Empiezo a contar los carros de ese material que hay en una máquina a partir del segundo hueco, porque el primero es el que está usando y no se le puede quitar
            c = 3
            while c < 11:
                print("c: ", c)
                print("items_huecos[b][c]", items_huecos[b][c])
                if items_huecos[b][c] == material:
                    cont_carros = cont_carros + 1
                    mat = material
                    maquina = id_maquina[b]
                    c = c + 2
                else:
                    c = c + 2
            if cont_carros != 0:
                items_materiales.append((mat, maquina[0], cont_carros))
                print("items_materiales: ", items_materiales)




        self.tableWidget.setRowCount(len(items_materiales))
        for fila in range(len(items_materiales)):
            for columna in range(3):
                self.tableWidget.setItem(fila, columna, QTableWidgetItem(str(items_materiales[fila][columna])))
                self.comboBox = QtWidgets.QComboBox()
                self.comboBox.addItem("0")
                # Que sólo pueda quitar como mucho el número de carros que tiene que llevar aunque haya más stock
                for x in range(items_materiales[fila][2]):
                    if x < max_carros:
                        self.comboBox.addItem(str(x+1))
                self.tableWidget.setCellWidget(fila, 3, self.comboBox)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = BuscarMaterialWindow()
    window.show()
    app.exec_()
