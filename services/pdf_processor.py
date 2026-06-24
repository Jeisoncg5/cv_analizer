import PyPDF2
from io import BytesIO

def extraer_texto_pdf(archivo_pdf):
    try:
        pdf_reader = PyPDF2.PdfReader(BytesIO(archivo_pdf.read()))
        texto_completo = ""

        for numero_pagina, pagina in enumerate(pdf_reader.pages):
            texto_pagina = pagina.extract_text()
            if texto_pagina.strip():  # Verifica si la página tiene texto
                texto_completo += f"\n--- PÁGINA {numero_pagina} ---\n"
                texto_completo += texto_pagina + "\n"
        
        texto_completo = texto_completo.strip()  # Elimina espacios en blanco al inicio y al final
        return texto_completo
    except Exception as e:
        return f"Error al procesar el PDF: {str(e)}"