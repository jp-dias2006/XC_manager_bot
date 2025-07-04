from dataclasses import dataclass

@dataclass
class User:
    id: int
    username: str
    is_subscribed: bool = False
