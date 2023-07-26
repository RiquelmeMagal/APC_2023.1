import math

def distancia(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

coordenada_x_a = float(input())
coordenada_y_a = float(input())
coordenada_z_a = float(input())
coordenada_x_b = float(input())
coordenada_y_b = float(input())
coordenada_z_b = float(input())

total_distancia = distancia(coordenada_x_a, coordenada_y_a, coordenada_z_a, coordenada_x_b, coordenada_y_b, coordenada_z_b)

print(total_distancia)