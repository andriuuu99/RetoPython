from flask import Flask, request, jsonify
import pandas as pd


app = Flask(__name__)

# Lee el archivo CSV con los datos de los vehículos
df = pd.read_csv('caso5.csv')

@app.route('/<matricula>', methods=['GET'])
def obtener_ultima_posicion(matricula):
    # Filtra el DataFrame por la matrícula dada
    vehiculo = df[df['Matricula'] == matricula]
    
    # Verifica si se encontraron datos para la matrícula dada
    if vehiculo.empty:
        return jsonify({'mensaje': 'No se encontraron datos para la matrícula especificada'}), 404
    
    # Obtiene la posición del vehículo
    ultima_posicion = vehiculo[0]  
    
    # Devuelve la fecha de la última posición
    fecha_ultima_posicion = ultima_posicion['Fecha']
    return jsonify({'fecha_ultima_posicion': fecha_ultima_posicion}), 200

if __name__ == '__main__':
    app.run(debug=True)