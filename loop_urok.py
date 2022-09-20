#ставка до броска
#ставки >0
#<=деньги
#ставка== казино

import  random

user_money = 10
casino_money = 10

while user_money and casino_money:
    print("у игрока", user_money,"монет")
    print("у казино", casino_money,"монет")
    input("нажмите энтер чтобы сделать ход")

    user_turn = random.randint(1, 6)
    casino_turn = random.randint(1, 6)
    print("игрок выбросил", user_turn)
    print("казино выбросило", casino_turn)

    if user_turn > casino_turn:
        print("игрок победил")
        user_money += 1
        casino_money -= 1
    elif user_turn < casino_turn:
        print("казино победило")
        casino_money += 1
        user_money -= 1
    else:
        print("ничья")

if user_money:
    print("казино победило ")
else casino_money:
    print("игрок победил ")
