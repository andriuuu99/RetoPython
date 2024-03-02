from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)


@app.route('/<matricula>', methods=['GET'])
def ObtenerFechaUltimaPosicion(matricula):
    '''
    Obtiene la fecha de la última posición de un vehículo según su matricula.

    @param matricula Matricula del vehículo
    
    '''
    # Lee el archivo CSV con los datos de los vehículos
    df = pd.read_csv('caso5.csv')

    # Filtra el DataFrame por la matrícula dada
    vehiculo = df[df['Matricula'] == matricula]
    
    # Verifica si se encontraron datos para la matrícula dada
    if vehiculo.empty:
        return jsonify({'mensaje': 'No se encontraron datos para la matrícula especificada'}), 404
    
    # Devuelve la fecha de la última posición
    fecha_ultima_posicion = df.iloc[0]['Fecha']
    return jsonify({'fecha_ultima_posicion': fecha_ultima_posicion}), 200


if __name__ == '__main__':
    app.run(debug=True)
