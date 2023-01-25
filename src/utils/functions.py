"""Консольный файловый менеджер.

Дополнительный модуль: вспомогательные функции."""

# импорт объектов из стандартной библиотеки
from os import name as os_type
from shutil import get_terminal_size as gts
from string import punctuation
from sys import modules, platform

# импорт объектов из текущего пакета
from src.utils import data


__all__ = [
    'draw_title',
    'show_menu',
    'get_menu_entry',
    'os_platform',
    'show_credits',
]


width = gts()[0] - 1


def draw_title(text: str, *, upper: bool = False, accent: bool = False) -> str:
    text = text.upper() if upper else text.title()
    half_width, mod = divmod(width-len(text)-2, 2)
    filler = '=' if accent else '+'
    return f'{filler*half_width} {text} {filler*(half_width+mod)}'


def show_menu():
    print('\n', draw_title(data.MESSAGES['MAIN_MENU_TITLE']), sep='')
    for i, entry in enumerate(data.MainMenu, 1):
        print(f' {i}. {entry.value}')


def get_menu_entry() -> data.MainMenu:
    while True:
        inp = input(data.PROMPT)
        if inp.isdecimal():
            inp = int(inp)
            if inp in range(1, len(data.MainMenu)+1):
                return list(data.MainMenu)[inp-1]
            else:
                print(data.ERROR_MESSAGES['RANGE'])
        else:
            print(data.ERROR_MESSAGES['DIGITS'])


def os_platform() -> None:
    print(f'\n{os_type.upper()} — {platform}')


def show_credits() -> None:
    app_name = modules['__main__'].__doc__.split('\n')[0].strip(punctuation)
    print(f'\n{app_name}, {data.CUR_YEAR}.\n'
          f'Разработка: {data.AUTHOR}.')

