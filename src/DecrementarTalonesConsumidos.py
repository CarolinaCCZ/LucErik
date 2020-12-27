# -*- coding: utf-8 -*-
"""
Clase que decrementa en 2 el número de talones cada vez que se fabrica una cubierta
e incrementa en 1 el número de cubiertas producidas si hay material para ello en la máquina.

@author: Carolina Colina Zamorano
"""

import sqlite3


class DecrementarTalonesConsumidos:

    @staticmethod
    def decrementar():

        # Conexión con la base de datos
        global con, cursor
        try:
            con = sqlite3.connect('Y:\LucErik.db')
            cursor = con.cursor()
        except sqlite3.OperationalError:
            sys.exit()

        cursor.execute("SELECT * FROM MAQUINAS ORDER BY ID ASC")
        cubiertas = cursor.fetchall()
        print("Cubiertas: ", cubiertas)

        for i in range(len(cubiertas)):
            # Compruebo si todavía hay que seguir produciendo
            if cubiertas[i][5] < cubiertas[i][4]:
                print("")
                print("i", i)
                print("Hay que seguir produciendo", cubiertas[i][5], "<", cubiertas[i][4])

                # Compruebo si hay talones en la máquina para producir
                sql = "SELECT * FROM HUECOS WHERE ID= '" + cubiertas[i][0] + "' ORDER BY ID ASC"
                cursor.execute(sql)
                talones = cursor.fetchall()

                print("Talones: ", talones)
                print("Máquina: ", cubiertas[i][0])

                # Si en el primer hueco no hay talones, inserto la palabra 'VACIO' en el hueco 'H1'
                if talones[0][3] == 0:
                    sql = "UPDATE HUECOS SET MATERIAL='VACIO' WHERE HUECO='H1' AND ID='" + cubiertas[i][0] + "'"
                    cursor.executescript(sql)
                    sql = "SELECT * FROM HUECOS WHERE ID= '" + cubiertas[i][0] + "' ORDER BY ID ASC"
                    cursor.execute(sql)
                    talones = cursor.fetchall()

                # Si hay 2 o más talones en el primer hueco y si es de ese material:
                # Incremento en 1 la producción de cubiertas
                # Decremento en 2 el consumo de talones
                print("cubiertas[i][2]", cubiertas[i][2])

                # Si el número de talones es mayor que 2 y coincide el material
                if talones[0][3] >= 2 and talones[0][2] == cubiertas[i][2]:
                    print("Incremento en 1 la producción de cubiertas")
                    sql = "UPDATE MAQUINAS SET PROD_ACTUAL=PROD_ACTUAL+1 WHERE ID='" + cubiertas[i][0] + "'"
                    cursor.executescript(sql)

                    print("Decremento en 2 el consumo de talones")
                    sql = "UPDATE HUECOS SET CANTIDAD=CANTIDAD-2 WHERE HUECO='H1' AND ID='" + cubiertas[i][0] + "'"
                    cursor.executescript(sql)

                # Si no hay talones en el primer hueco o no es del material que se está produciendo,
                # Recorro los huecos a ver si hay material en otro hueco
                else:
                    b = 1
                    while b < (len(talones)):
                        print("talones[b][2]", talones[b][2])

                        # Si lo encuentro intercambio los huecos
                        if talones[b][2] == cubiertas[i][2]:
                            # Guardo lo que hay en el primer hueco
                            material = talones[0][2]
                            print("MATERIAL:", material)
                            cantidad = talones[0][3]
                            print("CANTIDAD:", cantidad)

                            # Guardo en el primer hueco lo que he encontrado
                            sql = "UPDATE HUECOS SET MATERIAL= '" + talones[b][2] + "', CANTIDAD= '" + str(
                                talones[b][3]) + "' WHERE HUECO='H1' AND ID='" + cubiertas[i][0] + "' "
                            cursor.executescript(sql)

                            # Guardo en el hueco donde lo he encontrado lo que había en el primer hueco
                            sql = "UPDATE HUECOS SET MATERIAL='" + material + "', CANTIDAD= '" + str(
                                cantidad) + "' WHERE HUECO='" + talones[b][1] + "' AND ID='" + cubiertas[i][0] + "'"
                            cursor.executescript(sql)

                            b = b + 1

                        else:
                            b = b + 1

            # Si se ha llegado al tope de cubiertas del primer material, es decir, del que se está produciendo
            # Cambio los materiales: En MAT_ACTUAL se coloca MAT_PROX
            else:
                print("Si ya se han hecho todas las cubiertas de esa medida", cubiertas[i][5], "=", cubiertas[i][4])
                print("Cambio los materiales de la máquina")
                sql = "UPDATE MAQUINAS SET MAT_ACTUAL=MAT_PROX WHERE ID='" + cubiertas[i][0] + "'"
                cursor.executescript(sql)
                sql = "UPDATE MAQUINAS SET TOTALES_ACTUAL=TOTALES_PROX WHERE ID='" + cubiertas[i][0] + "'"
                cursor.executescript(sql)
                sql = "UPDATE MAQUINAS SET PROD_ACTUAL=0 WHERE ID='" + cubiertas[i][0] + "'"
                cursor.executescript(sql)
                sql = "UPDATE MAQUINAS SET MAT_PROX='NULL' WHERE ID='" + cubiertas[i][0] + "'"
                cursor.executescript(sql)
                sql = "UPDATE MAQUINAS SET TOTALES_PROX=0 WHERE ID= '" + cubiertas[i][0] + "' "
                cursor.executescript(sql)

                # Una vez cambiado el material, vuelvo a recuperar los datos actuales
                sql = "SELECT * FROM MAQUINAS WHERE ID = '" + cubiertas[i][0] + "' "
                cursor.execute(sql)
                cubiertas = cursor.fetchall()

        con.close()


if __name__ == "__main__":
    DecrementarTalonesConsumidos.decrementar()
