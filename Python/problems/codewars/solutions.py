def narcissistic(value: float | int) -> bool:
    len_digits = len(str(value))
    return summ_narcissistic(value, len_digits) == value


def summ_narcissistic(value: float | int, len_digits: int | None = None) -> int:
    if value >= 1:
        number = value % 10
        res = summ_narcissistic(value // 10, len_digits) + ((number % 10) ** len_digits)
    else:
        res = 0
    return res
