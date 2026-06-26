from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Base de datos simulada (lista en memoria)
usuarios = [
    {"id": 1, "nombre": "Ana", "email": "ana@email.com"},
    {"id": 2, "nombre": "Carlos", "email": "carlos@email.com"}
]

@app.get("/")
def inicio():
    return {"mensaje": "¡Hola Mundo!"}

@app.get("/usuarios")
def listar_usuarios():
    return {"usuarios": usuarios}

@app.get("/usuarios/{id}")
def obtener_usuario(id: int):
    for usuario in usuarios:
        if usuario["id"] == id:
            return usuario
    return {"error": "Usuario no encontrado"}

@app.post("/usuarios")
def crear_usuario(nombre: str, email: str):
    nuevo_id = max([u["id"] for u in usuarios]) + 1 if usuarios else 1
    nuevo = {"id": nuevo_id, "nombre": nombre, "email": email}
    usuarios.append(nuevo)
    return nuevo

@app.get("/usuarios/buscar")
def buscar_usuario(nombre: str):
    """Buscar usuarios por nombre"""
    resultados = [u for u in usuarios if nombre.lower() in u["nombre"].lower()]
    return {"resultados": resultados, "total": len(resultados)}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)