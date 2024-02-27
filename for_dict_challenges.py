# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
def name_students():
    str_students = ""
    for one_dict in students:
        str_students += one_dict['first_name']
        str_students += " "
    list_students = str_students.split() #создали список из словаря
    unique_students = set(list_students) #создали уникальное множество из списка
    for unique_name in unique_students:
        count = 0
        for list_name in list_students:
            if unique_name == list_name:
                count += 1
        print(f"{unique_name}: {count}")
        #прогнали циклом элементы уникального множества по списку всех учеников и учли количество повторений
name_students()
print() #просто пустая строка для разделения


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
def name_students():
    str_students = ""
    for one_dict in students:
        str_students += one_dict['first_name']
        str_students += " "
    list_students = str_students.split() #создали список из словаря
    unique_students = set(list_students) #создали уникальное множество из списка
    max_count = 0
    for unique_name in unique_students:
        count = 0
        for list_name in list_students:
            if unique_name == list_name:
                count += 1
                if count > max_count:
                    max_count = count
                    name_max = unique_name
    print(f"Самое частое имя среди учеников: {name_max}")
    #прогнали циклом элементы уникального множества по списку всех учеников и для наибольшего количества повторений добавили имя в отдельную переменную
name_students()
print() #просто пустая строка для разделения

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
def often_name():
    max_count = 0
    class_number = 0
    #почти то же самое, что и в прошлый раз, но теперь вложили прошлое решение еще в один цикл из-за еще одного уровня вложенности входных данных, также переместили некоторые переменные-счетчики на соответствующие уровни
    for i in school_students:
        class_number += 1
        str_students = ""
        for one_dict in i:
            str_students += one_dict['first_name']
            str_students += " "
        list_students = str_students.split() #создали список из словаря
        unique_students = set(list_students) #создали уникальное множество из списка
        for unique_name in unique_students:
            count = 0
            for list_name in list_students:
                if unique_name == list_name:
                    count += 1
                    if count > max_count:
                        max_count = count
                        name_max = unique_name
        print(f"Самое частое имя среди учеников в классе {class_number}: {name_max}")
        max_count = 0
        #прогнали циклом элементы уникального множества по списку всех учеников и для наибольшего количества повторений добавили имя в отдельную переменную
often_name()
print() #просто пустая строка для разделения

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

def boys_girls():
    for item_list in school: #лезем в словарь
        str_students = ''
        for one_dict in item_list['students']: #лезем в список по ключу
            str_students += one_dict['first_name']
            str_students += " "
        list_students = str_students.split() #создали список из словаря
        count_b = 0
        count_g = 0
        for pupil in list_students: #пробегаем каждым студентом из списка по словарю с булевыми полами
            if is_male.get(pupil) == True:
                count_b += 1
            else:
                count_g += 1
        print(f"Класс {item_list['class']}: девочки {count_g}, мальчики {count_b}")

boys_girls()
print() #просто пустая строка для разделения

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

def boys_girls(): #общий принцип подсчета почти такой же, как и в прошлом задании, но добавляются максимальные значения по полам и переменные для сохранения имени класса, где будет максимум
    max_count_girls = 0
    max_count_boys = 0
    name_boy_class = ""
    name_girl_class = ""
    for item_list in school:
        str_students = ''
        for one_dict in item_list['students']:
            str_students += one_dict['first_name']
            str_students += " "
        list_students = str_students.split() #создали список из словаря
        count_b = 0
        count_g = 0
        for pupil in list_students:
            if is_male.get(pupil) == True:
                count_b += 1
            else:
                count_g += 1
        if max_count_girls < count_g:
            max_count_girls = count_g
            name_girl_class = item_list["class"]
        if max_count_boys < count_b:
            max_count_boys = count_b
            name_boy_class = item_list['class']
    print(f"Больше всего мальчиков в классе {name_boy_class}\nБольше всего девочек в классе {name_girl_class} ")

boys_girls()