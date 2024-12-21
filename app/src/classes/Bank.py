class Bank:
    def __init__(self, name, address, hot_line):
        self.__name__ = name
        self.__address__ = address
        self.__hot_line__= hot_line
        self.__number_of_users__ = 0
    def get_name(self):
        return self.__name__

    def get_address(self):
        return self.__address__

    def get_hot_line(self):
        return self.__hot_line__

    def get_number_of_users(self):
        return self.__number_of_users__

    def inc_user(self):
        self.__number_of_users__ += 1

    def dec_user(self):
        if self.__number_of_users__ > 0:
            self.__number_of_users__ -= 1


