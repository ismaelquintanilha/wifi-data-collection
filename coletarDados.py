# Tabela de medições
# Objetivo:  x | y | sinal_% | RSSI_dBm | timestamp

import subprocess
from datetime import datetime
import re

# ==== TESTE (Saída única) ====
# # obter informações da interface Wi-Fi no Windows
# saida = subprocess.check_output(
#     "netsh wlan show interfaces",
#     shell=True,
#     encoding="latin-1",
#     errors="ignore"
# )

# sinal_pct = None

# # extrair o valor do sinal em porcentagem 
# for linha in saida.splitlines():
#     if "Sinal" in linha:
#         numeros = re.findall(r"\d+", linha)
#         if numeros:
#             sinal_pct = int(numeros[0])
#             break

# # tratamento de erro
# if sinal_pct is None:
#     raise ValueError("Não foi possível extrair o sinal Wi-Fi.")

# # calcular RSSI estimado em dBm (já que o Windows não fornece diretamente)
# rssi_dbm = (sinal_pct / 2) - 100

# print("Sinal (%):", sinal_pct)
# print("RSSI estimado (dBm):", rssi_dbm)
# print("Timestamp:", datetime.now())

# ==== CÓDIGO PRINCIPAL ====

# grade fixa 5x5 (x: 0-4, y:0-4)
GRID_X = 3
GRID_Y = 3
ARQUIVO = "medicoes_wifi.csv"
RUIDO_DBM = -90

# assume uma ordem (ex: 0,0 -> 0,1 -> ... -> 4,4)
dados = []

for x in range(GRID_X):
    for y in range(GRID_Y):
        input(f"Posicione-se no ponto ({x},{y}) e pressione ENTER")

        saida = subprocess.check_output(
        ["netsh", "wlan", "show", "interfaces"],
        encoding="latin1"
        )

        sinal = re.search(r"Sinal\s*:\s*(\d+)%", saida)
        canal = re.search(r"Canal\s*:\s*(\d+)", saida)
        bssid = re.search(r"BSSID\s*:\s*([0-9a-fA-F:]{17})", saida)

        if not sinal or not canal or not bssid:
            raise ValueError("Falha ao extrair dados do Wi-Fi")

        sinal_pct = int(sinal.group(1))
        canal = int(canal.group(1))
        bssid = bssid.group(1)

        # Conversão padrão aceita
        rssi_dbm = (sinal_pct / 2) - 100

        # Frequência inferida
        frequencia = "2.4 GHz" if canal <= 14 else "5 GHz"

        # SNR calculado
        snr_db = rssi_dbm - RUIDO_DBM

        info = {
        "sinal_pct": sinal_pct,
        "rssi_dbm": rssi_dbm,
        "ruido_dbm": RUIDO_DBM,
        "snr_db": snr_db,
        "frequencia": frequencia,
        "canal": canal,
        "bssid": bssid,
        "timestamp": datetime.now()
        }
        info["x"] = x
        info["y"] = y
        dados.append(info)
        print("Coletado:", info)

# salvar tabela
import csv
with open(ARQUIVO, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=dados[0].keys())
    writer.writeheader()
    writer.writerows(dados)

print(f"\nArquivo {ARQUIVO} salvo com sucesso!")