# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])
print() #просто пустая строка для разделения


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(len(word))
print() #просто пустая строка для разделения


# Вывести количество гласных букв в слове
word = 'Архангельск'
def count_vowels(word):
    word = word.lower()
    count = 0
    for k in word:
        if k in 'ауеыоэияю':
            count += 1
    print(count)
count_vowels(word)
print() #просто пустая строка для разделения

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))
print() #просто пустая строка для разделения

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
def first_letter(sentence):
    list_sentence = sentence.split()
    for item in list_sentence:
        print(item[0])
first_letter(sentence)
print() #просто пустая строка для разделения

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
def len_avg_word(sentence):
    list_sentence = sentence.split()
    print(round(len(sentence)/len(list_sentence)))
len_avg_word(sentence)