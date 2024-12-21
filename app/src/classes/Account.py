class Account:
    def __init__(self, user_id: int, username: str, password: str, card_number: int, pin: int, balance: float):
        self.__user_id = user_id
        self.__username = username
        self.__password = password
        self.__card_number = card_number
        self.__pin = pin
        self.__balance = balance

    def get_user_id(self) -> int:
        return self.__user_id

    def set_username(self, username: str) -> None:
        self.__username = username

    def get_username(self) -> str:
        return self.__username

    def set_password(self, password: str) -> None:
        self.__password = password

    def get_password(self) -> str:
        return self.__password

    def get_card_number(self) -> int:
        return self.__card_number

    def set_pin(self, pin: int) -> None:
        self.__pin = pin

    def get_pin(self) -> int:
        return self.__pin

    def set_balance(self, balance: float) -> None:
        self.__balance = balance

    def get_balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
