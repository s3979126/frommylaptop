"""
CLASS - OBJECT
caculate the distance

"""


class Account:
    currency = '$'  # public
    _min = 10.  # protected
    __max = 1000.0  # private

    def __init__(self, person, amount):
        self.__balance = amount  # private
        self._owner = person  # protected
        self.status = 'OK'  # public

    def get_info(self):  # public
        return [self.status]

    def get_loan_limit(self):  # public
        return self.__get_income() * 5

    def _get_more_info(self):  # protected
        return self.get_info() + [self._owner]

    def __get_income(self):  # private
        return self.__balance + 100
    def new_min(self,newmin):
        self._min=newmin
    def new_max(self,newmax):
        self._Account__max=newmax
"""this work"""
# print('maximum allowed:', Account._Account__max) # error
# a = Account('Adam', 100)
# print('balance:', a._Account__balance) # error
# print('income:', a._Account__get_income()) # error
"""this wont work"""
# print(dir(Account))
# print('maximum allowed:', Account.__max) # error
# a = Account('Adam', 100)
# print('balance:', a.__balance) # error
# print('income:', a.__get_income()) # error
print('minimum allowed:', Account._min)
a = Account('Adam', 100)
print('owner:', a._owner)
print('more info:', a._get_more_info())
print(a._Account__max)
print(a.new_min(80))
print(a.new_max(9))
print(Account.new_min(90))



