import os
way_1 = True
way_2 = True
way_3 = True
game = True
# todo: выбрать перса
#

while game == True:

    os.system("cls")
    if way_1 == True or way_2 == True or way_3 == True:
        print("Подъезжает Илья к трем дорожкам, на перекрестке камень лежит, а на том камне написано: «Кто вправо поедет - тому убитым быть, кто влево поедет - тому богатым быть, а кто прямо поедет - тому женатым быть».")
        print("Поеду-ка я по той дорожке, где убитому быть. Умру в чистом поле, как славный богатырь!")
        print("Ну, поеду теперь, где женатому быть!")
        print("Ну, поеду теперь в дорожку, где богатому быть")
        user_choise = 0
        while user_choise != 1 and user_choise != 2 and user_choise != 3:
            user_choise = int(input("введите номер решения"))
        if user_choise == 1:
            print("Только он отъехал три версты, напали на него сорок разбойников. Хотят его с коня стащить, хотят его ограбить, до смерти убить")
            print("1-Эй вы, разбойнички, вам убить меня не за что и ограбить у меня нечего. Только и есть у меня кунья шубка в пятьсот рублей, соболиная шапка в три сотенки, да узда в пятьсот рублей, да седло черкасское в две тысячи. Ну, еще попона семи шелков, шита золотом да крупным жемчугом. Да меж ушами у Бурушки камень самоцвет. Он в осенние ночи как солнце горит, за три версты от него светло. Да еще, пожалуй, есть конь Бурушка - так ему во всем мире цены нет. Из-за этакой малости стоит ли старому голову рубить?!")
            print("2-")

            while user_choise != 1 and user_choise != 2 and user_choise != 3:
             user_choise = int(input("введите номер решения"))

        elif user_choise == 2:
            print("Как проехал Илья три версты, выехал на лесную поляну. Там стоят терема златоверхие, широко рас крыты ворота серебряные, на воротах петухи поют. Въехал Илья на широкий двор, выбежали к нему на встречу двенадцать девушек, среди них королевна-красавица.")
            print("Взяла его королевична за руку, повела в терем, посадила за дубовый стол. Принесли Илье меду слад кого, вина заморского, жареных лебедушек, калачей крупитчатых... Напоила-накормила богатыря, стала его уговаривать")
        elif user_choise == 3:
            print("Ну, поеду теперь в дорожку, где богатому быть. Только отъехал он три версты, увидал большой камень в триста пудов.")

    way = int(input("введите номер решения"))

    else:
        print("все дороги пройдены")

        input("нажмите энтер для продолжения")
