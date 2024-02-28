import csv


def Caso1(nombreFichero):
    '''
    Ejecuta el caso 1, lee el fichero reto.csv,
    e imprime cada fila.
    '''
    with open(nombreFichero, newline = '') as archivoCsv:
        lectorCsv = csv.reader(archivoCsv)

        for fila in lectorCsv:
            print(fila)


def main():
    nombreFichero = 'reto.csv'
    Caso1(nombreFichero)

if __name__ == "__main__":
    main()