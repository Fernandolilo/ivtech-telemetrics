

from services.bluetooth_connection import BluetoothConnection

# Mude o import para apontar para o seu arquivo local
from services.logger import get_logger

# Inicialize o logger para esta classe
logger = get_logger("ConnectionManager")



class ConnectionManager:
        
    logger = get_logger("ConnectionManager")
    def __init__(self):
        self.connection = None
        self.is_initialized = False

    async def start(self, target_name):
        """Inicializa e conecta a conexão Bluetooth."""
        if not self.connection:
            self.connection = BluetoothConnection()
            # ... dentro do seu método start ...
            logger.error("Falha ao estabelecer conexão Bluetooth.")
        
        # Conecta se ainda não estiver conectado
        sucesso = await self.connection.connect(target_name)
        self.is_initialized = sucesso 
        logger.info(f"Tentando conectar ao dispositivo: {target_name}")
        return sucesso

# Instância única para ser usada na API
manager = ConnectionManager()