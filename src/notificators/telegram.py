from .models import BaseNotificator
from . import schemas
import requests
from typing import Any

class TelegramBot(BaseNotificator):
    
    def __init__(self, chat_id: int) -> None:
        super().__init__()
        self.logger.info(f"Initializing {self.notificator_name}...")
        self.base_url = "https://api.telegram.org/bot"
        self.bot_token = "6566722334:AAEYCNOWgyplrrA3jKz6xHBsX3fPnLCWmVk"
        self.bot_name: str | None = None
        self.bot_username: str | None = None
        self.bot_id: int | None = None
        self.chat_id: int | None = chat_id
        self.status: bool = self.bot_status_control()
        if self.status:
            self.logger.info(f"{self.notificator_name} is ready to use.")
        else:
            self.logger.error(f"{self.notificator_name} is not ready to use.")
            
    def __str__(self) -> str:
        return f"{self.notificator_name}: {self.bot_id} - {self.bot_name}"
    
    def request_parser(self,request: requests.PreparedRequest) -> Any:
        session = requests.Session()
        response: requests.Response = session.send(request)
        if not response.ok:
            print(response.status_code,response.content)
        try:
            response_json = response.json()
            return response_json
        except requests.exceptions.JSONDecodeError:
            print(response.content)
    
    def bot_status_control(self) -> bool:
        request = requests.Request("GET", f"{self.base_url}{self.bot_token}/getMe")
        response_json = self.request_parser(request = request.prepare())
        schema = schemas.TelegramGetMe.from_dict(response_json)
        self.bot_id = schema.result.id
        self.bot_name = schema.result.first_name
        self.bot_username = schema.result.username
        self.chat_id = self.get_chat_id()
        return schema.ok
    
    def get_chat_id(self) -> int:
        request = requests.Request("GET", f"{self.base_url}{self.bot_token}/getUpdates")
        response_json = self.request_parser(request = request.prepare())
        schema = schemas.TelegramGetUpdates.from_dict(response_json)
        chat_id = schema.result[-1].message.chat.id
        return chat_id
    
    def send_message(self,message: str) -> bool:
        data = {'text': message}
        self.logger.success(f"Sending message to {self.chat_id}...") # type: ignore
        request = requests.Request("POST", f"{self.base_url}{self.bot_token}/sendMessage?chat_id={self.chat_id}",data=data)
        response_json = self.request_parser(request = request.prepare())
        return response_json["ok"]
    
