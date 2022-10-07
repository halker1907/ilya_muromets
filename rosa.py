import os
import random

name = input("как вас зовут? ")
if not name:
    name = "Илья"

way_1 = True
way_2 = True
way_3 = True
game = True
key = ""

while game:

    if (way_1 or way_2 or way_3) and key == "":
        key = ""
        os.system("cls")
        print(f"у камня {name} ")
        if way_1:
            print("1 - дорога ")
        if way_2:
            print("2 - дорога")
        if way_3:
            print("3 - дорога")

        user_choice = input("введите номер ответа и нажмите ENTER ")
        if user_choice == "1" and way_1:
            key += user_choice
        if user_choice == "2" and way_2:
            key += user_choice
        if user_choice == "3" and way_3:
            key += user_choice

    if way_1 and key == "1":
        os.system("cls")
        print("дорога 1 ты встретил разбойников")
        print("1 - сбежать ")
        print("2 - сразиться")

        user_choice = input("Введите номер ответа и нажмите ENTER ")
        if user_choice == 1 or user_choice == 2 or user_choice == 3:
            key += user_choice
        if user_choice == "1" and way_1:
            key += user_choice
        if user_choice == "2" and way_2:
            key += user_choice
        if user_choice == "3" and way_3:
            key += user_choice

    if way_1 and key == "11":
        os.system("cls")
        print("1 - ты сбежал, но тебя нашли и повесили")
        way_1 = False
        key = ""

    if way_1 and key == "12":
        os.system("cls")
        print("2 - ты сразился и победил теперь все что у них было твое")
        game = False
        key = ""

    if way_2 and key == "2":
        os.system("cls")
        print("дорга 2 ты встретил ведьму")
        print("1 - короче суда или")
        print("2 - суда")


        user_choice = input("введите номер ответа и нажмите ENTER ")
        if user_choice == 1 or user_choice == 2:
            key += user_choice

    # key == "22"

    if way_2 and key == "21":
        os.system("cls")
        secret = random.randint(1, 100)
        print("ведьма загадала число от 1 до 100. отгадай его.")
        attempts = 7
        while attempts:
            print(f"у вас {attempts} попыток")
            user_choice = int(input("введите число"))
            if user_choice == secret:
                print("угадал")
                key = ""
                way_2 = False
                break
            elif user_choice > secret:
                print("многовато")
                attempts -= 1
            else:
                print("маловато")
                attempts -= 1
        else:
            print("проиграл")
            game = False

    if way_2 and key == "22":
        os.system("cls")
        print("2 - ")
        game = False
        key = ""

    if way_3 and key == "3":
        os.system("cls")
        print("дорога 3 ты увидел гору золота ")
        print("1 - забрать")
        print("2 - пройти мимо оставив золото")

        user_choice = input("введите номер ответа и нажмите ENTER ")
        if user_choice == 1 or user_choice == 2:
            key += user_choice
        if user_choice == "1" and way_1:
            key += user_choice
        if user_choice == "2" and way_2:
            key += user_choice

    if way_3 and key == "31":
        os.system("cls")
        print("1 - ты забрал золото но оно было проклято ты отравился и умер")
        way_3 = False
        key = ""

    if way_3 and key == "32":
        os.system("cls")
        print("2 - ты прошел мимо и дальше была еще гора нормального золота ты забрал его и стал богат")
        game = False
        key = ""

    if not(way_1 and way_2 and way_3):
        print("все дроги проехал молодец")
        game = False

print("конец")
