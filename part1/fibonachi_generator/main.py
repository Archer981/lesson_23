# Напишите, свой собственный генератор,
# который отдавал бы N чисел фибоначчи
# (https://ru.wikipedia.org/wiki/Числа_Фибоначчи).
# Дополните функцию fib


def fib(n):
    if n == 1:
        yield 0
    elif n == 2:
        yield 0
        yield 1
    else:
        a = 0
        b = 1
        yield 0
        yield 1
        n -= 2
        while n > 0:
            c = a + b
            n -= 1
            yield c
            a, b = b, c


fib_gen = fib(15)

if __name__ == "__main__":
    print([x for x in fib_gen])
