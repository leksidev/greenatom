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
print(execute_handlers(handlers))

