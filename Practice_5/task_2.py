# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from random import randint


BOT_NAME = "(-_0)"

def calculate_max_pick(current_value, max_value):
    if max_value > current_value:
        return current_value
    else:
        return max_value


def get_user_name(message:str, users: dict):
    while (True):
        name = input(message)
        if name in users or name == BOT_NAME:
            print("Имя уже занято, введите псевдоним!")
        else:
            users[name] = list()
            break

def get_input(name, count, max_pick):
    default_pick = calculate_max_pick(count, max_pick)
    
    while True:
        try:
            number = int(input(f"{name} возмите от 1 до {default_pick} кофет "))
        except:
            print("Вы ввели недопустимое число. Повторите ввод")
            continue
        
        if not default_pick >= number > 0:
            print("Вы ввели недопустимое число. Повторите ввод")
        else:
            break
        
    return number
    

def print_stats(users: dict, user_name: str):
    for name, total_pick in users.items():
        if name == user_name:
            print(f"Пользователь {name} забрал конфеты за {len(total_pick)} ходов.")
            
def init_ai(users: dict): 
    users[BOT_NAME] = list()
    
def ai_input(count, user_input, max_step):
    key_number = max_step + 1
    
    if (count - (key_number - user_input)) % key_number == 0:
        step = key_number - user_input
    else:
        step = count % key_number
        
    if step == 0:
        step = randint(1, key_number-1)
        
    if step > count:
        step = count
    
    print(f"{BOT_NAME} забрал {step} конфет")
    return step

def game_2021():
    users = dict()
    game = 2021
    max_step_pick = 280
    count = game
    
    get_user_name("Введите имя первого игрока ", users)
    if input("Вы хотите сыграть с БОТОМ? Y/n ").capitalize() == "Y":
        init_ai(users)
    else:
        get_user_name("Введите имя второго игрока ", users)
    
    print("Game started!")
    
    while count > 0:
        last_user_input = 0
        for name, _ in users.items():
            print(f"Осталост {count} конфет")
            if name == BOT_NAME:
                pick = ai_input(count, last_user_input, max_step_pick)
            else: 
                pick = get_input(name, count, max_step_pick)
                last_user_input = pick
               
            users[name].append(pick)
            count -= pick
            
            if count == 0:
                print(f"Выиграл игрок с именем: {name}")
                print_stats(users, name)
                return
        

game_2021()

