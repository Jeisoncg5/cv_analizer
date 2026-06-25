import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from models.cv_model import AnalisisCV
from prompts.cv_prompts import crear_sistema_prompts

# Cargar variables de entorno desde .env
load_dotenv()

def crear_evaluador_cv():
    modelo_base = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.2
    )
    modelo_estructurado = modelo_base.with_structured_output(AnalisisCV)
    chat_prompt = crear_sistema_prompts()
    cadena_evaluacion = chat_prompt | modelo_estructurado

    return cadena_evaluacion

def evaluar_candidato(texto_cv: str, descripcion_puesto: str):
    try:
        cadena_evaluacion = crear_evaluador_cv()
        resultado = cadena_evaluacion.invoke({
            "cv_texto": texto_cv,
            "descripcion_puesto": descripcion_puesto
        })
        return resultado

    except Exception as e:
        print(f"ERROR EN EVALUACIÓN: {str(e)}")
        print(f"Tipo de error: {type(e).__name__}")
        return AnalisisCV(
            nombre_candidato=f"Error: {type(e).__name__}",
            experiencia="Error",
            habilidades_clave=[str(e)[:100]],
            educacion="No se puede determinar.",
            experiencia_relevante=f"Error durante el análisis: {str(e)}",
            fortalezas=["Requiere revisión manual."],
            areas_mejora=["Verifica tu API Key de OpenAI"],
            porcentaje_ajuste=0
        )