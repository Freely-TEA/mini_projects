from random import randint
from statistics import median


MIN_ = -100
MAX_ = 100


""" 
Нашёл я на хабре метод поиска медианы одного человека
https://habr.com/ru/post/346930/   <-  ссылка
Почитал, посмотрел код и понял что мне нравится метод, но не нравится код
Переписал, сохранив алгоритм. Не совсем. Пришлось переосмыслить его на бумаге 
Скину в чат фото листка, если надо будет, там интересные зарисовки
Вообще спасло то, что кол-во чисел в массиве нечётное иначе нужно переделыватть логику

Есть проблема с большими массивами. Рекурсия нестабильна и может вывалится из-за ограничения вызовов
"""

class MedianNotSorted:
    def __init__(self, getted_arr):
        # на случай если массив короткий
        if len(arr) in (0, 1):
            print("Get wrong array")
            return None

        self.arr = arr
        self.arr_default_len = len(getted_arr)
        self.last_left_len = None # На будущее ВАЖНОЕ

        # на этой позиции (ниже) должна находится медиана
        self.needed_minimal = self.arr_default_len // 2 + 1

    # основной метод
    def get_median(self):
        while type(self.arr) == list:
            self.arr = self.founder(self.arr)

        self.median = self.arr
        return self.median

    # получение рандомного числа указателя
    def get_pivot(self, arr):
        return randint(0, len(arr) - 1)

    # для проверки массива на случай множества повторений медианы
    def arr_checker(self, arr):
        if len(arr) == 0:
            return "Что за дичь"
        if len(arr) == 1:
            return True
        if arr[0] == arr[1]:
            return True
        return False  


    def founder(self, arr):
        # если поспешно нашли медиану (возможно никчему)
        if len(arr) == 1:
            return arr[0]
        if len(arr) == 0:
            return f"ERROR"


        # создаём указатель и области меньше-больше
        pivot = self.get_pivot(arr)
        left, right = [], []
    # процесс сравнения и разбиения
        for el in arr:
            if el > arr[pivot]:
                right.append(el) # тут больше чем число под указателем
            elif el <= arr[pivot]:
                left.append(el) # a тут меньше
        """ тут был способ оптимизации, который я не доработал """

        # если повезло найти медиану
        if len(left) == self.needed_minimal:
            if len(left) != 1:
                pass
            else:
                return left[0]
        # если медиана в левой части
        if len(left) >= self.needed_minimal:
            if len(left) == self.last_left_len:
                if self.arr_checker(left):
                    return left[0]
            self.last_left_len = len(left)
            return left
        #если медиана в правой части
        elif len(left) < self.needed_minimal:
            self.needed_minimal -= len(left)
            return right 
        


#user_len = int(input("Введите m #"))
user_len = int(input("Введите m #"))
arr = [randint(MIN_, MAX_) for _ in range(user_len * 2 + 1)]
print(f"Исходный массив: {arr}")
print(f"Медиана, полученная читом: {median(arr)}")

arrs = MedianNotSorted(arr)
arrs = arrs.get_median()

print(f"Медиана, полученная классом: {arrs}")

