with open('text.txt', 'r') as file: #Открываем файл для чтения
    text = file.read()   #Читаем содержимое файла
words = text.split() #Разбиваем текст на слова
word_count = len(words) #Подсчитываем количество слов
print("Количество слов в файле:", word_count) #Выводим количество слов
