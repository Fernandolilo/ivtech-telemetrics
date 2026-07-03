from abc import ABC, abstractmethod

class BaseConnection(ABC):
    @abstractmethod
    async def connect(self, target_info): pass
    
    @abstractmethod
    async def send(self, command: str): pass
    
    @abstractmethod
    def disconnect(self): pass