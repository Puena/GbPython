# Предоставлен список чисел необходимо вывевести элементы исходного списка значения которых больше предыдущих
user_input = int(input("Введите максимальное число последовательности "))
input_array = [n for n in range(20, user_input+1) if n %
               20 == 0 or n % 21 == 0]
print(input_array)