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

# Generar nuevas posiciones simuladas (10 movimientos randoms)
current_position = initial_position
for i in range(10):
    new_position = generate_random_position(current_position)
    positions.append(new_position)
    current_position = new_position

# Crear los datos del trayecto para la visualizacion
path_data = [{"path": [[pos[1], pos[0], pos[2]] for pos in positions]}]  # [Longitud, Latitud, Altitud]

# Función para crear un tooltip
def get_tooltip(path):
    def _get_tooltip(path_index):
        if path_index is None:
            return None
        point = path[path_index]

        # Imprimir los datos del punto para verificar la estructura
        print(point)

        # Opciones para acceder a la altitud (descomenta la que corresponda)
        altitude = float(point[2])  # Si la altitud está en el tercer índice
        # altitude = point['properties']['altitude']  # Si la altitud está dentro de un objeto 'properties'
        # altitude = point.altitude  # Si la altitud es una propiedad de nivel superior

        return f"Latitud: {point[1]:.6f}\nLongitud: {point[0]:.6f}\nAltitud: {altitude} m"
    return _get_tooltip

# Crear la capa PathLayer con tooltip
path_layer = pdk.Layer(
    "PathLayer",
    path_data,
    get_path="path",
    get_width=5,
    get_color=[255, 0, 0],  # Color rojo para la trayectoria
    width_min_pixels=3,
    extruded=True,  # Mostrar la altitud (altura)
    elevation_scale=200,  
    pickable=True,  
    auto_highlight=True,  
    get_tooltip=get_tooltip("path")
)

# Definir el mapa centrado en la posición inicial (CABA)
view_state = pdk.ViewState(
    latitude=initial_position[0],  
    longitude=initial_position[1],  
    zoom=13,  
    pitch=60,  
    bearing=45,  
)

# Crear el objeto de Deck.gl con la capa y la vista definida
r = pdk.Deck(
    layers=[path_layer],
    initial_view_state=view_state,
    # Especificar el contexto del tooltip para acceder a la altitud
    tooltip={"text": "{altitude}"}  
)

# Guardar el resultado como un archivo HTML pa
r.to_html("trayectoriaPydeck.html")

print("la trayectoria 3D del CubeSat esta lista para su visualizacion")