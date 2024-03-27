# Ввод списка из трёх слов
word_list = input("Введите три слова через пробел: ").split()
# Ввод текста произведения
text = input("Введите текст произведения: ")

# Разделение текста на слова
text_words = text.split()
count = 0
# Подсчет количества вхождений слов из списка
for word in word_list:
    count += text_words.count(word)

print(f"Слова встречаются в тексте {count} раз")
