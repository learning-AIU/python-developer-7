from src.bank import bank

from pytest import mark


class TestGetBalance:

    @mark.parametrize('test_number', [0, 123, -4, ])
    def test_integer(self, test_number):
        bank.balance = test_number
        result = bank.get_balance()
        expected = f'\n = текущий баланс: {bank.balance:.2f} ₽ = '
        assert result == expected

    @mark.parametrize('test_number', [0.0, 1.2, -0.1])
    def test_float(self, test_number):
        bank.balance = test_number
        result = bank.get_balance()
        expected = f'\n = текущий баланс: {bank.balance:.2f} ₽ = '
        assert result == expected

