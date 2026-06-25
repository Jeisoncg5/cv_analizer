import json
import os
import re

import requests
from dotenv import load_dotenv

from models.cv_model import AnalisisCV
from prompts.cv_prompts import OLLAMA_PROMPT

load_dotenv()

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
REQUEST_TIMEOUT = int(os.getenv("OLLAMA_TIMEOUT", "120"))


def generar_texto_ollama(prompt: str) -> str:
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "format": "json",
        "options": {
            "temperature": 0.2,
        },
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()

    data = response.json()
    texto = data.get("response", "").strip()
    if not texto:
        raise ValueError("Ollama no devolvio contenido para analizar.")

    return texto


def limpiar_lista(valor):
    if isinstance(valor, list):
        return [str(item).strip() for item in valor if str(item).strip()]
    if isinstance(valor, str):
        items = re.split(r"[\n\r]+|,", valor)
        return [re.sub(r"^[\-\*\s]+", "", item).strip() for item in items if item.strip()]
    return []


def extraer_json_valido(texto: str) -> str:
    start = texto.find("{")
    if start == -1:
        raise ValueError("No se encontro JSON valido en la respuesta.")

    depth = 0
    in_string = False
    escape = False

    for idx, char in enumerate(texto[start:], start):
        if escape:
            escape = False
            continue
        if char == "\\":
            escape = True
            continue
        if char == '"':
            in_string = not in_string
            continue
        if in_string:
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return texto[start:idx + 1]

    raise ValueError("No se encontro JSON valido en la respuesta.")


def parsear_respuesta_json(respuesta: str):
    texto_json = extraer_json_valido(respuesta)
    datos = json.loads(texto_json)

    datos["habilidades_clave"] = limpiar_lista(datos.get("habilidades_clave", []))
    datos["fortalezas"] = limpiar_lista(datos.get("fortalezas", []))
    datos["areas_mejora"] = limpiar_lista(datos.get("areas_mejora", []))

    return AnalisisCV.model_validate(datos)


def evaluar_candidato(texto_cv: str, descripcion_puesto: str):
    try:
        prompt = OLLAMA_PROMPT.format(
            cv_texto=texto_cv,
            descripcion_puesto=descripcion_puesto,
        )

        respuesta = generar_texto_ollama(prompt)
        return parsear_respuesta_json(respuesta)

    except Exception as e:
        mensaje = str(e)
        if "HTTPConnectionPool" in mensaje or "Failed to establish a new connection" in mensaje:
            mensaje = (
                "No fue posible conectar con Ollama. Verifica que este en ejecucion "
                "y escuchando en http://localhost:11434."
            )

        return AnalisisCV(
            nombre_candidato="Error de analisis",
            experiencia="Error",
            habilidades_clave=[mensaje[:100]],
            educacion="No se pudo determinar.",
            experiencia_relevante=f"Error durante el analisis: {mensaje}",
            fortalezas=["Requiere revision manual."],
            areas_mejora=[
                "Verifica que Ollama este instalado, en ejecucion y que el modelo exista."
            ],
            porcentaje_ajuste=0,
        )
