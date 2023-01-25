"""Консольный файловый менеджер.

Дополнительный модуль: операции с файлами и каталогами."""

# импорт объектов из стандартной библиотеки
from shutil import rmtree, copytree, copy2

# импорт объектов из текущего пакета
from src.utils import data


__all__ = [
    'create_dir',
    'delete_file_or_dir',
    'copy_file_or_dir',
    'list_dir',
    'change_cwd',
]


def create_dir() -> None:
    dir_name = input(data.MESSAGES['ASK_DIR_NAME'])
    (data.CWD / dir_name).mkdir(exist_ok=True)


def delete_file_or_dir() -> None:
    file_or_dir_name = input(data.MESSAGES['ASK_FILE_OR_DIR_NAME'])
    path = data.CWD / file_or_dir_name
    if path.is_dir():
        rmtree(path, ignore_errors=True)
    elif path.is_file():
        path.unlink(missing_ok=True)


def copy_file_or_dir() -> None:
    file_or_dir_name = input(data.MESSAGES['ASK_FILE_OR_DIR_NAME'])
    source = data.CWD / file_or_dir_name
    target_name = input(data.MESSAGES['ASK_TARGET_NAME'])
    target = data.CWD / target_name
    if source.is_dir():
        copytree(source, target)
    elif source.is_file():
        copy2(source, target)


def list_dir(*, only_files: bool = False, only_dirs: bool = False) -> None:
    print()
    for item in data.CWD.iterdir():
        if not only_files ^ only_dirs:
            print(item.name)
        elif only_files and item.is_file():
            print(item.name)
        elif only_dirs and item.is_dir():
            print(item.name)


def change_cwd() -> None:
    new_path = data.Path(input(data.MESSAGES['ASK_PATH']))
    if new_path.is_dir():
        if new_path.is_absolute():
            data.CWD = new_path
        else:
            data.CWD = data.SOURCE_DIR / new_path
    else:
        print(data.ERROR_MESSAGES['DIR_NOT_FOUND'])

