LEFT = '0'
RIGHT = '1'

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def get_nodes(self):
        to_return = []
        if type(self.left) == str:
            to_return.append(self.left)
        else:
            to_return.append(self.left.get_nodes())

        if type(self.right) == str:
            to_return.append(self.right)
        else:
            to_return.append(self.right.get_nodes())
        
        spam = []
        for el in to_return:
            if type(el) == list:
                spam.append(el)
                for i in el:
                    to_return.append(i)

        if len(spam) != 0:
            for el in spam:
                to_return.remove(el)


        
        return to_return

    def __str__(self):
        return f"{self.left} - {self.value} - {self.right}"
    
def create_arr(string):
    arr = [[0, string[0]]]
    add = False
    for el in string:
        for i in range(len(arr)):
            if el == arr[i][1]:
                arr[i][0] += 1
                add = False
                break
            else:
                add = True
        
        if add:
            arr.append([1, el])
            add = False
    
    return sorting(arr)

def sorting(arr):
    for i in range(len(arr) - 1):
        if arr[i][0] > arr[i + 1][0]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

def create_tree(arr):
    arr = create_arr(arr)
    haferman_dict = {}
    for el in arr:
        haferman_dict.update({el[1]:''})
    while len(arr) != 1:
        to_left = arr.pop(0)  #arr[0]
        to_right = arr.pop(0)  #arr[1]

        spam = to_left[1]    #запись символа во временную переменную
        if type(spam) == str:
            haferman_dict[spam] += LEFT
        else:
            getted_el = spam.get_nodes()
            for el in getted_el:
                haferman_dict[el] += LEFT

        spam = to_right[1]
        if type(spam) == str:
            spam = to_right[1]
            haferman_dict[spam] += RIGHT
        else:
            getted_el = spam.get_nodes()
            for el in getted_el:
                haferman_dict[el] += RIGHT
        
        spam = to_left[0] + to_right[0] # подсчёт суммы ветки

        node = Node(left= to_left[1], right= to_right[1])
        arr.append([spam, node])
    
    # разворачиваем коды символов тк записывались в обратном порядке
    for key in haferman_dict:
        haferman_dict.update({key: haferman_dict[key][::-1]})

    return haferman_dict #node, arr      # удалить первый шарп для возврата всего "мусора" 

def bit_word_generate(string, dictionary):
    word = ''
    for el in string:
        word += dictionary[el]
    return word

def retranslate(word, dictionary):
    # разворачиваем словрь
    spam = {}
    for key in dictionary:
        spam.update({dictionary[key]: key})
    
    dictionary.clear()
    dictionary = spam.copy()

    # разбиваем битовое слово на отдельные биты
    spam = []
    for bit in word:
        spam.append(bit)
    word = spam.copy()


    string = ''
    spam = 1
    while len(word) != 0:
        if spam == 1:
            key = word[0:spam][0]
        else:
            buffer = word[0:spam]
            for el in buffer:
                key += el 

        if key in dictionary:
            string += dictionary[key]
            for _ in range(spam):
                word.pop(0)
            spam = 1
        else:
            spam += 1
        key = ''
        
    return string

string = input('Введите строку: ')
haferman_dict = create_tree(string)
print(haferman_dict) # Нужно сохранять, иначе он очищается
bit_word = bit_word_generate(string, haferman_dict)
translate_word = retranslate(bit_word, haferman_dict)
print(haferman_dict)
print(bit_word)
print(translate_word)