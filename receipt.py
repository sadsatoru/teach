class Receipt:
    __kvitancia = 1

    def __init__(self,type_of_device, date, time_of_repair, fio, status):
        self._type_of_device = type_of_device
        self._date = date
        self._time_of_repair = time_of_repair
        self._fio = fio
        self._status = status
        Receipt.__kvitancia += 1

    def __str__(self):
        return f"Квитанция номер: {self.__kvitancia}, Тип девайса: {self._type_of_device}, Получит: " \
               f"{self._date}, Тайм на ремонт: {self._time_of_repair}, Получатель: {self._fio}, Статус: {self._status}"


