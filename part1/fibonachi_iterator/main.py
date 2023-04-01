# Напишите, свой собственный итератор,
# который отдавал бы N чисел фибоначчи
# (https://ru.wikipedia.org/wiki/Числа_Фибоначчи).
# Для решения задачи нужно дополнить класс Fib
# Достаточно будет сделать итератор только для положительных чисел


class Fib:
    def __init__(self, n):
        self.n = n
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < 1:
            raise StopIteration
        else:
            self.c = self.a + self.b
            self.n -= 1
            self.a, self.b = self.b, self.c
            return self.c



fib = Fib(15)

if __name__ == "__main__":
    print([x for x in fib])
