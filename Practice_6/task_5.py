# Реализовать функцию возвращающую n штук шуток, сформированных случыйным образом из слов взятых из трёх списков - по одному из каждого
import random


word_first = ["дом", "огонь", "лес", "автомобиль", "город"]
word_second = ["ночью", "завтра", "вчера", "сегодня", "позавчера"]
word_third = ["мягкий", "зеленый", "яркий", "веселый", "утопичный"]
random.shuffle(word_first)
random.shuffle(word_second)
random.shuffle(word_third)

input = int(input("Введите число шуток от 1 до 5 "))

zipped = zip(word_first, word_second, word_third)
print(list(zipped)[:input])
