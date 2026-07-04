from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from services.connection_manager import manager

router = APIRouter()

# 1. ESTA LINHA ESTAVA FALTANDO OU NÃO FOI EXECUTADA
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # A sintaxe correta e mais estável é esta:
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"request": request}
    )

@router.post("/connect")
async def connect(target_name: str):
    sucesso = await manager.start(target_name)
    if not sucesso:
        raise HTTPException(status_code=400, detail="Falha na conexão")
    return {"status": "Conectado", "target": target_name}

@router.get("/status")
async def get_status():
    return {"connected": manager.is_initialized}

@router.post("/reconnect")
async def reconnect(target_name: str):
    # 1. Encerra a conexão atual de forma segura
    await manager.stop()
    
    # 2. Inicia o processo de conexão no novo alvo
    # Aqui o seu manager.start internamente deve chamar o scanner
    sucesso = await manager.start(target_name)
    
    if not sucesso:
        # Retorna erro para o front saber que falhou
        raise HTTPException(status_code=400, detail=f"Não foi possível conectar a {target_name}")
        
    return {"status": "success", "message": f"Conectado ao {target_name}"}