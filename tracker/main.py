'''
opciones de librerias

geopy: To geolocate a query to an address, coordinates and measuring distances
~> pip install geopy

Folium:Para graficar las posiciones simuladas, nos permite ver la posicion en un grafico 2d en tiempo real
~> pip install folium

'''

import time
import random
import folium
import geopy    

# Punto inicial (Lat, Long)
initial_position = (51.5074, -0.1278)  # Londres como ejemplo

# Crear un mapa centrado en la posición inicial
mapa = folium.Map(location=initial_position, zoom_start=13)

# Añadir marcador inicial
folium.Marker(initial_position, popup="Posición inicial").add_to(mapa)

# Guardar el mapa en un archivo HTML
mapa.save("cube_sat_mapa.html")

def simulate_gps_movement(start_pos, num_points=100):
    positions = [start_pos]
    
    for _ in range(num_points):
        # Simulación de movimiento pequeño (en este caso, alrededor de la posición inicial)
        new_lat = positions[-1][0] + random.uniform(-0.0005, 0.0005)
        new_long = positions[-1][1] + random.uniform(-0.0005, 0.0005)
        new_position = (new_lat, new_long)
        positions.append(new_position)
        time.sleep(0.1)  # Simular recepción de datos cada 100ms
    
    return positions

# Generar posiciones simuladas
positions = simulate_gps_movement(initial_position)

# Crear un nuevo mapa con las posiciones simuladas
mapa_trayectoria = folium.Map(location=initial_position, zoom_start=13)

# Añadir marcadores de trayectoria
for pos in positions:
    folium.Marker(pos).add_to(mapa_trayectoria)

# Guardar el nuevo mapa con la trayectoria
mapa_trayectoria.save("cube_sat_trayectoria.html")

print("Trayectoria guardada en cube_sat_trayectoria.html")
