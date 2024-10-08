import time
import random
import folium
from geopy.distance import geodesic

# Punto inicial (Lat, Long, Alt)
initial_position = (-34.5895, -58.4665, 30)  # CABA con 100 metros de altitud como ejemplo

# Crear un mapa centrado en la posición inicial (ignora la altitud para visualización en el mapa)
mapa = folium.Map(location=initial_position[:2], zoom_start=13)

# Añadir marcador inicial
folium.Marker(initial_position[:2], popup="Posición inicial (Altitud: 100m)").add_to(mapa)

# Guardar el mapa inicial en un archivo HTML
mapa.save("cube_sat_mapa_inicial.html")

# Función para generar una nueva posición simulada (con altitud)
def generate_random_position(last_position):
    # Variar latitud, longitud y altitud ligeramente
    new_lat = last_position[0] + random.uniform(-0.001, 0.001)  # Cambios pequeños en latitud
    new_long = last_position[1] + random.uniform(-0.001, 0.001)  # Cambios pequeños en longitud
    new_alt = last_position[2] + random.uniform(-10, 10)  # Cambios de altitud (sube o baja entre -10m y 10m)
    return (new_lat, new_long, new_alt)

# Lista para almacenar las posiciones y formar la trayectoria
positions = [initial_position]

# Usar el bucle para generar nuevas coordenadas
current_position = initial_position

for i in range(10):  # 10 movimientos
    # Generar una nueva posición
    new_position = generate_random_position(current_position)
    positions.append(new_position)

    # Calcular la distancia 2D (latitud, longitud)
    distance_2d = geodesic(current_position[:2], new_position[:2]).meters

    # Calcular la diferencia de altitud
    altitude_difference = abs(current_position[2] - new_position[2])

    # Calcular la distancia total
    distance_3d = (distance_2d**2 + altitude_difference**2) ** 0.5

    # Mostrar la distancia por consola
    print(f"Distancia 3D entre punto {i} y punto {i+1}: {distance_3d:.2f} metros")

    # Añadir la nueva posición al mapa (latitud y longitud)
    folium.Marker(new_position[:2], popup=f"Posición {i+1} (Altitud: {new_position[2]:.2f}m)").add_to(mapa)

    # Dibujar la línea entre la posición anterior y la nueva posición
    folium.PolyLine([pos[:2] for pos in positions], color="blue", weight=2.5, opacity=1).add_to(mapa)

    # Actualizar la posición actual
    current_position = new_position

    # Esperar un segundo antes de generar la siguiente posición
    time.sleep(1)

# Guardar el nuevo mapa con las posiciones y líneas
mapa.save("cube_sat_trayectoria_con_altura.html")

print("Trayectoria con altitud guardada en cube_sat_trayectoria_con_altura.html")
