import random
import plotly.graph_objects as go

# Punto inicial (Lat, Long, Alt)
initial_position = (-34.5895, -58.4665, 30)  # CABA

# Lista para almacenar las posiciones y formar la trayectoria
positions = [initial_position]

# Función para generar una nueva posición simulada (con altitud)
def generate_random_position(last_position):
    # Variar latitud, longitud y altitud ligeramente
    new_lat = last_position[0] + random.uniform(-0.001, 0.001)  # Cambios pequeños en latitud
    new_long = last_position[1] + random.uniform(-0.001, 0.001)  # Cambios pequeños en longitud
    new_alt = last_position[2] + random.uniform(-10, 10)  # Cambios de altitud (sube o baja entre -10m y 10m)
    return (new_lat, new_long, new_alt)

# Usar el bucle para generar nuevas coordenadas
current_position = initial_position

for i in range(10):  # 10 movimientos simulados
    # Generar una nueva posición
    new_position = generate_random_position(current_position)
    positions.append(new_position)
    current_position = new_position

# Extraer listas de latitudes, longitudes y altitudes
latitudes = [pos[0] for pos in positions]
longitudes = [pos[1] for pos in positions]
altitudes = [pos[2] for pos in positions]

# Crear la figura 3D con Plotly
fig = go.Figure(data=[go.Scatter3d(
    x=longitudes,  # Eje X: longitud
    y=latitudes,   # Eje Y: latitud
    z=altitudes,   # Eje Z: altitud
    mode='lines+markers',
    line=dict(color='blue', width=2),
    marker=dict(size=5, color='red'),
)])

# Establecer etiquetas y título
fig.update_layout(
    scene=dict(
        xaxis_title='Longitud',
        yaxis_title='Latitud',
        zaxis_title='Altitud (m)'
    ),
    title="Simulación de Trayectoria en 3D",
)

# Mostrar el gráfico interactivo en el navegador
fig.show()
