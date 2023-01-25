"""Викторина.

Основной модуль."""

# импорт объектов из стандартной библиотеки
from random import randrange, shuffle

# импорт объектов из внешних пакетов проекта
from src import utils
# импорт объектов из текущего пакета
from src.quiz import data


__all__ = [
    'play'
]


answers = {
    'total': 0,
    'correct': 0,
    'wrong': 0,
}


def get_letter(word, mask):
    if not mask:
        return '*' * len(word)
    while True:
        i = randrange(len(word))
        if mask[i] == '*':
            mask = mask[:i] + word[i] + mask[i+1:]
            break
    return mask


def calc_stats() -> str:
    """Возвращает статистику результатов игры в форматированном виде.

    Процент правильных ответов считается от количества вопросов. Процент неправильных ответов считается от всех ответов.
    """
    # КОММЕНТАРИЙ: спросить про литералы в дата-файлах, исходниках и тестах
    return (f"Количество правильных ответов: {answers['correct']}\n"
            f"Процент отвеченных вопросов: {answers['correct'] * 100 / len(data.QA):.0f}%\n"
            f"Количество неправильных ответов: {answers['wrong']}\n"
            f"Процент неправильных ответов: {answers['wrong'] * 100 / answers['total']:.0f}%")


def play():
    """Точка входа."""
    print(f"\n{utils.draw_title('викторина')}")

    quit: bool = False

    question_list = list(data.QA.keys())
    shuffle(question_list)

    while True:
        for question in question_list:
            print(f"\n{question}\n")
            mask = ''
            let_in_ans = len(data.QA[question])
            while True:
                mask = get_letter(data.QA[question], mask)
                prompt = f"{let_in_ans} букв: {mask}\nваш ответ: "
                answer = input(prompt)
                answers['total'] += 1
                if answer == data.QA[question]:
                    print(data.MESSAGES['CORRECT'])
                    answers['correct'] += 1
                    break
                elif answer.lower().strip() in data.QUIT_KW:
                    print(data.MESSAGES['QUIT'])
                    quit = True
                    break
                else:
                    answers['wrong'] += 1
                    if mask.count('*') > 1:
                        print(data.MESSAGES['INCORRECT'])
                    else:
                        print(f"Правильный ответ: {data.QA[question]}\n")
                        break
            if quit:
                break
        print(calc_stats(), end='\n\n')
        if quit or input(data.MESSAGES['NEW']).lower().strip() != 'y':
            break
        print()
