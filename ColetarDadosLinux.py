#ANTES DE RODAR O CÓDIGO NO LINUX:
#sudo apt install iw
#sudo python3 ColetarDadosLinux.py

# Tabela de medições
# Objetivo:  x | y | sinal_% | RSSI_dBm | timestamp
import subprocess
import re
from datetime import datetime
import csv
INTERFACE = "wlp1s0"
GRID_SIZE = 5
ARQUIVO = "medicoes_wifi_linux.csv"

with open(ARQUIVO, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "x",
        "y",
        "rssi_dbm",
        "ruido_dbm",
        "snr_db",
        "frequencia_mhz",
        "bssid",
        "timestamp"
    ])

    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):

            input(f"Posicione-se no ponto ({x},{y}) e pressione ENTER")

            saida_link = subprocess.check_output(
                ["iw", "dev", INTERFACE, "link"],
                encoding="utf-8",
                errors="ignore"
            )

            rssi = int(re.search(r"signal:\s*(-\d+)", saida_link).group(1))
            freq = int(float(re.search(r"freq:\s*([\d\.]+)", saida_link).group(1)))
            bssid = re.search(r"Connected to\s+([0-9a-f:]+)", saida_link).group(1)

            saida_survey = subprocess.check_output(
                ["iw", "dev", INTERFACE, "survey", "dump"],
                encoding="utf-8",
                errors="ignore"
            )

            ruido = None
            blocos = saida_survey.split("Survey data from")

            for bloco in blocos:
                if str(freq) in bloco:
                    ruido = int(re.search(r"noise:\s*(-\d+)", bloco).group(1))
                    break

            if ruido is not None:
                snr = rssi - ruido
            else:
                snr = None

            writer.writerow([
                x,
                y,
                rssi,
                ruido,
                snr,
                freq,
                bssid,
                datetime.now()
            ])

            print(
                f"Coletado ({x},{y}) | "
                f"RSSI={rssi} dBm | "
                f"Ruído={ruido} dBm | "
                f"SNR={snr} dB | "
                f"Freq={freq} MHz"
            )

print("\nArquivo medicoes_wifi_linux.csv gerado com sucesso!")