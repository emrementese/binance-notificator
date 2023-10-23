from mashumaro.mixins.json import DataClassJSONMixin
from mashumaro import field_options
from dataclasses import dataclass, field
from typing import List

@dataclass
class TelegramGetMe(DataClassJSONMixin):
    """
        Response Schmea: Telegram getMe
    """
    
    @dataclass
    class Result(DataClassJSONMixin):
        id: int
        is_bot: bool
        first_name: str
        username: str
        can_join_groups: bool
        can_read_all_group_messages: bool
        supports_inline_queries: bool
    
    ok: bool
    result: Result
    
@dataclass
class TelegramGetUpdates(DataClassJSONMixin):

    @dataclass
    class Result(DataClassJSONMixin):
        
        @dataclass
        class Message(DataClassJSONMixin):
            
            @dataclass
            class Chat(DataClassJSONMixin):
                id: int
                first_name: str
                type: str
                last_name: str | None = None
                username: str | None = None
            
            @dataclass
            class From(DataClassJSONMixin):
                id: int
                is_bot: bool
                first_name: str
                language_code: str
                last_name: str | None = None
                username: str | None = None
                
            @dataclass
            class Entities(DataClassJSONMixin):
                offset: int
                length: int
                type: str
                
            message_id: int
            chat: Chat
            date: int
            text: str
            from_: From = field(metadata=field_options(alias="from"))
            entities: List[Entities] | None = None
            
        update_id: int
        message: Message
        
    ok: bool
    result: List[Result]