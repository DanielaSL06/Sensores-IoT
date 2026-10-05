from flask import Flask, request, jsonify
import json
import os
import csv # Para manejar el archivo CSV

app = Flask(__name__)

ARCHIVO_JSON = 'datosSensor.json'
ARCHIVO_CSV = 'datosSensor.csv' 

@app.route('/sensores', methods=['POST'])
def recibirDatos():
    datos = request.get_json()
    
    #Guardar en JSON
    if not os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, 'w') as f:
            json.dump([], f)
            
    with open(ARCHIVO_JSON, 'r') as f:
        contenido = json.load(f)
    
    contenido.append(datos)
    
    with open(ARCHIVO_JSON, 'w') as f:
        json.dump(contenido, f, indent=4)
        
    # Guardar en CSV
    existe_csv = os.path.exists(ARCHIVO_CSV)
    with open(ARCHIVO_CSV, mode='a', newline='') as f:
        escritor = csv.writer(f)
        # Si el archivo es nuevo, escribe los títulos: temperatura,humedad,timestamp
        if not existe_csv:
            escritor.writerow(['temperatura', 'humedad', 'timestamp'])
        
        # Escribe los datos en el orden correcto
        escritor.writerow([datos['temperatura'], datos['humedad'], datos['timestamp']])

    #Cálculos para mostrar en consola
    temps = [d['temperatura'] for d in contenido]
    hums = [d['humedad'] for d in contenido]
    
    print("\n--- DATOS  ---")
    print(f"Promedio Humedad: {sum(hums)/len(hums):.2f}")
    print(f"Temperatura Máxima: {max(temps)}")
    print(f"Temperatura Mínima: {min(temps)}")
    print("--------------------------\n")
        
    return jsonify({'mensaje': 'Dato guardado en JSON y CSV'}), 201

@app.route('/estadisticas', methods=['GET'])
def obtenerEstadisticas():
    if not os.path.exists(ARCHIVO_JSON):
        return jsonify({'error': 'No hay datos'}), 404
        
    with open(ARCHIVO_JSON, 'r') as f:
        datos = json.load(f)

    lista_temps = [d['temperatura'] for d in datos]
    lista_hums = [d['humedad'] for d in datos]

    return jsonify({
        'promedio_humedad': round(sum(lista_hums) / len(lista_hums), 2),
        'temperatura_maxima': max(lista_temps),
        'temperatura_minima': min(lista_temps),
        'total_registros': len(datos)
    }), 200

if __name__ == '__main__':
    app.run(debug=True)