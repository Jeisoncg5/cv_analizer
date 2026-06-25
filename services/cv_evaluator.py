import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from models.cv_model import AnalisisCV
from prompts.cv_prompts import crear_sistema_prompts

load_dotenv()

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


def crear_evaluador_cv():
    modelo_base = ChatOpenAI(
        model=OPENAI_MODEL,
        temperature=0.2,
    )
    modelo_estructurado = modelo_base.with_structured_output(AnalisisCV)
    chat_prompt = crear_sistema_prompts()
    cadena_evaluacion = chat_prompt | modelo_estructurado
    return cadena_evaluacion


def evaluar_candidato(texto_cv: str, descripcion_puesto: str):
    try:
        cadena_evaluacion = crear_evaluador_cv()
        resultado = cadena_evaluacion.invoke(
            {
                "cv_texto": texto_cv,
                "descripcion_puesto": descripcion_puesto,
            }
        )
        return resultado

    except Exception as e:
        mensaje = str(e) or "No se pudo completar la evaluacion con OpenAI."
        print(f"ERROR EN EVALUACION: {mensaje}")
        print(f"Tipo de error: {type(e).__name__}")
        return AnalisisCV(
            nombre_candidato=f"Error: {type(e).__name__}",
            experiencia="Error",
            habilidades_clave=[mensaje[:100]],
            educacion="No se puede determinar.",
            experiencia_relevante=f"Error durante el analisis: {mensaje}",
            fortalezas=["Requiere revision manual."],
            areas_mejora=["Verifica tu API key de OpenAI y el modelo configurado."],
            porcentaje_ajuste=0,
        )
