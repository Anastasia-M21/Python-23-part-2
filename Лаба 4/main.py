if __name__ == "__main__":
class Animal:
    """
    Базовый класс, описывающий животное.
    Инкапсуляции в базовом и дочерниках классах для упрощения кода и предотвращения изменения состояния объекта.
    """
    def __init__(self, name: str, category: str, age: int):
        """
        Конструктор класса Animal.
        Параметры:
        - name (str): Имя животного.
        - category (str): Класс в природе, к которому относится животное.
        - age (int): Возраст животного.
        """
        self._name = name
        self._category = category
        self._age = age

    def __str__(self) -> str:
        """
        Строковое представление объекта Animal.
        """
        return f"Животное: {self.name}. Класс: {self.category}"

    def __repr__(self) -> str:
        """
        Машинно-ориентированное представление объекта Animal.
        """
        return f"{self.__class__.name}(name={self.name!r}, category={self.category})"

    def check_category(self, category: str) -> str:
        """
        Метод, который в зависимости от класса животного в природе выводит информацию о данном классе.

        Возвращает:
        - str: Строка с основной информацией о данном классе.
        """
        ...

    def growing_up(self, age: int) -> str:
        """
        Метод, который в зависимости от возраста выводит категорию особи: детеныш, подросток, взрослая особь.

        Возвращает:
        - str: Строка - категория особи.
        """
        ...

    @property
    def name(self) -> str:
        return self._name

    @property
    def category(self):
        return self._category

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age: int) -> None:
        if not isinstance(new_age, int):
            raise TypeError
        if new_age < 0:
            raise ValueError
        self._age = new_age


class Shark(Animal):
    """
    Подкласс акула, унаследованный от класса Animal.
    """
    def __init__(self, name: str, category: str, weight: float, habitat: str):
        """
        Конструктор класса Shark.
        Параметры:
        - name (str): Имя акулы.
        - category (str): Класс в природе, к которому относится акула.
        - age (int): Возраст акулы.
        - weight (float): Вес акулы.
        - habitat (str): Среда обитания акулы.
        """
        super().__init__(name, category)
        self._weight = weight
        self._habitat = habitat

    def __str__(self) -> str:
        """
        Перегруженный метод для строкового представления объекта Shark.

        Возвращает:
        - str: Форматированная строка с информацией об акуле.
        """
        return f"Животное: {self.name}. Класс: {self.category}. " \
               f"Вес: {self.weight}. Среда обитания: {self.habitat}."

    def __repr__(self) -> str:
        """
        Перегруженное машинно-ориентированное представление объекта Shark.

        Возвращает:
        - str: Машинно-ориентированная строка с информацией об акуле.
        """
        return f"{self.__class__.name}(name={self.name!r}, category={self.category}, " \
               f"weight={self.weight}, habitat={self.habitat})"

    def check_category(self, category: str):
        """
        Унаследованный метод из базовго класса
        """
        super().check_category(category)

    def growing_up(self, weight: float, age: int):
        """
        Перегруженный метод из базового класса.
        В зависимости от возраста идет расчет веса акулы.

        Возвращает:
        - float: Вес акусы.
        """
        ...

    @property
    def habitat(self):
        return self._habitat

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, new_weight: float) -> None:
        if not isinstance(new_weight, float):
            raise TypeError
        if new_weight < 0:
            raise ValueError
        self._weight = new_weight


class Giraffe(Animal):
    """
    Подкласс жираф, унаследованный от класса Animal.
    """
    def __init__(self, name: str, category: str, height: float, type_of_food: str):
        """
        Конструктор класса Giraffe.
        Параметры:
        - name (str): Имя жирафа.
        - category (str): Класс в природе, к которому относится жираф.
        - age (int): Возраст жирафа.
        - height (float): Рост жирафа.
        - type_of_food (str): Тип питания жирафа.
        """
        super().__init__(name, category)
        self._type_of_food = type_of_food
        self._height = height

    def __str__(self) -> str:
        """
        Перегруженный метод для строкового представления объекта Giraffe.

        Возвращает:
        - str: Форматированная строка с информацией о жирафе.
        """
        return f"Животное: {self.name}. Класс: {self.category}. " \
               f"Рост: {self.height}. Тип питания: {self.type_of_food}."

    def __repr__(self) -> str:
        """"
        Перегруженное машинно-ориентированное представление объекта Giraffe.

        Возвращает:
        - str: Машинно-ориентированная строка с информацией о жирафе.
        """
        return f"{self.__class__.name}(name={self.name!r}, category={self.category}, " \
               f"height={self.height}, type_of_food={self.type_of_food})"

    def check_category(self, category: str):
        """
        Унаследованный метод из базовго класса
        """
        super().check_category(category)

    def growing_up(self, age: int, height: float) -> float:
        """
        Перегруженный метод из базового класса.
        В зависимости от возраста идет расчет роста жирафа.

        Возвращает:
        - float: Рост жирафа.
        """
        ...

    @property
    def type_of_food(self):
        return self._type_of_food

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height: float) -> None:
        if not isinstance(new_height, float):
            raise TypeError
        if new_height < 0:
            raise ValueError
        self._height = new_height

    pass
