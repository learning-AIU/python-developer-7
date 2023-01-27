"""Консольный файловый менеджер.

Дополнительный модуль: операции с файлами и каталогами."""

# импорт объектов из стандартной библиотеки
from shutil import rmtree, copytree, copy2

# импорт объектов из текущего пакета
from src import utils


__all__ = [
    'create_dir',
    'delete_file_or_dir',
    'copy_file_or_dir',
    'list_dir',
    'change_cwd',
]


datafile = utils.DATA_DIR / 'production/listdir.txt'


def create_dir() -> None:
    dir_name = input(utils.MESSAGES['ASK_DIR_NAME'])
    (utils.CWD / dir_name).mkdir(exist_ok=True)


def delete_file_or_dir() -> None:
    file_or_dir_name = input(utils.MESSAGES['ASK_FILE_OR_DIR_NAME'])
    path = utils.CWD / file_or_dir_name
    if path.is_dir():
        rmtree(path, ignore_errors=True)
    elif path.is_file():
        path.unlink(missing_ok=True)


def copy_file_or_dir() -> None:
    file_or_dir_name = input(utils.MESSAGES['ASK_FILE_OR_DIR_NAME'])
    source = utils.CWD / file_or_dir_name
    target_name = input(utils.MESSAGES['ASK_TARGET_NAME'])
    target = utils.CWD / target_name
    if source.is_dir():
        copytree(source, target)
    elif source.is_file():
        copy2(source, target)


def list_dir(*, only_files: bool = False, only_dirs: bool = False) -> None:
    print()
    files, dirs = [], []
    for item in utils.CWD.iterdir():
        if item.is_file():
            files += [item.name]
        elif item.is_dir():
            dirs += [item.name]
    buffer = ''
    if not only_files ^ only_dirs:
        print(*dirs, *files, sep='\n')
        buffer += ('files: ' + ', '.join(files) +
                   '\ndirs: ' + ', '.join(dirs))
    elif only_files:
        print(*files, sep='\n')
        buffer += 'files: ' + ', '.join(files)
    elif only_dirs:
        print(*dirs, sep='\n')
        buffer += 'dirs: ' + ', '.join(dirs)
    datafile.write_text(buffer, encoding='utf-8')


def change_cwd() -> None:
    new_path = utils.Path(input(utils.MESSAGES['ASK_PATH']))
    if new_path.is_dir():
        if new_path.is_absolute():
            utils.CWD = new_path
        else:
            utils.CWD = utils.SOURCE_DIR / new_path
    else:
        print(utils.ERROR_MESSAGES['DIR_NOT_FOUND'])

