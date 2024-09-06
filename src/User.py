class User:
    def __init__(self, dni: int, name: str, number_of_checkouts: int =0, number_of_checkins: int =0):
        self.__dni: int = dni
        self.__name: str = name
        self.__number_of_checkouts: int = number_of_checkouts
        self.__number_of_checkins: int = number_of_checkins

    # Getters
    def get_dni(self) -> int:
        return self.__dni

    def get_name(self) -> str:
        return self.__name

    def get_number_of_checkouts(self) -> int:
        return self.__number_of_checkouts

    def get_number_of_checkins(self) -> int:
        return self.__number_of_checkins

    # Setters
    def increment_checkouts(self) -> None:
        self.__number_of_checkouts += 1

    def increment_checkins(self) -> None:
        self.__number_of_checkins += 1