class DEVICES:

    def __init__(self, mark, name, breakdown_description):
        self._mark = mark
        self._breakdown_description = breakdown_description
        self._name = name


def __str__(self):
    return f"Тип девайса:{self._name}, Марка:{self._mark}, Описание поломки: {self._breakdown_description}"


class Mobile(DEVICES):

    def __init__(self, mark, breakdown_description, system):
        super().__init__(mark, breakdown_description)
        self._system = system

    def __str__(self):
        return f"{super().__str__()}, Система: {self._system}"


class Laptop(DEVICES):
    def __init__(self, mark, breakdown_description, system, year_of_release):
        super().__init__(mark, breakdown_description)
        self._system = system
        self._year_of_release = year_of_release

    def __str__(self):
        return f"{super().__str__()}, Система: {self._system}, Дата производства: {self._year_of_release}"


class TV(DEVICES):

    def __init__(self, mark, diagonal, breakdown_description):
        super().__init__(mark, breakdown_description)
        self._diagonal = diagonal

    def __str__(self):
        return f"{super().__str__()}, Диагональ: {self._diagonal}"

