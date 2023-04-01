# Вам нужно написать функцию counter, 
# которая должна подсчитать количество городов в регионах. 
# На вход функция принимает towns - список объектов Town, 
# на выходе должна возвращать словарь, 
# где ключ - регион, значение - количество городов в этом регионе. 
# Для решения задачи следует применить defaultdict.
from collections import namedtuple, defaultdict

Town = namedtuple('Town', ['name', 'region'])
 
towns = [Town('балашиха', 'мо'), Town('химки', 'мо'), Town('тула', 'тульская область')]


def counter(towns):
    result = defaultdict(int)
    for town in towns:
        result[town.region] += 1
    return result


if __name__ == "__main__":
    print(counter(towns))
