# Вам нужно написать функцию top3, 
# которая на вход принимает строку и 
# возвращает 3 наиболее повторяющихся элемента из входной строки. 
from collections import Counter

def top3(input_str):
    result = Counter(input_str).most_common()
    return [result[i][0] for i in range(3)]


if __name__ == "__main__":
    print(top3('11111111222222223333333344444444555555'))
