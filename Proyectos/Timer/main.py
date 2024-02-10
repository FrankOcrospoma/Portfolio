from flask import Flask, request, jsonify, render_template
import psycopg2

app = Flask(__name__, static_url_path='/static')

# Configura la conexión a la base de datos
conn = psycopg2.connect(
    dbname='timer',
    user='postgres',
    password='frank2003',
    host='localhost',
    port='5432'  # Puerto predeterminado de PostgreSQL
)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/cubo')
def cubo():
    return render_template('cubo.html')

@app.route('/guardar-tiempo', methods=['POST'])
def guardar_tiempo():
    data = request.get_json()
    time = data['time']
    scramble = data['scramble']
    
    # Insertar el tiempo en la base de datos
    cur = conn.cursor()
    cur.execute("INSERT INTO times (session_id, time_interval, scramble) VALUES (%s, %s, %s)", (1, time, scramble))
    conn.commit()
    cur.close()

    return jsonify({"message": "Tiempo guardado exitosamente"}), 200
@app.route('/mejortiempo')
def get_mejores():
    # Ejecutar una consulta para obtener los tiempos de la base de datos
    cur = conn.cursor()
    cur.execute("SELECT MIN(time_interval) AS mejortiempo, MIN(ao5) AS mejorao5, MIN(ao12) AS mejora12,MIN(ao100) AS mejora100 FROM times WHERE session_id = 1")
    times = cur.fetchall()
    cur.close()
    
    # Convertir los tiempos en una lista de diccionarios
    mejor = [{"mejortiempo": time[0], "mejorao5": time[1], "mejorao12": time[2],  "mejorao100": time[3]} for time in times]

    return jsonify(mejor)

@app.route('/times')
def get_times():
    # Ejecutar una consulta para obtener los tiempos de la base de datos
    cur = conn.cursor()
    cur.execute("SELECT time_interval, ao5, ao12, ao100, indice FROM times ORDER BY solve_date DESC")
    times = cur.fetchall()
    cur.close()
    
    # Convertir los tiempos en una lista de diccionarios
    times_list = [{"time_interval": time[0], "ao5": time[1], "ao12": time[2], "ao100": time[3], "indice": time[4]} for time in times]

    return jsonify(times_list)
@app.route('/get_time_difference')
def get_time_difference():
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            (SELECT time_interval FROM times ORDER BY solve_date DESC LIMIT 1) - 
            (SELECT time_interval FROM times ORDER BY solve_date DESC LIMIT 1 OFFSET 1) AS difference;
    """)
    
    # Obtener el resultado
    difference = cur.fetchone()[0]

    cur.close()

    # Devolver la diferencia como JSON
    return jsonify({'difference': difference})


if __name__ == '__main__':
    app.run(debug=True)
