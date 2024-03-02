import csv
import json
import math
from haversine import haversine, Unit

import pandas as pd
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

    @param nombreFichero Nombre del fichero a leer
    
    '''
    
    with open(nombreFichero, newline = '') as archivoCsv:
        lectorCsv = csv.reader(archivoCsv)

        # Saltar la cabecera
        next(lectorCsv)

        # Guardamos los datos de cada matricula y la distancia recorrida en su posición anterior
        dictMatriculaDistancia = dict()
        dictMatriculaDistancia["vehiculos"] = {}

        # Iteramos las filas, guardando el acumulado de distancia por vehículo
        for fila in lectorCsv:
                
            matricula = fila[0]
            distancia = float(fila[3])

            if matricula in dictMatriculaDistancia["vehiculos"]:
                dictMatriculaDistancia["vehiculos"][matricula].append(distancia)
            else:
                dictMatriculaDistancia["vehiculos"][matricula] = list()
                dictMatriculaDistancia["vehiculos"][matricula].append(distancia)

        # Iteramos el diccionario e imprimimos el datos de la distancia de cada matricula:
        for matricula in dictMatriculaDistancia["vehiculos"]:
            sumaDistancia = sum (dictMatriculaDistancia["vehiculos"][matricula])
            print(f"El vehículo con la matricula: {matricula}, ha recorrido {str(sumaDistancia)} unidades de distancia")

def CalculaDistanciaCoordenadas(lat1, lon1, lat2, lon2):
    '''
    Devuelve la distancia de la tierra en kilómetros entre dos puntos.

    @param lat1 Latitud del primer punto
    @param lon1 Longitud del primer punto
    @param lat2 Latitud del segundo punto
    @param lon2 Longitud del segundo punto
    
    '''

    distancia = math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)

    return distancia


def Caso4(nombreFichero):
    '''
    Calcula la distancia recorrida por cada vehículo en función de las coordenadas 
    de cada posición.
    
    '''
    # Lee el archivo CSV
    df = pd.read_csv(nombreFichero, skiprows=1)

    # Ordena el DataFrame por la columna del tiempo (primero los registros más viejos)
    dfSorted = df.sort_values(df.columns[4], ascending=True)

    # Guardamos los datos de cada matricula y la distancia recorrida en su posición anterior
    dictMatriculaDistancia = dict()
    dictMatriculaDistancia["vehiculos"] = {}
    
    # Itera sobre el DataFrame ordenado sin mostrar el índice
    for fila in dfSorted.itertuples(index=False):
        matricula = fila[0]
        lat = float(fila[1])
        lon = float(fila[2])

        # Por cada vehículo, guardamos las localizaciones dónde ha estado
        if matricula in dictMatriculaDistancia["vehiculos"]:
            dictMatriculaDistancia["vehiculos"][matricula]["puntos"].append([lat,lon])
        else:
            dictMatriculaDistancia["vehiculos"][matricula] = {"puntos": [[lat, lon]]}


    distCoche = 0 # Distancia recorrida por cada coche
    '''
    Por cada coche calculamos la distancia recorrida entre cada posición en km.
    Las posiciones estarán ordenadas de más antiguas, a más recientes.
    '''
    for matriculaActual in dictMatriculaDistancia["vehiculos"]:
        for n in range(1, len(dictMatriculaDistancia["vehiculos"][matriculaActual]["puntos"]) ):
            lat1 = dictMatriculaDistancia["vehiculos"][matriculaActual]["puntos"][n-1][0]
            lon1 = dictMatriculaDistancia["vehiculos"][matriculaActual]["puntos"][n-1][1]
            lat2 = dictMatriculaDistancia["vehiculos"][matriculaActual]["puntos"][n][0]
            lon2 = dictMatriculaDistancia["vehiculos"][matriculaActual]["puntos"][n][1]
            dist = haversine((lat1, lon1), (lat2, lon2), unit=Unit.KILOMETERS)
            distCoche = distCoche + dist

        print(f"El coche con la matricula {matriculaActual}, ha recorrido {str(distCoche)} km.")
        distCoche = 0



def main():
    nombreFichero = 'reto.csv'
    Caso4(nombreFichero)

if __name__ == "__main__":
    main()