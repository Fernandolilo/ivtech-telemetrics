from services.bluetooth_connection import BluetoothConnection
from services.logger import get_logger

logger = get_logger("ConnectionManager")

class ConnectionManager:
    def __init__(self):
        self.connection = None
        self.is_initialized = False

    async def start(self, target_name):
        """Inicializa e tenta conectar a um dispositivo."""
        logger.info(f"Tentando conectar ao dispositivo: {target_name}")
        
        # Garante que temos uma instância de conexão limpa
        if not self.connection:
            self.connection = BluetoothConnection()
        
        sucesso = await self.connection.connect(target_name)
        self.is_initialized = sucesso
        
        if not sucesso:
            logger.error(f"Falha ao estabelecer conexão Bluetooth com {target_name}.")
        else:
            logger.info(f"Conexão estabelecida com sucesso com {target_name}.")
            
        return sucesso

    async def stop(self):
        """Limpa a conexão e reseta o estado do manager."""
        if self.connection:
            try:
                # Chama o método de desconexão da sua classe de Bluetooth
                await self.connection.disconnect()
            except Exception as e:
                logger.error(f"Erro ao desconectar: {e}")
            finally:
                self.connection = None
                self.is_initialized = False
                logger.info("Conexão encerrada e estado limpo.")

# Instância única para ser usada na API
manager = ConnectionManager()