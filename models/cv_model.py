from pydantic import BaseModel, Field

class AnalisisCV(BaseModel):
    """
    Modelo de datos para representar el análisis de un CV.
    """

    nombre_candidato: str = Field(description="Nombre Completo del candidato.")
    experiencia: str = Field(description="Años Totales de Experiencia laboral del candidato.")
    habilidades_clave: list[str] = Field(description="Lista de las 5-7 Habilidades del candidato.")
    educacion: str = Field(description="Nivel de Educación más alto del candidato y especialización principal.")
    experiencia_relevante: str = Field(description="Resumen conciso de la Experiencia laboral más relevante del candidato.")
    fortalezas: list[str] = Field(description="3-5 principales fortalezas del candidato basadas en su perfil.")
    areas_mejora: list[str] = Field(description="2-4 áreas donde el candidato podria desarrollarse basadas en su perfil.")
    porcentaje_ajuste: int = Field(description="Porcentaje de ajuste del candidato al puesto (0-100) basado en su perfil y experiencia.")