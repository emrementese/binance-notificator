from src.logger import logger

class NotificatorException(Exception):
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        
class BaseNotificator:
    
    def __init__(self):
        self.notificator_name = self.__class__.__name__
        self.logger = logger
        
    def send(self, message):
        raise NotImplementedError('Not implemented')