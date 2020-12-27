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
        self.comboBox = QtWidgets.QComboBox()
        # Método encargado de generar la interfaz
        self.setupUi(self)
        self.mostrarOtrasUbicaciones()
        self.btn_Recoger.clicked.connect(self.recogerMaterial)
        self.btn_Volver.clicked.connect(self.volver)
        # global maq, material, max_carros

    """ FUNCIÓN PARA CONECTAR CON LA BASE DE DATOS """
    @staticmethod
    def conectarBD():
        global con, cur
        try:
            con = sqlite3.connect('Y:\LucErik.db')
            cur = con.cursor()
        except sqlite3.OperationalError:
            sys.exit()
        return cur

    """ FUNCIÓN QUE CIERRA LA VENTANA ACTUAL """
    def volver(self):
        self.close()

    """ FUNCIÓN QUE ACTUALIZA LOS HUECOS DE LAS MÁQUINAS CUANDO SE QUITA MATERIAL DE ELLAS
    ACTUALIZA EL STOCK EN LA TABLA MATERIALES """
    def recogerMaterial(self):
        # Guardo en máquina el primer valor pasado como parámetro
        maquina = sys.argv[1]
        # Guardo en filas el número de filas de la tabla
        filas = self.tableWidget.rowCount()
        print("filas: ", filas)

        # Recorro la tabla
        for i in range(filas):
            # Guardo en valor, el número seleccionado en la lista desplegable
            widget = self.tableWidget.cellWidget(i, 3)
            valor = int(widget.currentText())
            print("Valor: ", valor)
            print("Quitar:", valor)

            # Si el valor es mayor que 0, es decir, vamos a quitar algún carro
            if valor > 0:
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
                if stock == 0:
                    sql = "DELETE FROM MATERIALES WHERE CODIGO= '" + str(material) + "' AND ORIGEN= '" + str(
                        ubicacion) + "'"
                    cursor.executescript(sql)

                # Sino, actualizo el material
                else:
                    sql = "UPDATE MATERIALES SET STOCK='" + str(stock) + "' WHERE CODIGO= '" + str(
                        material) + "' AND ORIGEN= '" + str(ubicacion) + "' "
                    cursor.executescript(sql)

                # En el caso de que lo haya recogido de una máquina actualizo sus huecos
                # Dejo vacíos los huecos de donde he quitado carros
                # Recorro la tabla huecos y pongo el material encontrado a VACIO tantas veces como carros se hayan quitado
                sql = "SELECT * FROM HUECOS WHERE ID= '" + str(
                    ubicacion) + "' AND HUECO<>'H1' AND MATERIAL= '" + material + "' "
                cursor.execute(sql)
                resul = cursor.fetchall()
                print("resul", resul)
                # De esta forma no guarda valores vacíos en huecos
                if len(resul) != 0:
                    huecos = resul
                    print("HUECOS: ", huecos)

                    print("Máquina a la que llevar: ", maquina)
                    # Lo llevo a la máquina que corresponde

                    # Recorro la tabla huecos para esa máquina y buscar los huecos vacíos
                    sql = "SELECT * FROM HUECOS WHERE ID= '" + maquina + "' "
                    cursor.execute(sql)
                    destino = cursor.fetchall()
                    print("Destino", destino)

                    v = valor
                    for b in range(len(huecos)):
                        print("b", b)
                        for a in range(len(destino)):
                            print("a", a)
                            print("destino[a][2]", destino[a][2])
                            if destino[a][2] == 'VACIO' and v > 0:
                                print("material", material)
                                print("destino[a][1]", destino[a][1])
                                print("huecos[a][3]", huecos[b][3])
                                sql = "UPDATE HUECOS SET MATERIAL='" + material + "', CANTIDAD='" + str(
                                    huecos[b][3]) + "' WHERE ID='" + maquina + "' AND HUECO='" + destino[a][1] + "'"
                                cursor.executescript(sql)
                                sql = "SELECT * FROM HUECOS WHERE ID= '" + maquina + "' "
                                cursor.execute(sql)
                                destino = cursor.fetchall()
                                print("Destino", destino)

                                v = v - 1

                                # Pongo los huecos en vacío a la máquina a la que se los he quitado
                                print("huecos[b][1]", huecos[b][1])
                                sql = "UPDATE HUECOS SET MATERIAL='VACIO', CANTIDAD=0 WHERE ID='" + ubicacion + "' AND HUECO='" + \
                                      huecos[b][1] + "'"
                                cursor.executescript(sql)
                                break

        self.close()

    """ FUNCIÓN QUE AÑADE A LA TABLA Y MUESTRA EN PANTALLA LAS UBICACIONES Y CANTIDAD DEL MATERIAL ENCONTRADO """
    def mostrarOtrasUbicaciones(self):
        # Guardo en maq el primer valor pasado como parámetro
        maquina = sys.argv[1]
        print("Maquina: ", str(maquina))
        # Guardo en material el segundo valor pasado como parámetro
        material = sys.argv[2]
        print("Material: ", material)
        # Guardo en max_carros el tercer valor pasado como parámetro
        max_carros = int(sys.argv[3])
        # Guardo en ubicacion el cuarto valor pasado como parámetro
        ubicacion = sys.argv[4]

        cursor = self.conectarBD()
        # Obtengo en qué RTBS se encuentra ese material y cantidades aparte de la que se muestra en la orden
        sql = "SELECT CODIGO, ORIGEN, STOCK FROM MATERIALES WHERE CODIGO= '" + material + "' AND ORIGEN<> '" + ubicacion + "' "
        cursor.execute(sql)
        items_materiales = cursor.fetchall()
        print("Materiales de tabla: ", items_materiales)

        items_huecos = []

        # Obtengo las máquinas en las que se encuentra el material
        # De esta forma en la tabla no muestra el stock de ese material que hay en la propia máquina, es decir, la que está seleccionada
        sql = "SELECT ID FROM MAQUINAS WHERE ID<> '" + maquina + "' AND MAT_ACTUAL= '" + str(
            material) + "' OR MAT_PROX= '" + str(material) + "' "
        cursor.execute(sql)
        id_maquina = cursor.fetchall()
        print("id_maquina", id_maquina)

        # Para cada una de las máquinas obtengo las filas de la tabla huecos para esa máquina y ese material
        # Obtengo en qué máquinas y cantidades de ese material hay aparte de la que se muestra en la orden
        for a in range(len(id_maquina)):
            sql = "SELECT * FROM HUECOS WHERE ID= '" + str(id_maquina[a][0]) + "' AND MATERIAL= '" + str(
                material) + "' AND HUECO<>'H1'"
            cursor.execute(sql)
            items = cursor.fetchall()
            print("items", items)
            if len(items) > 0:
                items_huecos.append(items)
                print("Materiales en huecos: ", items_huecos)


        for b in range(len(items_huecos)):
            print("len(items_huecos)", len(items_huecos))
            # Empiezo a contar los carros de ese material que hay en una máquina a partir del segundo hueco, porque el primero es el que está usando y no se le puede quitar

            cont_carros = 0
            for c in range(len(items_huecos[b])):
                print("items_huecos[b]", items_huecos[b])
                print("items_huecos[b][c]", items_huecos[b][c])
                if items_huecos[b][c][2] == material:
                    cont_carros = cont_carros + 1
                    print("cont_carros", cont_carros)
                    # mat = material
                    print("mat", material)
                    maquina = items_huecos[b][c][0]
                    print("maquina", maquina)


            if cont_carros != 0:
                items_materiales.append((material, maquina, cont_carros))
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
                        self.comboBox.addItem(str(x + 1))
                self.tableWidget.setCellWidget(fila, 3, self.comboBox)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = BuscarMaterialWindow()
    window.show()
    app.exec_()
