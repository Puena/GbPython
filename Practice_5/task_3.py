# Создайте программу для игры в ""Крестики-нолики"".


def create_field():
    return [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

def get_user_name(message:str, users: dict):
    while (True):
        name = input(message)
        if name in users:
            print("Имя уже занято, введите псевдоним!")
        else:
            users[name] = list()
            break

def is_win(field: list):
    sum_to_win = 3
    row_sum = 0
    column_sum = 0
    diagonal_left_sum = 0
    diagonal_right_sum = 0
    is_not_empty = True

    for i in range(len(field)):
        for j in range(len(field[i])):
            row_sum += field[i][j]
            column_sum += field[j][i]
            
            if(field[i][j] == 0):
                is_not_empty = False
            if i == j:
                diagonal_left_sum += field[i][j]
            if len(field[i]) -1 -i == j:
                diagonal_right_sum += field[i][j]
        if abs(row_sum) == sum_to_win or abs(column_sum) == sum_to_win:
            return 1
        else:
            row_sum = 0
            column_sum = 0
            
    
    if abs(diagonal_left_sum) == sum_to_win or abs(diagonal_right_sum) == sum_to_win:
        return 1
    
    if is_not_empty:
        return -1
    
    return 0

def get_mark(val: int):
    marks = {
        -1: "O",
        1: "X"
    }
    
    if val in marks:
        return marks[val]
    else:
        return " "

def print_field(field: dict):
    count = 1
    
    for i in range(len(field)):
        print()
        for j in range(len(field[i])):
            if 0 == j or j == len(field[i]):
                print(" ", end="")
            else:
                print("|", end="")
            print(f"  {get_mark(field[i][j])}   ", end="")
            count += 1
        print("\n")
        for c in range(count - len(field), count):
            print(f"---{c}---", end="")
        print()
        
def handle_user_input(field: list, sign: int, name: str, users: dict):
    max_number = len(field) * len(field[0])
    while (True):
        try:
            cell_number = int(input(f"{name} укажите номер ячейки: "))
            cell_number = cell_number - 1
            if 0 <= cell_number < max_number:
                change_cell(cell_number, sign, field)
                users[name].append(cell_number)
                return cell_number
            else:
                raise ValueError("Wrong number")
        except:
            print("Не допустимое знаЧение, повторите ввод!")
            continue

       
def change_cell(cell_number: int, sign: int, field: list):
    row = cell_number // 3
    col = cell_number % 3
    
    if (field[row][col] != 0):
        raise ValueError("Не пустое поле!")
  
    field[row][col] = sign


def tik_tak_game():
    users = dict()
    get_user_name("Введите имя первого игрока ", users)
    get_user_name("Введите имя второго игрока ", users)
    
    field = create_field()
    game = is_win(field)
    print_field(field)
    while (game == 0):
        sign = 1
        for name, _ in users.items():
            handle_user_input(field, sign, name, users)
            print_field(field)
            game = is_win(field)
            if game == 1:
                print(f"Выиграл игрок {name}")
                return
            elif game == -1:
                print("Ничья")
                return
            sign *= -1
    
        
    
    
tik_tak_game()