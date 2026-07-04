from bleak import BleakScanner
from services.bluetooth_service import BluetoothService
from models.base_connection import BaseConnection

class BluetoothConnection(BaseConnection):
    def __init__(self, uuid="0000fff1-0000-1000-8000-00805f9b34fb"):
        self.uuid = uuid
        self.service = BluetoothService()

    # 1. Implementação obrigatória do método 'send' exigido pela BaseConnection
    async def send(self, cmd: str):
        return await self.service.send(cmd)

    # 2. Implementação obrigatória do método 'disconnect'
    async def disconnect(self):
        if self.service.client:
            await self.service.client.disconnect()
            self.service.connected = False

    # 3. Seu método de conexão que já tínhamos definido
    async def connect(self, device_name):
        return await self.service.find_and_connect_by_name([device_name])
    
    @staticmethod
    async def listar_dispositivos():
        print("\nEscaneando dispositivos...")
        devices = await BleakScanner.discover(timeout=5)
        dispositivos = [d for d in devices if d.name]
        
        for i, d in enumerate(dispositivos, start=1):
            print(f"{i} - {d.name}")
        
        return dispositivos