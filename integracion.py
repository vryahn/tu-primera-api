"""Tu primera integración: lee el clima de una API y le avisa a otro sistema.

Uso:
    pip install requests
    python integracion.py
"""
import requests

# Abre https://webhook.site, copia tu URL única y pégala aquí.
WEBHOOK_URL = "TU_URL_DE_WEBHOOK"

# 1. GET: le preguntamos a Open-Meteo el clima de CDMX.
clima = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={"latitude": 19.43, "longitude": -99.13, "current_weather": "true"},
    timeout=10,
)
print("Open-Meteo respondió:", clima.status_code)
clima.raise_for_status()  # si no fue 2xx, el programa se detiene aquí
temp = clima.json()["current_weather"]["temperature"]
print("Temperatura en CDMX:", temp)

# 2. POST: le avisamos al otro sistema, con los datos en un body JSON.
aviso = requests.post(WEBHOOK_URL, json={"ciudad": "CDMX", "temp": temp}, timeout=10)
print("El webhook respondió:", aviso.status_code)
