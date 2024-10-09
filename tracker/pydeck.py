import pydeck as pdk
import random

# Punto inicial (Lat, Long, Alt) - CABA con 30 metros de altitud
initial_position = (-34.5895, -58.4665, 30)

# Lista para almacenar las posiciones y formar la trayectoria
positions = [initial_position]



# Función para generar una nueva posición simulada (con altitud errática)
def generate_random_position(last_position):
    # Variar latitud, longitud y altitud más drásticamente
    new_lat = last_position[0] + random.uniform(-0.005, 0.005)  # Variaciones mayores en latitud
    new_long = last_position[1] + random.uniform(-0.005, 0.005)  # Variaciones mayores en longitud
    new_alt = last_position[2] + random.uniform(-50, 50)  # Variaciones más grandes en altitud (hasta 50 metros)
    return (new_lat, new_long, new_alt)

# Generar nuevas posiciones simuladas (10 movimientos erráticos)
current_position = initial_position
for i in range(10):
    new_position = generate_random_position(current_position)
    positions.append(new_position)
    current_position = new_position

# Crear los datos del trayecto para la visualización en pydeck (Longitud, Latitud, Altitud)
path_data = [{"path": [[pos[1], pos[0], pos[2]] for pos in positions]}]  # [Longitud, Latitud, Altitud]

# Crear la capa PathLayer para mostrar la trayectoria del CubeSat con altitud
path_layer = pdk.Layer(
    "PathLayer",
    path_data,
    get_path="path",
    get_width=5,
    get_color=[255, 0, 0],  # Color rojo para la trayectoria
    width_min_pixels=3,
    extruded=True,  # Mostrar la altitud (altura)
    elevation_scale=200,  # Escalar la altitud para mayor visibilidad
)

# Definir el mapa centrado en la posición inicial (CABA)
view_state = pdk.ViewState(
    latitude=initial_position[0],  # Latitud inicial
    longitude=initial_position[1],  # Longitud inicial
    zoom=13,  # Nivel de zoom
    pitch=60,  # Inclinación para ver la trayectoria en 3D
    bearing=45,  # Girar el ángulo para una mejor perspectiva
)

# Crear el objeto de Deck.gl con la capa y la vista definida
r = pdk.Deck(layers=[path_layer], initial_view_state=view_state, tooltip={"text": "Altitud: {altitude}"})

# Guardar el resultado como un archivo HTML para visualizar en el navegador
r.to_html("trayectoria_cubesat_erratica_3d.html")

print("Trayectoria 3D del CubeSat errático guardada en trayectoria_cubesat_erratica_3d.html")
