import database
import students_controller


def main():
    database.init()
    students_controller.help_info()
    print("For exit, type: exit")
    active = True
    while active:
        u_input = input("Enter command please!\n")
        students_controller.handle(u_input)
        if u_input == "exit":
            active = False


main()
