class Workshop:

    def __init__(self, number, type_of_device, take, time_of_repair, fio, status):

        self._type_of_device = type_of_device
        self._num = number
        self._take = take
        self._time_of_repair = time_of_repair
        self._fio = fio
        self._status = status

    divices = ["Телефон", "Ноут", "Телик"]
    status = ["ремонтируется, готово, выдано клиенту"]

    @property
    def fio(self):
        return self._fio

    def __str__(self):
        return f"Number of receipt: {self._num}, {self._type_of_device}, Date of receiving: " \
               f"{self._take}, Date of repair: {self._time_of_repair}, Initials: {self._fio}, Status: " \
               f"{self._status} "

