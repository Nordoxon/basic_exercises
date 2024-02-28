# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])
print() #просто пустая строка для разделения


# Вывести количество букв "а" в слове
word = 'Архангельск'
word = word.lower()
count = 0
for k in word:
	if k == 'а':
	    count += 1
print(count)
print() #просто пустая строка для разделения


# Вывести количество гласных букв в слове
word = 'Архангельск'
word = word.lower()
count = 0
for k in word:
    if k in 'ауеыоэияю':
        count += 1
print(count)
print() #просто пустая строка для разделения

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))
print() #просто пустая строка для разделения

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
list_sentence = sentence.split()
for item in list_sentence:
    print(item[0])
print() #просто пустая строка для разделения

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
list_sentence = sentence.split()
str_list_sentence = (''.join(list_sentence))
print((len(str_list_sentence)/len(list_sentence)))