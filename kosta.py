import os
name = input("как зовут перса ")
if not name: name = "Илья Муромец "
way_1 = True
way_2 = True
way_3 = True
game = True
user_hp = 10
varvar_hp = 10
key = ""
while game:
    if way_1 or way_2 or way_3:
        key == ""
        print ("у камня ")
        if way_1:
            print ("первый вариант ")
        if way_2:
            print ("второй вариант ")
        if way_3:
            print ("третий вариант ")
        user_choise = input("введите номер решения")
        key += user_choise
        os.system("cls")
        print("1 дорога ")
        print("2 дорога ")

    if key == "1":
        print("дорога 1 - хорошо ")
        input("нажмите энтер для продолжения")
        game = False
    if key =="2":
        print("плохая концовка :(")
        input("нажмите энтер для продолжения")
        os.system("cls")
    if key =="3":
        print("1 дорога :)")
        game = False

print("конец {name} ")