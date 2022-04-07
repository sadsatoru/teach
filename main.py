import DEVICES
import src
import datetime
import random

from receipt import Receipt
from workshop import Workshop


def who_are_u():
    fio = input(src.fio)
    return fio


def create_tv(mark, breakdown_description):
    diagonal = input(src.user_diagonal)
    tv = DEVICES.TV(mark, breakdown_description, diagonal)
    return tv


def create_mobile(mark, breakdown_description):
    system = input(src.user_system)
    mobile = DEVICES.Mobile(mark, breakdown_description, system)
    return mobile


def create_computer(mark, breakdown_description):
    system = input(src.user_system)
    year_of_release = input(src.user_year_of_release)
    laptop = DEVICES.Laptop(mark, breakdown_description, system, year_of_release)
    return laptop


def create_receipt(workshop, name):
    while True:
        type_of_device = input(src.user_type_of_device)
        if type_of_device == "1":
            mark = input(src.user_mark)
            desc = input(src.user_breakdown_description)
            receipt = Receipt(create_tv(mark, desc), name)
            workshop.add_receipt(receipt)
            print(receipt)
            break
        elif type_of_device == "2":
            mark = input(src.user_mark)
            breakdown_description = input(src.user_breakdown_description)
            receipt = Receipt(create_computer(mark, breakdown_description), name)
            workshop.add_receipt(receipt)
            print(receipt)
            break
        elif type == "3":
            mark = input(src.user_mark)
            breakdown_description = input(src.user_breakdown_description)
            receipt = Receipt(create_mobile(mark, breakdown_description), name)
            workshop.add_receipt(receipt)
            print(receipt)
            break
        else:
            print(src.user_wrong)


def user(workshop):
    try:
        name, lastname, surname = who_are_u()
        while True:
            choice = input(src.user_application)
            if choice == "1":
                create_receipt(workshop, name)
                break
            else:
                break
    except Exception as e:
        print(e)


def main():
    workshop = Workshop([])
    while True:
        choice = input(src.main_path)
        if choice == "1":
            user(workshop)
        else:
            break


if __name__ == '__main__':
    main()
