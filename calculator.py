from typing import Union

Number = Union[int, float]


def calculate_simple_interest(principal: Number, rate: Number, time: Number) -> float:
    """
    Вычисляет простой процент.

    Формула: principal * rate * time / 100
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Аргументы должны быть неотрицательными")

    return float(principal * rate * time / 100)


def calculate_compound_interest(
    principal: Number,
    rate: Number,
    time: Number,
    n: int = 1,
) -> float:
    """
    Вычисляет сложный процент.

    Формула: principal * (1 + rate/(100*n))**(n*time)
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Аргументы должны быть неотрицательными")

    if not isinstance(n, int) or n <= 0:
        raise ValueError("n должно быть положительным целым числом")

    return float(principal * (1 + rate / (100 * n)) ** (n * time))


def calculate_tax(amount: Number, tax_rate: Number) -> float:
    """
    Вычисляет сумму налога.

    Формула: amount * tax_rate / 100
    """
    if amount < 0:
        raise ValueError("Сумма должна быть неотрицательной")

    if tax_rate < 0 or tax_rate > 100:
        raise ValueError("Налоговая ставка должна быть от 0 до 100")

    return float(amount * tax_rate / 100)
