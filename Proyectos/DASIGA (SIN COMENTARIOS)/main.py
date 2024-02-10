
from flask import Flask, request, render_template
from agua import ejecutar_algoritmo_genetico
import agua

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultados')
def resultados():
    mejor_solucion = ejecutar_algoritmo_genetico()
    data_grafico = [{'distrito': distrito, 'asignacion': asignacion} for distrito, asignacion in mejor_solucion.items()]
    total_litros = sum(mejor_solucion.values())
    demanda = agua.demanda_agua
    total_demanda = sum(demanda)
    return render_template("resultados.html", mejor_solucion=mejor_solucion, data_grafico=data_grafico, total_litros=total_litros, demanda=demanda, total_demanda=total_demanda)


@app.route('/update-agua', methods=['POST'])
def update_agua():
    global agua_disponible
    agua_disponible = int(request.form['aguaDisponible'])
    agua.agua_disponible = agua_disponible 
    return 'Configuración exitosa.', 200

if __name__ == '__main__':
    app.run(debug=True)
