import time
import requests

URL = "http://127.0.0.1:8000/posicao"
USUARIO = "jay"

#ponto de partida (recife) e quanto "andar" a cada envio
latitude = -8.0500
longitude = -34.8800
PASSO_LAT = 0.0002
PASSO_LON = 0.0002

print("Simulador iniciado. Aperte Ctrl+C para parar.")

while True:
    dados = {"usuario": USUARIO, "latitude": latitude, "longitude": longitude}
    resposta = requests.post(URL, json=dados, timeout=5)
    print(f"Enviado: {latitude:.4f}, {longitude:.4f} -> {resposta.status_code}")
    latitude += PASSO_LAT
    longitude += PASSO_LON 
    time.sleep(5)  # espera 5 segundos antes de enviar a próxima posição