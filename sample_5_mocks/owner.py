"""
Jako rozwinięcie dodamy klasę Owner -  właściciela portfela.

Założenia:
* Obiekt przetrzymuje informacje o imieniu (self.first_name) i nazwisko (self.last_name) właściciela oraz instancje
  portfela (prywatnie self._wallet). Konstruktor przyjmuje te 3 zmienne.
* Metoda supply_wallet(cash) dodająca określoną sumę pieniędzy do portfela
* Metoda withdraw_money(cash) wyciąga odpowienią sumę pieniędzy z portfela
* Metoda check_if_can_afford(cash) pozwala sprawdzić czy właściciela stać na zakup rzeczy poprzez porównanie ceny
  z dostępnymi środkami. True jeżeli właściciel może sobie pozwolić na zakup, False w innym przypadku.
"""

from sample_5_mocks.wallet import Wallet


class Owner:

    def __init__(self, first_name, last_name, wallet: Wallet):
        self.first_name = first_name
        self.last_name = last_name
        self._wallet = wallet

    def supply_wallet(self, cash):
        self._wallet.add_cash(cash=cash)

    def withdraw_money(self, amount):
        self._wallet.spend_cash(spending=amount)

    def check_if_can_afford(self, amount):
        return self._wallet.get_balance() >= amount


if __name__ == '__main__':
    wallet = Wallet()
    owner = Owner(first_name='Ala', last_name='Makota', wallet=wallet)

    owner.supply_wallet(cash=10)
    owner.withdraw_money(amount=5)

    print(owner.check_if_can_afford(amount=10))
    print(owner.check_if_can_afford(amount=5))

    t = 0
