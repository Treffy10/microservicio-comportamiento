from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Microservicio de Comportamiento activo"}


# Endpoint para obtener el comportamiento según ciudad y fecha
@app.get("/comportamiento")
async def obtener_comportamiento(ciudad: str, fecha: str):          
    """
    Devuelve un comportamiento simulado para la ciudad y fecha dadas.
    """
    # ==== Simulación de comportamiento ====
    comportamientos = [
        "Muy activo",
        "Activo",
        "Normal",
        "Poco activo",
        "Inactivo"
    ]
    comportamiento = comportamientos[(hash(ciudad + fecha) % len(comportamientos))]

    return {
        "comportamiento": comportamiento
    }
