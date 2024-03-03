from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)


@app.route('/<matricula>', methods=['GET'])
def ObtenerFechaUltimaPosicion(matricula):
    '''
    Obtiene la fecha de la última posición de un vehículo según su matricula.

    @param matricula Matricula del vehículo
    '''
    # Crea un cursor para ejecutar consultas SQL
    # Configura la conexión a la base de datos PostgreSQL
    conn = psycopg2.connect(
        dbname='root',
        user='root',
        password='root',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()

    try:
        # Ejecuta la consulta para obtener la fecha de la última posición
        cursor.execute("SELECT Fecha FROM fecha_ultima_posicion_vehiculo WHERE Matricula = %s", (matricula,))
        
        # Obtiene el resultado de la consulta
        fecha_ultima_posicion = cursor.fetchone()

        if fecha_ultima_posicion:
            return jsonify({'fecha_ultima_posicion': fecha_ultima_posicion[0]}), 200
        else:
            return jsonify({'mensaje': 'No se encontraron datos para la matrícula especificada'}), 404
    except Exception as e:
        # Si ocurre algún error, se maneja aquí
        return jsonify({'mensaje': str(e)}), 500
    finally:
        # Cierra el cursor y la conexión
        cursor.close()
        conn.close()


if __name__ == '__main__':
    app.run(debug=True)
