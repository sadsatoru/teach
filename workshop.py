import DEVICES
import receipt
import random
import datetime


class Workshop:
    def __init__(self, receipt_fio: list):
        self.receipt = {receipt.id: receipt for receipt in receipt_fio}

    def add_receipt(self, new_receipt):
        self._receipt.update({new_receipt.id: new_receipt})

    def remove_receipt(self, receipt_id):
        self.__receipt.pop(receipt_id)

    def get_receipt(self, receipt_id):
        return self.receipt[receipt_id]

    def get_receipt_fio(self, fio):
        receipt_fio = []
        for receipt in self._receipt.values():
            if receipt._fio == fio:
                receipt_fio.append(receipt)
            return receipt_fio
