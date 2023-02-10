'''Какие ты видишь проблемы в следующем коде? 
Как его следует исправить? 
Исправь ошибку и перепиши код с использованием типизации'''

'''Ошибка в lambda. Чтобы исправить добавила в lambda переменную step,
добавленная переменная перехватывает текущее значение step и
передает его в lambda.
'''

'''Для проверки добавила тестовый обработчик step_plus_one.
'''

from collections.abc import Callable

def create_handlers(callback: Callable) -> list[Callable]:
    handlers = []
    for step in range(5):
        # добавляем обработчики для каждого шага (от 0 до 4)
        handlers.append(lambda step=step: callback(step))
    return handlers


def execute_handlers(handlers: list[Callable]) -> None:
    # запускаем добавленные обработчики (шаги от 0 до 4)
    for handler in handlers:
        handler()


def step_plus_one(step: int):
    print(f'{step} + 1 = {step + 1}')

handlers = create_handlers(step_plus_one)
execute_handlers(handlers)

