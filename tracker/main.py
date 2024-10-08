import time
import random
import folium

# Punto inicial (Lat, Long)
initial_position = (51.5074, -0.1278)  # Londres como ejemplo

# Crear un mapa centrado en la posición inicial
mapa = folium.Map(location=initial_position, zoom_start=13)

# Añadir marcador inicial
folium.Marker(initial_position, popup="Posición inicial").add_to(mapa)

# Guardar el mapa inicial en un archivo HTML
mapa.save("cube_sat_mapa_inicial.html")

# Función para generar una nueva posición simulada
def generate_random_position(last_position):
    # Variar latitud y longitud ligeramente
    new_lat = last_position[0] + random.uniform(-0.001, 0.001)  # Cambios pequeños
    new_long = last_position[1] + random.uniform(-0.001, 0.001)
    return (new_lat, new_long)

# Lista para almacenar las posiciones y formar la trayectoria
positions = [initial_position]

# Usar el bucle for o while para generar nuevas coordenadas
current_position = initial_position

for i in range(10):  # Simulamos 10 movimientos
    # Generar una nueva posición
    new_position = generate_random_position(current_position)
    positions.append(new_position)

    # Mostrar la posición actual (opcional)
    print(f"Posición {i+1}: {new_position}")

    # Añadir la nueva posición al mapa
    folium.Marker(new_position, popup=f"Posición {i+1}").add_to(mapa)

    # Dibujar la línea entre la posición anterior y la nueva posición
    folium.PolyLine(positions, color="blue", weight=2.5, opacity=1).add_to(mapa)

    # Actualizar la posición actual
    current_position = new_position

    # Esperar un segundo antes de generar la siguiente posición
    time.sleep(1)

# Guardar el nuevo mapa con las posiciones y líneas
mapa.save("cube_sat_trayectoria_con_lineas.html")

print("Trayectoria guardada en cube_sat_trayectoria_con_lineas.html")
