from fastapi import FastAPI, UploadFile, File, HTTPException
import fitz  # PyMuPDF
import os

app = FastAPI()

@app.post("/analizar-pdf")
async def analizar_pdf(file: UploadFile = File(...)):
    # Validar que sea PDF
    if not file.filename.endswith(".pdf"):
        return {"error": "El archivo no es un PDF válido"}

    try:
        # Leer el contenido del archivo en memoria
        content = await file.read()
        
        # Abrir el PDF con PyMuPDF
        doc = fitz.open(stream=content, filetype="pdf")
        
        # Obtener datos clave
        num_paginas = len(doc)
        info = doc.metadata
        
        # Lógica simple para detectar color (analiza la primera página)
        # Esto es una estimación, para fines prácticos preguntaremos al usuario después,
        # pero esto ayuda al sistema.
        es_color = False
        page = doc[0]
        pix = page.get_pixmap()
        # Si el espacio de color no es Gray/DeviceGray, podría ser color
        if pix.n > 2: 
            es_color = True

        doc.close()

        return {
            "status": "success",
            "filename": file.filename,
            "paginas": num_paginas,
            "detectado_color": es_color,
            "info": info
        }

    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def read_root():
    return {"mensaje": "Servicio de Análisis de PDF Activo 🚀"}
