import DEVICES
import receipt
import random
import datetime


class Workshop:
    def __init__(self, application: list):
        self._application = application

    @property
    def application(self):
        return self._application


def print_application(self):
    applications = self._application
    return applications


def new_application():
    fio = input("ФИО: ")
    date = datetime.date.isoformat(datetime.date.today())
    status = "repairing"
    time_of_repair = datetime.date.today() + datetime.timedelta(random.randint(1, 5))

    print("Тип девайса: ")
    for i in range(len(receipt.devices)):
        return f"{i + 1}. {receipt.devices[i]}"
    type_of_device = receipt.devices[int(input())-1]

    mark = input("Модель: ")
    breakdown_description = input("Проблема: ")
    if type_of_device == "Телефон":
        system = input("Система: ")
        nw = DEVICES.Mobile(mark, breakdown_description, system)
    if type_of_device == "Ноут":
        system = input("Система: ")
        year_of_release = input("Дата производства: ")
        nw = DEVICES.Laptop(mark, breakdown_description, system, year_of_release)
    if type_of_device == "Телик":
        diagonal = int(input("Диагональ: "))
        nw = DEVICES.TV(mark, diagonal, breakdown_description)

    nr = receipt.Receipt(type_of_device, date, time_of_repair, fio, status)
    return nr.__str__()









