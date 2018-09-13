from combat import combat_round, combat_full
from inventory import *

player = {
    "NAME":"Thằng rank thấp",
    "CLASS":"Gamer",
    "HP": 60,
    "STR": 7,
    "DEF": 10,
    "LVL": 1,
    "Luck": 50,
    "AGI": 2,
}

cmd = input("Your command?")
if cmd == "stats":
    print("NAME:", player["NAME"])
    print("CLASS:", player["CLASS"])
    print("HP:", player["HP"])
    print("STRENGHT:", player["STR"])
    print("DEFENSE:", player["DEF"])
    print("LEVEL:", player["LVL"])
    print("LUCK:", player["Luck"])
    print("AGI:", player["AGI"])
elif cmd == "here":
    print("Bạn đang ở trước cửa Game")
    print("Bạn có 2 lựa chọn")
    print("1. không chơi nũa")
    print("2. chơi luôn")
    option = input("Lựa chọn của bạn?")
    if option == "1":
        print("Gà quá bạn ơi")
        print("Nhập lại đê!!")
    elif option == "2":
        print("Bạn đã vào chơi")
        print("Bạn thấy một bình EXP để lên cấp ở trên mặt đất")
        print("1. Bỏ qua")
        print("2. Nhặt lên uống")
        option = input("Lựa chọn của bạn?")
        if option == "1":
            print("Tiếc quá")
        elif option == "2":
            player["HP"] = 100
            print ("Bạn đã hồi phục hoàn toàn HP")
            print("NAME:", player["NAME"])
            print("CLASS:", player["CLASS"])
            print("HP:", player["HP"])
            print("STRENGHT:", player["STR"])
            print("DEFENSE:", player["DEF"])
            print("LEVEL:", player["LVL"])
            print("LUCK:", player["Luck"])
            print("AGI:", player["AGI"])
        print("bạn muốn chơi lên rank cao")
        print("Bạn gặp 1 con Orc chưa trưởng thành")
        print("Bạn sẽ:")
        print("1. Chạy trốn")
        print("2. Nấp vào hang đá bên cạnh")
        print("3. Chơi luôn sợ gì!!!")
        option = input("lựa chọn của bạn?")
        if option == "1":
            print("Do bạn chạy quá chậm bạn bị bắt đi")
        elif option == "2":
            print("Orc không nhìn thấy bạn và bỏ đi")
            print("Tuy nhiên bạn ức chế vì game ném ra ngoài cửa sổ")

        elif option == "3":
            Orc ={
                "NAME":" Orc",
                "HP": 7,
                "STR": 11,
                "DEF": 2,
                "Luck": 5,
                "AGI": 2

            }
            print("OPPONENT:", Orc["NAME"])
            print("HP:", Orc["HP"])
            print("STENGHT:", Orc["STR"])
            print("DEFENSE:", Orc["DEF"])
            print("LUCK:", Orc["Luck"])
            print("AGI:", Orc["AGI"])

            combat_full(player, Orc)
            show_item(inventory)
            













    else:
        print("Bạn sẽ không được chơi!!!")

else:
    print("Bạn đã chết")