ejercicio1/main.py.
def limpiar_registro_sensor(registro_raw):
    sensor_id = registro_raw.get("sensor_id", "").strip()
    temp_str = registro_raw.get("temperatura", "0")
    temperatura = float(str(temp_str).replace("C", "").replace("c", "").strip())
    ubicacion = registro_raw.get("ubicacion", "").strip()
    if not ubicacion:
        ubicacion = "Sin ubicacion"
    return {"sensor_id": sensor_id, "temperatura": temperatura, "ubicacion": ubicacion}

def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    lista_sensores_alerta = []
    suma_temp = 0
    for sensor in lista_sensores_limpios:
        suma_temp += sensor["temperatura"]
        if sensor["temperatura"] > umbral_temperatura:
            lista_sensores_alerta.append(sensor["sensor_id"])
    promedio_temperatura = suma_temp / len(lista_sensores_limpios) if lista_sensores_limpios else 0
    return (lista_sensores_alerta, promedio_temperatura)

if __name__ == "__main__":
    sensores_raw = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": "SENSOR-002", "temperatura": "31.2C", "ubicacion": ""}
    ]
    sensores_limpios = [limpiar_registro_sensor(s) for s in sensores_raw]
    alerta, promedio = generar_resumen_sensores(sensores_limpios, 30)
    print("--- REPORTE ECOTECH ---")
    print(f"Sensores en alerta: {alerta}")
    print(f"Promedio temperatura: {promedio:.2f}°C")

