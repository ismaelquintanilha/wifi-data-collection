import subprocess
from datetime import datetime
import re

# (x,y) → RSSI_médio, variância, SNR_médio
dados = [{'sinal_pct': 75, 'rssi_dbm': -62.5, 'ruido_dbm': -90, 'snr_db': 27.5, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 19, 17, 620872), 'x': 0, 'y': 0},
{'sinal_pct': 62, 'rssi_dbm': -69.0, 'ruido_dbm': -90, 'snr_db': 21.0, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 19, 21, 839853), 'x': 0, 'y': 1},
{'sinal_pct': 62, 'rssi_dbm': -69.0, 'ruido_dbm': -90, 'snr_db': 21.0, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 19, 24, 736570), 'x': 0, 'y': 2},
{'sinal_pct': 62, 'rssi_dbm': -69.0, 'ruido_dbm': -90, 'snr_db': 21.0, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 19, 27, 336847), 'x': 0, 'y': 3},
{'sinal_pct': 57, 'rssi_dbm': -71.5, 'ruido_dbm': -90, 'snr_db': 18.5, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 19, 31, 938456), 'x': 0, 'y': 4},
{'sinal_pct': 57, 'rssi_dbm': -71.5, 'ruido_dbm': -90, 'snr_db': 18.5, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 19, 42, 872597), 'x': 1, 'y': 0},
{'sinal_pct': 60, 'rssi_dbm': -70.0, 'ruido_dbm': -90, 'snr_db': 20.0, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 19, 48, 859682), 'x': 1, 'y': 1},
{'sinal_pct': 67, 'rssi_dbm': -66.5, 'ruido_dbm': -90, 'snr_db': 23.5, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 19, 51, 906283), 'x': 1, 'y': 2},
{'sinal_pct': 53, 'rssi_dbm': -73.5, 'ruido_dbm': -90, 'snr_db': 16.5, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 19, 55, 132498), 'x': 1, 'y': 3},
{'sinal_pct': 53, 'rssi_dbm': -73.5, 'ruido_dbm': -90, 'snr_db': 16.5, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 19, 58, 677657), 'x': 1, 'y': 4},
{'sinal_pct': 70, 'rssi_dbm': -65.0, 'ruido_dbm': -90, 'snr_db': 25.0, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 20, 7, 403561), 'x': 2, 'y': 0},
{'sinal_pct': 70, 'rssi_dbm': -65.0, 'ruido_dbm': -90, 'snr_db': 25.0, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 20, 10, 946831), 'x': 2, 'y': 1},
{'sinal_pct': 70, 'rssi_dbm': -65.0, 'ruido_dbm': -90, 'snr_db': 25.0, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 20, 14, 306290), 'x': 2, 'y': 2},
{'sinal_pct': 70, 'rssi_dbm': -65.0, 'ruido_dbm': -90, 'snr_db': 25.0, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 20, 19, 29261), 'x': 2, 'y': 3},
{'sinal_pct': 86, 'rssi_dbm': -57.0, 'ruido_dbm': -90, 'snr_db': 33.0, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 20, 24, 104527), 'x': 2, 'y': 4},
{'sinal_pct': 86, 'rssi_dbm': -57.0, 'ruido_dbm': -90, 'snr_db': 33.0, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 20, 40, 451629), 'x': 3, 'y': 0},
{'sinal_pct': 86, 'rssi_dbm': -57.0, 'ruido_dbm': -90, 'snr_db': 33.0, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 20, 50, 764449), 'x': 3, 'y': 1},
{'sinal_pct': 86, 'rssi_dbm': -57.0, 'ruido_dbm': -90, 'snr_db': 33.0, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 20, 54, 191306), 'x': 3, 'y': 2},
{'sinal_pct': 89, 'rssi_dbm': -55.5, 'ruido_dbm': -90, 'snr_db': 34.5, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 21, 1, 494266), 'x': 3, 'y': 3},
{'sinal_pct': 89, 'rssi_dbm': -55.5, 'ruido_dbm': -90, 'snr_db': 34.5, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 21, 6, 968833), 'x': 3, 'y': 4},
{'sinal_pct': 86, 'rssi_dbm': -57.0, 'ruido_dbm': -90, 'snr_db': 33.0, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 21, 20, 867070), 'x': 4, 'y': 0},
{'sinal_pct': 86, 'rssi_dbm': -57.0, 'ruido_dbm': -90, 'snr_db': 33.0, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 21, 24, 222212), 'x': 4, 'y': 1},
{'sinal_pct': 86, 'rssi_dbm': -57.0, 'ruido_dbm': -90, 'snr_db': 33.0, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 21, 27, 248692), 'x': 4, 'y': 2},
{'sinal_pct': 86, 'rssi_dbm': -57.0, 'ruido_dbm': -90, 'snr_db': 33.0, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 21, 31, 81014), 'x': 4, 'y': 3},
{'sinal_pct': 86, 'rssi_dbm': -57.0, 'ruido_dbm': -90, 'snr_db': 33.0, 'frequencia': '5 GHz', 'canal': 36, 'bssid': '8c:68:3a:97:8d:60', 'timestamp': (2025, 12, 15, 18, 21, 35, 223718), 'x': 4, 'y': 4},
]

