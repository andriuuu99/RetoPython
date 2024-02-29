import csv
import json

def Caso1(nombreFichero):
    '''
    Ejecuta el caso 1, lee el fichero reto.csv,
    e imprime cada fila.

    @param nombreFichero Nombre del fichero a leer
    '''
    with open(nombreFichero, newline = '') as archivoCsv:
        lectorCsv = csv.reader(archivoCsv)

        # Saltar la cabecera
        next(lectorCsv)


        for fila in lectorCsv:
            print(fila)


def Caso2(nombreFichero):
    '''
    Lee el fichero CSV, convierte cada línea a un
    JSON e imprímelo.

    @param nombreFichero Nombre del fichero a leer
    '''
    with open(nombreFichero, newline = '') as archivoCsv:
        lectorCsv = csv.reader(archivoCsv)

        # Saltar la cabecera
        next(lectorCsv)

        for fila in lectorCsv:

            # Guardamos los datos en un diccionario
            dictDatos = {

                "matricula" : fila[0],
                "latitud": fila[1],
                "longitud": fila[2],
                "distance": fila[3],
                "post_date": fila[4],


            }
            #Guardamos en un json e imprimimos el resultado
            jsonResultante = json.dumps(dictDatos)
            print(jsonResultante)


def Caso3(nombreFichero):
    '''
    Calcula el sumatorio de distancias recorridas por cada coche
    según el campo distacia del fichero de datos.
    
    '''
    with open(nombreFichero, newline = '') as archivoCsv:
        lectorCsv = csv.reader(archivoCsv)

        # Saltar la cabecera
        next(lectorCsv)

        # Guardamos los datos de cada matricula y la distancia recorrida en su posición anterior
        dictMatriculaDistancia = dict()
    
        # Iteramos las filas, guardando el acumulado de distancia por vehículo
        for fila in lectorCsv:
            matricula = fila[0]
            distancia = float(fila[3])

            if matricula in dictMatriculaDistancia:
                dictMatriculaDistancia[matricula] = dictMatriculaDistancia[matricula] + distancia
            else:
                dictMatriculaDistancia[matricula] = distancia

        # Iteramos el diccionario e imprimimos el datos de la distancia de cada matricula:
        for matricula in dictMatriculaDistancia:
            print(f"El vehículo con la matricula: {matricula}, ha recorrido {str(dictMatriculaDistancia[matricula])} unidades de distancia")
def main():
    nombreFichero = 'reto.csv'
    Caso3(nombreFichero)

if __name__ == "__main__":
    main()