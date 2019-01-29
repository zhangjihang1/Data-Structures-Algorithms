#!user/bin/env python
# -*- coding:utf-8 -*-

"""
@author:zjh
@file:test.py
@time:2019/01/27
"""


class CreditCard:
    """A consumer credit card"""

    def __init__(self, customer, bank, acnt, limit):

        """Create a new credit card instance.

        Tne initial balance is zero.

        customer  the name of the customer(e.g., 'John Bowman')
        bank  the name of bank(e.g. 'California Savings')
        acnt  the account identifier(e.g. '5391 0375 9387 5309')
        limit credit limit(measured in dollars)
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """return name of the customer."""
        return self._customer

    def get_bank(self):
        """return the bank's name."""
        return self._bank

    def get_account(self):
        """return the card identifying number(typically stored as a string)."""
        return self._account

    def get_limit(self):
        """return current credit limit."""
        return self._limit

    def get_balance(self):
        """return current balance."""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        """
        if not isinstance(price, (int, float)):
            raise ValueError('Price must be a number.')
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount


# if __name__ == '__main__':
#     wallet = []
#     wallet.append(CreditCard('zjh', '1st Bank', '123', 10000))
#     wallet.append(CreditCard('zjh', '2ed Bank', '456', 20000))
#     wallet.append(CreditCard('zjh', '3rd Bank', '789', 30000))
#
#     for val in range(1, 17):
#         wallet[0].charge(val)
#         wallet[1].charge(2 * val)
#         wallet[2].charge(3 * val)
#
#     for c in range(3):
#         print('Customer = ', wallet[c].get_customer())
#         print('Bank = ', wallet[c].get_bank())
#         print('Account = ', wallet[c].get_account())
#         print('Limit = ', wallet[c].get_limit())
#         print('Balance = ', wallet[c].get_balance())
#         while wallet[c].get_balance() > 100:
#             wallet[c].make_payment(100)
#             print('New balance = ', wallet[c].get_balance())
#         print('*************************')


class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""
    OVER_LIMIT_FEE = 5

    def __init__(self, customer, bank, acnt, limit, apr):
        """Creat a new predatory credit card instance.

        The initial balance is zero.

        customer  the name of the customer(e.g., 'John Bowman')
        bank  the name of bank(e.g. 'California Savings')
        acnt  the account identifier(e.g. '5391 0375 9387 5309')
        limit credit limit(measured in dollars)
        apr  annual percentage rate(e.g., 0.0825 for 8.25% APR)
        """

        super().__init__(customer, bank, acnt, limit)  # call super constructor
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed.
        Return False  and assess $5 if charge was denied.
        """
        success = super().charge(price)
        if not success:
            self._balance += PredatoryCreditCard.OVER_LIMIT_FEE
        return success

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplication factor
            monthly_factor = pow(1 + self._apr, 1 / 12)
            self._balance *= monthly_factor
