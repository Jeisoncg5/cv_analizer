# CV Analyzer with Ollama

Aplicacion en Streamlit para analizar hojas de vida en PDF y compararlas contra una descripcion de cargo usando un modelo local en Ollama.

## Que hace

- Extrae texto de un CV en PDF
- Evalua experiencia, educacion y habilidades
- Genera fortalezas y areas de mejora
- Calcula un porcentaje de ajuste al cargo
- Usa Ollama en local, sin depender de modelos guardados en el repo

## Requisitos

- Python 3.11 o superior
- Ollama instalado y ejecutandose localmente
- Un modelo disponible en Ollama

Modelo probado en este proyecto:

```text
qwen2.5-coder:1.5b
```

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

## Instalacion

1. Clona el repositorio.
2. Crea y activa un entorno virtual.
3. Instala las dependencias.
4. Configura el archivo `.env`.
5. Asegurate de que Ollama este corriendo y tenga el modelo cargado.

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

## Configuracion de Ollama

Verifica que Ollama este instalado:

```powershell
ollama --version
```

Descarga el modelo si aun no lo tienes:

```powershell
ollama pull qwen2.5-coder:1.5b
```

Lista los modelos instalados:

```powershell
ollama list
```

Si usas otro modelo, cambia `OLLAMA_MODEL` en `.env`.

## Variables de entorno

Archivo `.env`:

```env
OLLAMA_MODEL=qwen2.5-coder:1.5b
OLLAMA_URL=http://localhost:11434/api/generate
OLLAMA_TIMEOUT=120
```

## Como ejecutar

Con el entorno virtual activo:

```powershell
python -m streamlit run app.py
```

Luego abre en el navegador la URL que Streamlit muestre en consola, normalmente:

```text
http://localhost:8501
```

## Flujo de uso

1. Sube un CV en PDF con texto seleccionable.
2. Escribe la descripcion del puesto.
3. Haz clic en `Analizar Candidato`.
4. Revisa el resumen, fortalezas, areas de mejora y porcentaje de ajuste.

## Problemas comunes

### Ollama no responde

Verifica que Ollama este en ejecucion y que la URL sea correcta:

```text
http://localhost:11434
```

### El modelo no existe

Confirma el nombre exacto con:

```powershell
ollama list
```

Y actualiza `.env` si es necesario.

### El PDF no se analiza bien

Usa PDFs con texto real. Los PDFs escaneados o convertidos en imagen pueden devolver poco o nada de contenido.

