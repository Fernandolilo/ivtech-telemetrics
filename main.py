import uvicorn
from fastapi import FastAPI
import app as app_  # Importa o roteador do seu app.py
from services.connection_manager import manager
from services.config_manager import load_config

app = FastAPI()

# Registra as rotas que estão no seu app.py (Controller)
app.include_router(app_.router)

@app.on_event("startup")
async def startup_event():
    # Inicialização automática conforme você queria
    config = load_config()
    if config:
        print(f"Iniciando serviço... Conectando em: {config['target_name']}")
        await manager.start(config['target_name'])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)