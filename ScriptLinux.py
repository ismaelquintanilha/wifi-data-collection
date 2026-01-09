import numpy as np
import matplotlib.pyplot as plt

# iw dev wlan0 scan
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

dados = [
    {'x':0,'y':0,'rssi_dbm':-44,'ruido_dbm':-96,'snr_db':52,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:26.587330')},
    {'x':0,'y':1,'rssi_dbm':-42,'ruido_dbm':-96,'snr_db':54,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:27.293347')},
    {'x':0,'y':2,'rssi_dbm':-40,'ruido_dbm':-96,'snr_db':56,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:27.509682')},
    {'x':0,'y':3,'rssi_dbm':-44,'ruido_dbm':-96,'snr_db':52,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:27.725087')},
    {'x':0,'y':4,'rssi_dbm':-43,'ruido_dbm':-96,'snr_db':53,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:27.915441')},

    {'x':1,'y':0,'rssi_dbm':-43,'ruido_dbm':-96,'snr_db':53,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:28.102400')},
    {'x':1,'y':1,'rssi_dbm':-43,'ruido_dbm':-96,'snr_db':53,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:28.301791')},
    {'x':1,'y':2,'rssi_dbm':-41,'ruido_dbm':-96,'snr_db':55,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:28.497943')},
    {'x':1,'y':3,'rssi_dbm':-39,'ruido_dbm':-96,'snr_db':57,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:28.698979')},
    {'x':1,'y':4,'rssi_dbm':-43,'ruido_dbm':-96,'snr_db':53,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:28.883454')},

    {'x':2,'y':0,'rssi_dbm':-43,'ruido_dbm':-96,'snr_db':53,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:29.079460')},
    {'x':2,'y':1,'rssi_dbm':-44,'ruido_dbm':-96,'snr_db':52,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:29.264564')},
    {'x':2,'y':2,'rssi_dbm':-45,'ruido_dbm':-96,'snr_db':51,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:29.456731')},
    {'x':2,'y':3,'rssi_dbm':-45,'ruido_dbm':-96,'snr_db':51,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:29.644360')},
    {'x':2,'y':4,'rssi_dbm':-45,'ruido_dbm':-96,'snr_db':51,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:29.827686')},

    {'x':3,'y':0,'rssi_dbm':-40,'ruido_dbm':-96,'snr_db':56,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:30.024787')},
    {'x':3,'y':1,'rssi_dbm':-42,'ruido_dbm':-96,'snr_db':54,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:30.221561')},
    {'x':3,'y':2,'rssi_dbm':-43,'ruido_dbm':-96,'snr_db':53,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:30.420955')},
    {'x':3,'y':3,'rssi_dbm':-45,'ruido_dbm':-96,'snr_db':51,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:30.620355')},
    {'x':3,'y':4,'rssi_dbm':-44,'ruido_dbm':-96,'snr_db':52,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:30.829650')},

    {'x':4,'y':0,'rssi_dbm':-43,'ruido_dbm':-96,'snr_db':53,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:31.051370')},
    {'x':4,'y':1,'rssi_dbm':-42,'ruido_dbm':-96,'snr_db':54,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:31.253480')},
    {'x':4,'y':2,'rssi_dbm':-44,'ruido_dbm':-96,'snr_db':52,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:31.459336')},
    {'x':4,'y':3,'rssi_dbm':-44,'ruido_dbm':-96,'snr_db':52,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:31.652666')},
    {'x':4,'y':4,'rssi_dbm':-43,'ruido_dbm':-96,'snr_db':53,'frequencia_mhz':5500,'bssid':'ac:b3:b5:f9:0e:58','timestamp':datetime.fromisoformat('2026-01-08 00:09:31.853527')},
]

xs = [d['x'] for d in dados]
ys = [d['y'] for d in dados]

max_x, max_y = max(xs), max(ys)

rssi = np.zeros((max_x+1, max_y+1))
noise = np.zeros_like(rssi)
snr = np.zeros_like(rssi)

for d in dados:
    x, y = d['x'], d['y']
    rssi[x,y] = d['rssi_dbm']
    noise[x,y] = d['ruido_dbm']
    snr[x,y] = d['snr_db']

plt.figure()
plt.imshow(rssi, origin='lower')
plt.colorbar(label='RSSI (dBm)')
plt.title('Radiomap RSSI')
plt.xlabel('Y')
plt.ylabel('X')
plt.show()

plt.figure()
plt.imshow(snr, origin='lower')
plt.colorbar(label='SNR (dB)')
plt.title('Mapa de SNR')
plt.xlabel('Y')
plt.ylabel('X')
plt.show()

plt.figure()
plt.imshow(noise, origin='lower')
plt.colorbar(label='Ruído (dBm)')
plt.title('Mapa de Ruído')
plt.xlabel('Y')
plt.ylabel('X')
plt.show()

variancia = np.var(rssi, axis=1)

plt.figure()
plt.plot(variancia, marker='o')
plt.title('Variância do RSSI por linha (X)')
plt.xlabel('X')
plt.ylabel('Variância')
plt.grid(True)
plt.show()

roteador_x, roteador_y = 1, 3

distancias = []
rssi_vals = []

for d in dados:
    dx = d['x'] - roteador_x
    dy = d['y'] - roteador_y
    distancias.append((dx**2 + dy**2)**0.5)
    rssi_vals.append(d['rssi_dbm'])

plt.figure()
plt.scatter(distancias, rssi_vals)
plt.xlabel('Distância')
plt.ylabel('RSSI (dBm)')
plt.title('RSSI vs Distância')
plt.grid(True)
plt.show()
