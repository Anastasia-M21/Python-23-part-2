import doctest


class Book:
    def __init__(self, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"
        :param author: Автор книги
        :param pages: Количество страниц в книге

        Пример:
        >>> book = Book('А.С. Пушкин', 300)  # инициализация экземпляра класса
        """
        if not isinstance(author, str):
            raise TypeError('ФИО автора должно быть типа str')
        self.author = author

        if not isinstance(pages, int):
            raise TypeError('Количество страниц должно быть типа int')
        if pages <= 0:
            raise ValueError('Количество страниц должно быть положительным числом')
        self.pages = pages

    def read_book(self, read_pages: int) -> bool:
        """
        Функция, которая проверяет прочитана книга или нет
        :param read_pages: Количество прочитанных страниц

        :raise ValueError: Если количество прочитаннх страниц превышает количество страниц в книге или является отрицательным числом, то вызываем ошибку

        :return: Прочитана ли книга

        Примеры:
        >>> book = Book('А.С. Пушкин', 300)
        >>> book.read_book(0)
        """
        if isinstance(read_pages, int):
            raise TypeError('Количество прочитанных страниц должно быть типа int')
        if self.pages < read_pages < 0:
            raise ValueError('Количество прочитанных страниц должно быть положительным числом и не превышать количество страниц в книге')
        ...

    def increment_last_read_pages(self, read_pages: int) -> None:
        """
        Функция, которая увеличивает последнюю прочитанную страницу
        :param read_pages: Количество прочитанных страниц

        :raise ValueError: Если количество прочитаннх страниц превышает количество страниц в книге или является отрицательным числом, то вызываем ошибку

        :return: Последняя прочитанная страница

        Примеры:
        >>> book = Book('А.С. Пушкин', 300)
        >>> book.increment_last_read_pages(20)
        """
        if isinstance(read_pages, int):
            raise TypeError('Количество прочитанных страниц должно быть типа int')
        if self.pages < read_pages < 0:
            raise ValueError('Количество прочитанных страниц должно быть положительным числом и не превышать количество страниц в книге')
        ...


class Auditorium:
    def __init__(self, number_of_seats: int,  number_of_students: int):
        """
        Создание и подготовка к работе объекта "Аудитория"
        :param number_of_seats: Количество мест в аудитории
        :param number_of_students: Количество студентов

        Пример:
        >>> auditorium = Auditorium(30, 25)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_seats, int):
            raise TypeError('Количество мест должно быть типа int')
        self.number_of_seats = number_of_seats

        if not isinstance(number_of_students, int):
            raise TypeError('Количество студентов должно быть типа int')
        if number_of_students > number_of_seats:
            raise ValueError('Количество студентов не должно быть больше количества сидящих мест')
        self.number_of_students = number_of_students

    def empty_class(self) -> bool:
        """
        Функция, которая проверяет пустая ли аудитория

        :return: Пустая ли аудитория

        Примеры:
        >>> auditorium = Auditorium(30, 0)
        >>> auditorium.empty_class()
        """
        ...

    def number_of_available_seats(self) -> None:
        """
        Функция, которая выводит количество свободных мест

        :return: Количество свободных мест

        Примеры:
        >>> auditorium = Auditorium(30, 20)
        >>> auditorium.empty_class()
        """
        ...


class Exam:
    def __init__(self, submitted_works: (float, int), mark: int):
        """
        Создание и подготовка к работе объекта "Экзамен"
        :param submitted_works: Количество сданных работ
        :param mark: Оценка за экзамен соответствующая такому количеству сданных работ

        Пример:
        >>> exam = Exam(5,5)  # инициализация экземпляра класса
        """
        if not isinstance(submitted_works, (float, int)):
            raise TypeError('Количество сданных работ должно быть типа float или int')
        if submitted_works < 0:
            raise ValueError('Количество сданных работ должно быть положительным числом')
        self.submitted_works = submitted_works

        if not isinstance(mark, int):
            raise TypeError('Оценка должна быть типа int')
        if mark < 2:
            raise ValueError('Оценка за экзамен не должна быть ниже 2')
        self.mark = mark

    def additional_session(self) -> bool:
        """
        Функция, которая проверяет сдан экзамен или нет (отправлен студент на дпосессию или нет)

        :return: допсессия или нет

        Примеры:
        >>> exam = Exam(1, 2)
        >>> exam.additional_session()
        """
        ...

    def admission_to_the_exam(self, attendance: int) -> None:
        """
        Функция, которая проверяет достаточно ли посещаемсоти пар для допуска к экзамену
        :param attendance: Посещаемость пар в процентах

        :raise ValueError: Если посещаемость превышает 100 процентов или является отрицательным числом, то вызываем ошибку

        :return: Есть ли допуск к экзамену

        Примеры:
        >>> exam = Exam(3, 3)
        >>> exam.admission_to_the_exam(50)
        """
        if isinstance(attendance, int):
            raise TypeError('Посещаемость должна быть типа int')
        if 0 < attendance < 100:
            raise ValueError('Посещаемость должна быть положительным числом и не превышать 100 процентов')
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