xs = [d['x'] for d in dados]
ys = [d['y'] for d in dados]

max_x = max(xs)
max_y = max(ys)

# 5 x 5
print(max_x+1," x ", max_y+1)

#Criar Matriz
matriz = [
    [None for _ in range(max_y + 1)]
    for _ in range(max_x + 1)
]

print("Matriz Inicial (Vazia):")
print(matriz)
print()

# Preencher Matriz com RSSI
for d in dados:
    x = d['x']
    y = d['y']
    matriz[x][y] = d['rssi_dbm']

print("Matriz Preenchida (RSSI):")
for linha in matriz:
    print(linha)
print()

# converter para numpy (mmelhor manipulação futura)
import numpy as np
rssi_matrix = np.array(matriz)

print("Matriz RSSI como Numpy Array:")
print(rssi_matrix.shape)
print()

# RADIOMAPS
# RSSI[x][y]
import matplotlib.pyplot as plt
plt.imshow(rssi_matrix, origin='lower')
plt.colorbar(label='RSSI (dBm)')
plt.title('Radiomap Wi-Fi (RSSI)')
plt.xlabel('Y')
plt.ylabel('X')
plt.show()
# cores quentes = sinal mais forte 
# cores frias = sinal fraco

#Variância simples por linha, mostra a instabilidade espacial.
variancia = np.var(rssi_matrix, axis=1)
print("Variância do RSSI por Linha (X):")
print(variancia)
print()
plt.plot(variancia, marker='o')
plt.title('Variação do RSSI por Linha (X)')
plt.xlabel('Linha (X)')
plt.ylabel('Variância do RSSI')
plt.grid(True)
plt.show()

#Lugar onde estar o roteador
roteador_x = 3
roteador_y = 0

#Cálculo de distância Euclidiana 
distancias = []
rssi_vals = []

for d in dados:
    dx = d['x'] - roteador_x
    dy = d['y'] - roteador_y
    distancia = (dx**2 + dy**2) ** 0.5

    distancias.append(distancia)
    rssi_vals.append(d['rssi_dbm'])

print("Distâncias e RSSI (primeiros 5):")
print(distancias[:5])
print(rssi_vals[:5])
plt.scatter(distancias, rssi_vals)
plt.xlabel('Distância (unidades da grade)')
plt.ylabel('RSSI (dBm)')
plt.title('RSSI vs Distância')
plt.grid(True)
plt.show()
print("Ta certo ser dos primeiros 5 pontos?")
print()

#Definir ruído médio
ruido_dbm = -90
#Calcular SNR
snr_vals = []

for rssi in rssi_vals:
    snr = rssi - ruido_dbm
    snr_vals.append(snr)
#HEATMAP SNR
snr_matrix = np.zeros_like(rssi_matrix)

for d in dados:
    x, y = d['x'], d['y']
    snr_matrix[x][y] = d['rssi_dbm'] - ruido_dbm
plt.imshow(snr_matrix, origin='lower')
plt.colorbar(label='SNR (dB)')
plt.title('Mapa de SNR')
plt.xlabel('Y')
plt.ylabel('X')
plt.show()

# Gráficos
#( ) Heatmap RSSI
#( ) Heatmap variância (multipercurso)
#( ) Heatmap ruído
#( ) Heatmap SNR
#( ) RSSI vs distância (opcional, mas forte)

# Métricas fisícas
#( ) RSSI médio global
#( ) RSSI mínimo e máximo
#( ) Variância média
#( ) Pontos mais instáveis (fading)
#( ) Zonas de sombra

#gerar tetxo par ia
import numpy as np

resumo = {}

resumo['rssi_medio'] = float(np.mean(rssi_matrix))
resumo['rssi_min'] = float(np.min(rssi_matrix))
resumo['rssi_max'] = float(np.max(rssi_matrix))

resumo['snr_medio'] = float(np.mean(snr_matrix))
resumo['snr_min'] = float(np.min(snr_matrix))
resumo['snr_max'] = float(np.max(snr_matrix))

resumo['variancia_rssi'] = float(np.var(rssi_matrix))

print("Resumo das Métricas Físicas:")
print(resumo)
print()

radiomap_texto = "Radiomap RSSI (dBm) por coordenada:\n"

for x in range(rssi_matrix.shape[0]):
    for y in range(rssi_matrix.shape[1]):
        radiomap_texto += f"({x},{y}): {rssi_matrix[x][y]} dBm\n"

print("Radiomap Texto:")
print(radiomap_texto)
print()

#Heatmap Ruído
ruido_matrix = np.zeros_like(rssi_matrix)

for d in dados:
    x, y = d['x'], d['y']
    ruido_matrix[x][y] = d['ruido_dbm']

plt.imshow(ruido_matrix, origin='lower')
plt.colorbar(label='Ruído (dBm)')
plt.title('Mapa de Ruído')
plt.xlabel('Y')
plt.ylabel('X')
plt.show()

