"""Операции с банковским счётом.

Основной модуль."""

# импорт объектов из стандартной библиотеки
from datetime import datetime as dt
from decimal import Decimal as dec
from json import load as jload, dump as jdump, JSONEncoder

# импорт объектов из текущего пакета
from src import utils


__all__ = [
    'start',
]


class JSONExtEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, dec):
            return f'{obj:.2f}'
        else:
            return super().default(obj)


datafile = utils.DATA_DIR / 'production/bank.json'

balance: dec = dec(0)
history: dict[dt, tuple[str, dec]] = {}


def read_from_datafile() -> None:
    global balance, history
    with open(datafile, encoding='utf-8') as filein:
        raw = jload(filein)
    balance = dec(raw['balance'])
    for timestamp, action in raw['history'].items():
        title, amount = action
        history[timestamp] = (title, dec(amount))


def write_to_datafile() -> None:
    raw = {
        'balance': balance,
        'history': history,
    }
    with open(datafile, 'w', encoding='utf-8') as fileout:
        jdump(raw, fileout, ensure_ascii=False, indent=2, cls=JSONExtEncoder)


def get_menu_element() -> str:
    print(f"""\n{utils.draw_title('меню банка')}
  1. проверка баланса
  2. пополнение счета
  3. покупка
  4. история покупок
  5. выход""")
    while True:
        inp = input(' > введите номер > ')
        if inp in set('12345'):
            return inp
        else:
            print(' _ неверный пункт меню _ ')


def get_balance() -> str:
    return f'\n = текущий баланс: {balance:.2f} ₽ = '


def deposit() -> None:
    global balance
    balance += dec(input(' > введите сумму пополнения > '))


def buy() -> None:
    global balance, history
    amount = dec(input(' > введите сумму покупки > '))
    if amount <= balance:
        balance -= amount
        title = input(' > введите название покупки > ')
        history |= {dt.now().strftime('%H:%M:%S %d.%m.%y'): (title, amount)}
    else:
        print(' _ недостаточно средств _ ')


def show_history() -> str:
    result = '\n = история покупок = '
    for timestamp, action in history.items():
        result += f'\n  {timestamp} — {action[0]}: {action[1]:.2f} ₽'
    return result


def start():
    """Точка входа."""
    if datafile.is_file():
        read_from_datafile()
    while True:
        choice = get_menu_element()

        if choice == '1':
            print(get_balance())

        elif choice == '2':
            deposit()

        elif choice == '3':
            buy()

        elif choice == '4':
            print(show_history())

        elif choice == '5':
            break
    write_to_datafile()
