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

students_name_counter = {}
for student_record in students:
    name = student_record['first_name']
    if name not in students_name_counter:
        students_name_counter[name] = 1
    else:
        students_name_counter[name] += 1
for k, v in students_name_counter.items():
    print(k, ": ", v)

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

students_name_counter = {}
for student_record in students:
    name = student_record['first_name']
    if name not in students_name_counter:
        students_name_counter[name] = 1
    else:
        students_name_counter[name] += 1
    max_count = 0
    name_max = ""
    for name_value in students_name_counter:
        count = 0
        if students_name_counter.get(name_value) > max_count:
            max_count = students_name_counter.get(name_value)
            name_max = name_value
print(f"Самое частое имя среди учеников: {name_max}")

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
        {'first_name': 'Оля'}
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

class_number = 0
for list_item in school_students:
    class_number += 1
    max_count = 0
    name_max = ""
    students_name_counter = {}
    for student_record in list_item:
        name = student_record['first_name']
        if name not in students_name_counter:
            students_name_counter[name] = 1
        else:
            students_name_counter[name] += 1
        for name_value in students_name_counter:
            if students_name_counter.get(name_value) > max_count:
                max_count = students_name_counter.get(name_value)
                name_max = name_value
    print(f"Самое частое имя среди учеников в классе {class_number}: {name_max}")

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

for class_dict in school: #лезем в словарь
    count_boys = 0
    count_girls = 0
    for name_dict in class_dict['students']: #лезем в список по ключу
        name = name_dict['first_name']
        if is_male.get(name) == True:
            count_boys += 1
        else:
            count_girls += 1
    print(f"Класс {class_dict['class']}: девочки {count_girls}, мальчики {count_boys}")

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

max_count_girls = 0
max_count_boys = 0
main_boy_class = ""
main_girl_class = ""
for class_dict in school: #лезем в словарь
    count_boys = 0
    count_girls = 0
    for name_dict in class_dict['students']: #лезем в список по ключу
        name = name_dict['first_name']
        if is_male.get(name) == True:
            count_boys += 1
        else:
            count_girls += 1
    if max_count_girls < count_girls:
        max_count_girls = count_girls
        main_girl_class = class_dict["class"]
    if max_count_boys < count_boys:
        max_count_boys = count_boys
        main_boy_class = class_dict['class']
print(f"Больше всего мальчиков в классе {main_boy_class}\nБольше всего девочек в классе {main_girl_class}")