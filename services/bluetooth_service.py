from bleak import BleakScanner, BleakClient
import asyncio
from collections import deque


class BluetoothService:

    def __init__(self):
        self.client = None
        self.uart_char = "0000fff1-0000-1000-8000-00805f9b34fb"

        # 🔥 buffer seguro (fila)
        self.rx_buffer = deque()

        # lock só para envio
        self.lock = asyncio.Lock()

        self.connected = False

    # =========================================================
    # CONEXÃO
    # =========================================================
    async def find_and_connect_by_name(self, keywords, timeout=10):

        devices = await BleakScanner.discover(timeout=timeout)

        for d in devices:
            name = d.name or "UNKNOWN"
            print(f"{name} | {d.address}")

            if any(k.lower() in name.lower() for k in keywords):

                print(f"\nSelecionado: {name}")

                self.client = BleakClient(d.address)
                await self.client.connect()

                if not self.client.is_connected:
                    return False

                self.connected = True

                await self.client.start_notify(
                    self.uart_char,
                    self._notify_handler
                )

                return True

        return False

    # =========================================================
    # CALLBACK BLE (THREAD EXTERNA → SEM ASYNC AQUI)
    # =========================================================
    def _notify_handler(self, sender, data):
        try:
            text = data.decode(errors="ignore")

            # 🔥 só adiciona na fila (thread-safe leve)
            self.rx_buffer.append(text)

        except Exception as e:
            print(f"[BLE ERROR] {e}")

    # =========================================================
    # ENVIO OBD (SEGURO)
    # =========================================================
    async def send(self, cmd: str, delay=0.3):

        if not self.client or not self.connected:
            return None

        async with self.lock:

            # limpa buffer ANTES
            self.rx_buffer.clear()

            await self.client.write_gatt_char(
                self.uart_char,
                (cmd + "\r").encode()
            )

            await asyncio.sleep(delay)

            # junta tudo que chegou
            resp = "".join(self.rx_buffer)
            self.rx_buffer.clear()

            return self._clean(resp)

    # =========================================================
    # LIMPEZA DE RESPOSTA OBD
    # =========================================================
    def _clean(self, data: str):
        if not data:
            return None

        return (
            data.replace(" ", "")
                .replace("\r", "")
                .replace("\n", "")
                .replace(">", "")
        )