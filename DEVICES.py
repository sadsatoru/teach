class Devices:
    counter = 1

    def __init__(self, mark, breakdown_description):
        self._breakdown_description = breakdown_description
        self._mark = mark
        self._id = Devices.__counter
        Devices.__counter += 1

    def __str(self):
        return f"Марка модели: {self._mark}, Описание поломки: {self._breakdown_description}"

    @property
    def id(self):
        return self._id


class Mobile(Devices):

    def __init__(self, mark, breakdown_description, system):
        super().__init__(mark, breakdown_description)
        self._system = system

    def __str__(self):
        return f"{super().__str__()}, Система: {self._system}"


class Laptop(Devices):
    def __init__(self, mark, breakdown_description, system, year_of_release):
        super().__init__(mark, breakdown_description)
        self._system = system
        self._year_of_release = year_of_release

    def __str__(self):
        return f"{super().__str__()}, Система: {self._system}, Дата производства: {self._year_of_release}"


class TV(Devices):

    def __init__(self, mark, diagonal, breakdown_description):
        super().__init__(mark, breakdown_description)
        self._diagonal = diagonal

    def __str__(self):
        return f"{super().__str__()}, Диагональ: {self._diagonal}"
