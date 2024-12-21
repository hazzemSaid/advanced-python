
import random
from .Person import Person
from .Person import Gender

class User(Person):
    def __init__(self, name: str, phone_number: str, gender: Gender, user_id:int, address: str ):
        super().__init__(name, phone_number,gender)
        
        self.__user_id = user_id
        self.__address = address
        
    
    def get_user_id(self) -> int:
        return self.__user_id
    
    def get_address(self) -> str:
        return self.__address
    def get_name(self) -> str:
        return self._name
    def get_phone_number(self) -> str:
        return self._phone_number
    
    
    def close_account(self, account_id) ->None:
        if account_id in self.__account:
            del self.__account[account_id]
        else:
            raise Exception("Account not found")