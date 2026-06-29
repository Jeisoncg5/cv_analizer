# CV Analyzer with Mistral AI

Aplicacion en Streamlit para analizar hojas de vida en PDF y compararlas contra una descripcion de cargo usando Mistral AI.

## Funcionalidades

- Carga de CV en PDF
- Extraccion de texto del documento
- Analisis estructurado del candidato con IA
- Evaluacion de experiencia, educacion y habilidades
- Calculo de porcentaje de ajuste al puesto

## Stack

- Python
- Streamlit
- LangChain
- Mistral AI
- Pydantic
- PyPDF2

## Estructura del proyecto

```text
cv_analizer/
|-- app.py
|-- requirements.txt
|-- .env.example
|-- models/
|   `-- cv_model.py
|-- prompts/
|   `-- cv_prompts.py
|-- services/
|   |-- cv_evaluator.py
|   `-- pdf_processor.py
|-- ui/
|   `-- streamlit_ui.py
```

## Requisitos

- Python 3.11 o superior
- Una API key valida de Mistral AI

## Instalacion

### Windows PowerShell

```powershell
git clone <URL_DEL_REPO>
cd cv_analizer
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

### macOS / Linux

```bash
git clone <URL_DEL_REPO>
cd cv_analizer
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

## Configuracion

Edita `.env` con tu API key:

```env
MISTRAL_API_KEY=your_mistral_api_key_here
MISTRAL_MODEL=mistral-small-latest
```

`MISTRAL_MODEL` es opcional. Si no lo defines, el proyecto usa `mistral-small-latest`.

## Como ejecutar

Con el entorno virtual activo:

```powershell
python -m streamlit run app.py
```

Luego abre la URL local que Streamlit muestre en consola, normalmente:

```text
http://localhost:8501
```

## Flujo de uso

1. Sube un CV en formato PDF.
2. Escribe la descripcion del puesto.
3. Pulsa `Analizar Candidato`.
4. Revisa el resultado estructurado del analisis.


## Problemas comunes

### Falta la API key

Si `MISTRAL_API_KEY` no esta definida o esta vacia, la evaluacion fallara y la app devolvera un error controlado.

### El PDF no tiene texto seleccionable

Si el PDF es una imagen escaneada, la extraccion puede devolver poco contenido o vacio.

### Dependencias faltantes

Reinstala el entorno con:

```powershell
python -m pip install -r requirements.txt
```

## Verificacion recomendada

Antes de usar la app:

```powershell
python -m compileall app.py services prompts models ui
```
