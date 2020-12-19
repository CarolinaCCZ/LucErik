# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:00:08 2020

@author: Carolina Colina Zamorano
"""

import sqlite3
import os


class IncrementarTalonesFabricados:
    def __init__(self):
        super().__init__()

    @staticmethod
    def incrementar():
        global con, cursor
        try:
            con = sqlite3.connect('Y:\LucErik.db')
            cursor = con.cursor()
            cursor2 = con.cursor()
            cursor3 = con.cursor()
        except sqlite3.OperationalError:
            sys.exit()


        sql = "SELECT * FROM LISTADO_RTBS"
        cursor.execute(sql)
        listadoRTBS = cursor.fetchall()
        print("Listado RTBS: ", listadoRTBS)
        #print("listadoRTBS[1][0]: ", listadoRTBS[1][0]) # rtb2

        # Recorro el listado de RTB'S
        for i in range(len(listadoRTBS)):
            sql = "SELECT * FROM PEDIDO WHERE ID= '"+str(listadoRTBS[i][0])+"' "
            cursor.execute(sql)
            rtb = cursor.fetchall()
            print("")
            print("rtb", rtb)

            # Para cada una de las máquinas voy incrementando el número de carros que se producen.
            # Se incrementa en 1 cada 20 minutos
            for a in range(len(rtb)):
                sql = "SELECT * FROM PRODUCCION_TALONES WHERE ID= '"+rtb[a][0]+"' "
                cursor.execute(sql)
                ped = cursor.fetchall()
                print("ped: ", ped)
                if ped[a][3] < ped[a][4]:
                    sql = "UPDATE PRODUCCION_TALONES SET PRODUCIDOS=PRODUCIDOS+1 WHERE ID_MATERIAL= '"+ped[a][1]+"' "
                    cursor.executescript(sql)


                    # He incrementado el número de carros en uno del material con el que está trabajando
                    # Tengo que incrementarlo en la tabla MATERIALES
                    # Obtengo lo que está produciendo la RTB
                    sql = "SELECT * FROM PRODUCCION_TALONES WHERE ID= '"+listadoRTBS[i][0]+"' "
                    cursor.execute(sql)
                    prod = cursor.fetchall()
                    print("")
                    print(listadoRTBS[i])
                    print("i: ", i)
                    print("prod", prod)
                    print("prod[a]", prod[i])

                    # Incremento los materiales
                    IncrementarTalonesFabricados.IncrementarMateriales(a, i, cursor, listadoRTBS, prod)

                    """cursor.execute("SELECT * FROM MATERIALES")
                    mat = cursor.fetchall()
                    print("MATERIALES", mat)"""

                    break

        con.close()

    @staticmethod
    # Método que incrementa en la tabla materiales a medida que se producen talones en las rtb's
    def IncrementarMateriales(a, i, cursor, listadoRTBS, prod):
        # Busco en la tabla MATERIALES si existe un material con ese código
        cursor.execute("SELECT count(*) FROM MATERIALES WHERE CODIGO=?;", (prod[a][1],))
        coinc_material = cursor.fetchall()
        print("coinc_material", coinc_material[0][0])
        # Si NO EXISTE ese código en la tabla materiales, lo inserto
        if coinc_material[0][0] == 0:
            print("Insertamos nuevo resgistro")
            sql = "INSERT INTO MATERIALES (CODIGO, ORIGEN, STOCK) VALUES ('" + str(prod[a][1]) + "', '" + str(
                listadoRTBS[i][0]) + "', '" + str(1) + "')"
            cursor.executescript(sql)

        # SI EXISTE ese código en la tabla MATERIALES
        else:
            # Busco en la tabla que coincidan el material y la ubicación
            cursor.execute("SELECT count(*) FROM MATERIALES WHERE CODIGO=? AND ORIGEN=?;",
                           (prod[a][1], listadoRTBS[i][0],))
            coinc_ubicacion = cursor.fetchall()
            print("coinc_origen", coinc_ubicacion[0][0])

            # Si NO EXISTE inserta un nuevo registro
            if coinc_ubicacion[0][0] == 0:
                print("Insertamos nuevo resgistro -> Existe pero no en la misma ubicación")
                sql = "INSERT INTO MATERIALES (CODIGO, ORIGEN, STOCK) VALUES ('" + str(prod[a][1]) + "', '" + str(
                    listadoRTBS[i][0]) + "', '" + str(1) + "')"
                cursor.executescript(sql)

            else:
                # SI EXISTE ese material y en la misma ubicación, incremento el STOCK
                print("Incrementamos el stock")
                cursor.execute("SELECT ID FROM MATERIALES WHERE CODIGO=? AND ORIGEN=?;",
                               (prod[a][1], listadoRTBS[i][0],))
                id = cursor.fetchall()
                print("id", id[0][0])
                sql = "UPDATE MATERIALES SET STOCK=STOCK+1 WHERE ID= '" + (str(id[0][0])) + "'"
                cursor.executescript(sql)


if __name__ == "__main__":
    #Prueba.__init__
    IncrementarTalonesFabricados.incrementar()
