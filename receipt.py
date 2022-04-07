import DEVICES
import datetime
import random


class Receipt:
    __status = {1: "Ремонтируется", 2: "Готово", 3: "Выдано клиенту"}

    def __init__(self, device, fio):
        self._device = None
        self._id = device.id
        self._fio = fio
        self.device = device
        self._acceptdate = datetime.date.today()
        self._status = 1
        self._dateofissue = datetime.date.today() + datetime.timedelta(days=random.randint(1, 6))

    def __str__(self):
        return f"Номер квитанции:{self._id}. Тип техники: {self._device.__class__.__name__}. Дата сдачи: {self._acceptdate}. Дата выдачи: {self._dateofissue}. " \
               f"ФИО: {self._fio}  Статус: {Receipt.__status[self._status]}"

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._fio
