#ANTES DE RODAR O CÓDIGO NO LINUX:
#sudo apt install wireless-tools iw
#sudo python3 ColetarDadosLinux.py

# Tabela de medições
# Objetivo:  x | y | sinal_% | RSSI_dBm | timestamp

import subprocess
import re
from datetime import datetime
import csv

# grade fixa 5x5 (x: 0-4, y:0-4)
INTERFACE = "wlp2s0"      
GRID_X = 5
GRID_Y = 5
ARQUIVO = "medicoes_wifi_linux.csv"

# assume uma ordem (ex: 0,0 -> 0,1 -> ... -> 4,4)
dados = []

for x in range(GRID_X):
    for y in range(GRID_Y):
        input(f"Posicione-se no ponto ({x},{y}) e pressione ENTER")

        saida = subprocess.check_output(
        ["iwconfig", INTERFACE],
        encoding="utf-8",
        errors="ignore"
        )   

        rssi = re.search(r"Signal level=(-?\d+)\s*dBm", saida)
        ruido = re.search(r"Noise level=(-?\d+)\s*dBm", saida)
        bssid = re.search(r"Access Point:\s*([0-9A-Fa-f:]{17})", saida)
        freq = re.search(r"Frequency:(\d+\.\d+)\s*GHz", saida)

        if not rssi or not ruido or not bssid or not freq:
            raise ValueError("Não foi possível extrair dados do Wi-Fi")

        rssi_dbm = int(rssi.group(1))
        ruido_dbm = int(ruido.group(1))
        snr_db = rssi_dbm - ruido_dbm

        freq_ghz = float(freq.group(1))
        frequencia = "2.4 GHz" if freq_ghz < 3 else "5 GHz"

        info =  {
            "rssi_dbm": rssi_dbm,
            "ruido_dbm": ruido_dbm,
            "snr_db": snr_db,
            "frequencia": frequencia,
            "bssid": bssid.group(1),
            "timestamp": datetime.now()
        }

        info["x"] = x
        info["y"] = y
        dados.append(info)
        print("Coletado:", info)

# salvar tabela
with open(ARQUIVO, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=dados[0].keys())
    writer.writeheader()
    writer.writerows(dados)

print(f"\nArquivo {ARQUIVO} salvo com sucesso!")