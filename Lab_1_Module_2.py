# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

import doctest


class Student:
    def __init__(self, surname_name_second_name: str, mark: int):
        """
        Создание и подготовка к работе объекта "Студент" - записи студента и его текущей оценки за дисциплину N

        :param surname_name_second_name: ФИО студента
        :param mark: Оценка студента

        Примеры:
        >>> student = Student(Ivanov Ivan Ivanovich, 97)  # инициализация экземпляра класса
        """
        if len(surname_name_second_name) != 3:
            raise ValueError("Требуется ввести полное ФИО")
        self.surname_name_second_name = surname_name_second_name

        if mark < 0 or mark > 100:
            raise ValueError("Оценивание ведется по стобальной системе")
        if not isinstance(mark, int):
            raise TypeError("Оценка представляет собой целое число")
        self.mark = mark

    def student_succeed (self) -> None:
        """
        Функция которая проверяет, достиг ли студент оценки 60 баллов, то есть необходимого балла для зачета по предмету N

        :return: Получил ли студент зачет по предмету N

        Примеры:
        >>> student = Student(Ivanov Ivan Ivanovich, 97)
        >>> student_succeed(student)
        """
        ...

    def add_points(self, points: int) -> None:
        """
        Добавление студенту баллов
        :param points: Количество добавляемых баллов

        :points ValueError: Если количество добавляемых баллов делает оценку больше ста, выдается ошибка
        :points ValueError: Значение должно быть положительным и целым, баллы забрать нельзя
        Примеры:
        >>> student = Student(Ivanov Ivan Ivanovich, 97)
        >>> student.add_points(2)
        """
        if not isinstance(points, (int)):
            raise TypeError("Нельзя добавить дробное количество баллов")
        if points < 0:
            raise ValueError("Нельзя забрать у студента баллы")
        ...

class Building:
    def __init__(self, floors: int, floors_built: int, status: str):
        """
        Создание и подготовка к работе объекта "Здание"

        :param floors: Планируемая этажность здания
        :param floors_built: Количество возведенных на данный момент этажей
        :param status: Состояние объекта
        Примеры:
        >>> building = Building(9, 4, construction)  # инициализация экземпляра класса
        """
        if not isinstance(floors, int):
            raise ValueError("Количество этажей - это целое число")
        if not isinstance(floors, int):
            raise ValueError("Количество этажей - это положительное число")
        self.floors = floors

        if not isinstance(floors_built, int):
            raise ValueError("Количество этажей - это целое число")
        if not isinstance(floors_built, int):
            raise ValueError("Количество этажей - это положительное число")
        self.floors_built = floors_built

        if status != 'construction' and status != 'planning' and status != 'finished':
            raise ValueError('Аргумент может принимать только значения: construction, planning, finished')
        self.status = status

    def change_status (self) -> None:
        """
        Функция, которая заменяет стадию планирования на стадию возведения, а стадию возведения - на стадию готового объекта

        :return: Функция не возвращает значение
        :points ValueError: Если функуия вызывается, когда объект уже считается готовым, пользователь видит предупреждение
        Примеры:
        >>> building = Building(9, 4, construction)
        >>> change_status(building)
        """
        ...

    def add_floor(self, amount_of_floors: int) -> None:
        """
        Обновление количества построенных этажей
        :param amount_of_floors: Количество новых этажей

        :return: Функция не возвращает значение

        :amount_of_floors ValueError: В результате количество этажей не должно быть больше планируемого
        :amount_of_floors ValueError: Значение должно быть положительным и целым
        Примеры:
        >>> building = Building(9, 4, construction)
        >>> building.add_floors(2)
        """
        if not isinstance(amount_of_floors, (int)):
            raise TypeError("Нельзя построить дробное количество этажей")
        if amount_of_floors < 0:
            raise ValueError("Нельзя добавить отрицательное количество этажей")
        ...

    def floors_left(self) -> None:
        """
        Функция определяет, сколько этажей осталось до конца строительства, а если их осталось 0, то меняет статус строителства на 'finished'
        :return: Функция возвращает количество этажей до конца строительства, а если этажей 0, то сообщает, что статус здания изменен
        Примеры:
        >>> building = Building(9, 4, construction)
        >>> building.floors_left()
        """

class Fabric:
    def __init__(self, color: str, price: float, meters_left: float):
        """
        Создание и подготовка к работе объекта "Ткань"

        :param price: Цена за метр ткани, рубли
        :param color: Цвет ткани
        :param meters_left: Количество ткани, оставшейся в рулоне, в метрах
        Примеры:
        >>> fabric = Fabric(yellow, 343, 7)  # инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError("Требуется ввести аргумент типа str")
        self.color = color

        if not isinstance(price, float):
            raise TypeError("Требуется ввести аргумент типа float")
        if price <= 0:
            raise ValueError("Цена не может быть отрицательной")
        self.price = price

        if not isinstance(meters_left, float):
            raise TypeError("Требуется ввести аргумент типа float")
        if meters_left <= 0:
            raise ValueError("Количество ткани не может быть отрицательным")
        self.meters_left = meters_left

    def change_color (self, new_color: str) -> None:
        """
        Функция, которая меняет цвет ткани

        :return: Функция не возвращает значение
        :param new_color: Новый цвет ткани
        :new_color ValueError: Значение должно быть равно одному из значений цветов в базе
        Примеры:
        >>> fabric = Fabric(yellow, 343, 7)
        >>> fabric.change_color(red)
        """
        ...

    def cut_fabric(self, amount_of_fabric: float) -> None:
        """
        Функция, которая отрезает ткань от рулона

        :return: Функция не возвращает значение
        :param amount_of_fabric: Количество отрезанной ткани
        :amount_of_fabric ValueError: Значение должно быть положительным и меньше или равно meters_left
        Примеры:
        >>> fabric = Fabric(yellow, 343, 7)
        >>> fabric.cut_fabric(200)
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
