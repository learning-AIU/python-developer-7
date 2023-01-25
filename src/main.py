"""Консольный файловый менеджер.

Основной модуль: точка входа."""

# импорт пакетов проекта
import bank
import quiz
import utils


def main():
    print(f'\n{utils.draw_title(utils.TITLE, upper=True, accent=True)}')
    while True:
        utils.show_menu()
        choice = utils.get_menu_entry()

        if choice is utils.MainMenu.ADD:
            utils.create_dir()

        elif choice is utils.MainMenu.COPY:
            utils.copy_file_or_dir()

        elif choice is utils.MainMenu.DEL:
            utils.delete_file_or_dir()

        elif choice is utils.MainMenu.DIR:
            utils.list_dir()

        elif choice is utils.MainMenu.DIR_D:
            utils.list_dir(only_dirs=True)

        elif choice is utils.MainMenu.DIR_F:
            utils.list_dir(only_files=True)

        elif choice is utils.MainMenu.CD:
            utils.change_cwd()

        elif choice is utils.MainMenu.OS:
            utils.os_platform()

        elif choice is utils.MainMenu.AUTHOR:
            utils.show_credits()

        elif choice is utils.MainMenu.BANK:
            bank.start()

        elif choice is utils.MainMenu.QUIZ:
            quiz.play()

        elif choice is utils.MainMenu.QUIT:
            break


# точка входа
if __name__ == '__main__':
    main()
