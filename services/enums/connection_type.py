from enum import Enum, auto

class ConnectionType(Enum):
    BLUETOOTH = auto()
    SERIAL = auto()
    TCP_SOCKET = auto()