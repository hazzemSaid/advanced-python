from enum import Enum

class Gender(Enum):
    Male = "Male"
    Female = "Female"

class Person:
    def __init__(self, name: str, phone_number: str, gender: str):
        self._name = name
        self._phone_number = phone_number
        self._gender = gender
        
    def set_name(self, name: str) -> None:
        self._name = name
        
    def get_name(self) -> str:
        return self._name
    
    def set_contact_info(self, phone_number: str) -> None:
        self._phone_number = phone_number
    
    def get_contact_info(self) -> str:
        return self._phone_number
    
    def set_gender(self, gender: str) -> None:
        self._gender = self._validate_gender(gender)
    
    def get_gender(self) -> str:
        return self._gender.value

# Example Usage:
# name = input("Enter name: ")
# phone_number = input("Enter phone number: ")
# gender = input("Enter gender (Male/Female): ")

# try:
#     person = Person(name=name, phone_number=phone_number, gender=gender)
#     print("Person created successfully!")
#     print(f"Name: {person.get_name()}")
#     print(f"Phone: {person.get_contact_info()}")
#     print(f"Gender: {person.get_gender()}")
# except ValueError as e:
#     print(e)
