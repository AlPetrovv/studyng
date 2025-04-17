from collections import deque


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


l = [1, 2, 3, [3123, 123, 123, [123123, 1231231], [123123123, [[1]]], [123]], 1231]


def get_sum(lst, res=0):
    for i in lst:
        if isinstance(i, list):
            res += get_sum(i)
        else:
            res += i
    return res


print(get_sum(l))


def sum_lst_deque(l):
    res = 0
    q = deque()
    q.appendleft(l)
    while q:
        c = q.pop()
        for i in c:
            if isinstance(i, list):
                q.appendleft(i)
            else:
                res += i
    return res


print(sum_lst_deque(l))
