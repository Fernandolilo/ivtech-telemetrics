from models.base_connection import BaseConnection
from services.enums.connection_type import ConnectionType

class BluetoothConnection(BaseConnection):
    def __init__(self, uuid):
        self.uuid = uuid
        self.client = None
        
    async def connect(self, address):
        # Lógica específica do Bluetooth (Bleak)
        print(f"Conectando BLE em {address} com UUID {self.uuid}")
        
    async def send(self, command):
        # Lógica específica de envio BLE
        pass

    def disconnect(self):
        pass

class SerialConnection(BaseConnection):
    def __init__(self, port, baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        
    async def connect(self, target_info=None):
        print(f"Abrindo porta Serial {self.port}...")
        
    async def send(self, command):
        # Lógica usando pyserial
        pass

    def disconnect(self):
        pass
    
    def connection_factory(conn_type: ConnectionType, config: dict):
            if conn_type == ConnectionType.BLUETOOTH:
                return BluetoothConnection(config.get("uuid"))
            elif conn_type == ConnectionType.SERIAL:
                return SerialConnection(config.get("port"), config.get("baudrate"))
            else:
                raise ValueError("Tipo de conexão não suportado!")