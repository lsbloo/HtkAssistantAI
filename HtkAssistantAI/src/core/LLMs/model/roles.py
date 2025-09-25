from enum import Enum

class RoleType(Enum):
    SYSTEM = 'system'
    USER = 'user'
    ASSISTANT = 'assistant'
    
    @staticmethod
    def fromType(type_str):
        for role in RoleType:
            if role.value == type_str:
                return role
        return RoleType.USER
        