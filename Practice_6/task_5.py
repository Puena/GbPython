import random


word_first = ["дом", "огонь", "лес", "автомобиль", "город"]
word_second = ["ночью", "завтра", "вчера", "сегодня", "позавчера"]
word_third = ["мягкий", "зеленый", "яркий", "веселый", "утопичный"]
random.shuffle(word_first)
random.shuffle(word_second)
random.shuffle(word_third)

zipped = zip(word_first, word_second, word_third)
print(list(zipped))
