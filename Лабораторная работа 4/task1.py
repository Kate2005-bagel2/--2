class Vehicle:
    """
    Базовый класс для всех транспортных средств.
    """

    def __init__(self, make: str, model: str, year: int) -> None:
        """
        Инициализация объекта транспортного средства.

        :param make: Производитель транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self.make = make
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта транспортного средства.
        """
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта транспортного средства.
        """
        return f"Vehicle(make='{self.make}', model='{self.model}', year={self.year})"


class Car(Vehicle):
    """
    Класс легкового автомобиля.
    """

    def __init__(self, make: str, model: str, year: int, doors: int) -> None:
        """
        Инициализация объекта легкового автомобиля.

        :param make: Производитель легкового автомобиля.
        :param model: Модель легкового автомобиля.
        :param year: Год выпуска легкового автомобиля.
        :param doors: Количество дверей легкового автомобиля.
        """
        super().__init__(make, model, year)
        self.__doors = doors  # Инкапсуляция, так как количество дверей внутреннее состояние

    def get_doors(self) -> int:
        """
        Получить количество дверей легкового автомобиля.

        :return: Количество дверей.
        """
        return self.__doors

    def set_doors(self, doors: int) -> None:
        """
        Установить количество дверей легкового автомобиля.

        :param doors: Количество дверей.
        """
        self.__doors = doors

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта легкового автомобиля.
        """
        return f"{super().__str__()} with {self.__doors} doors"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта легкового автомобиля.
        """
        return f"Car(make='{self.make}', model='{self.model}', year={self.year}, doors={self.__doors})"


# Пример использования классов
car = Car("Toyota", "Camry", 2022, 4)
print(car)  # Выводит: 2022 Toyota Camry with 4 doors
print(repr(car))  # Выводит: Car(make='Toyota', model='Camry', year=2022, doors=4)