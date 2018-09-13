from random import randint
steal_gaunlet={
    "NAME":"STEAL GAUNLET",
    "HP":10,
    "AGI":-5,
    "STA":-3,
    "LUCK":1,


}

bronze_shield = {
    "NAME":"BRONZE SHIELD",
    "HP":10,
    "AGI":-2,
}


golden_stick = {
    "NAME":"GOLDEN STICK",
    "AGI":15,
    "HP":20,
    "STR":100,

}
org = {"NAME":"Org guard",
        "STR": 1,
                       "DEF": 2,
                       "HP":69,
                       "LUCK":1,
                       "AGI":2,
       }

inventory=[]

def combat_round(attacker, defender):
    print(attacker["NAME"],"is beating",defender["NAME"])
    has_crit = calculate_crit(attacker)
    if has_crit:
        print("Chí mạng")
        damage = attacker["STR"]*2 - defender["DEF"]
    else:

        damage = attacker["STR"]  - defender["DEF"]

    if damage > 0:
        defender["HP"] -= damage
        print(defender["NAME"], "lost", abs(damage), "HP")

        print(defender["NAME"],"now has",defender["HP"],"HP")
    else:
        attacker["HP"] -= abs(damage)
        print(attacker["NAME"], "lost", damage, "HP")
        print(attacker["NAME"], "now has",attacker["HP"], "HP")

def combat_full(player,opponent):
    while True:
        auto_đánh = True
        combat_round(player, opponent)
        if opponent["HP"] <= 0 or player["HP"]<=0:

            break






        combat_round(opponent, player)
        if opponent["HP"] <= 0 or player["HP"] <= 0:

            break
        if  auto_đánh:
            print("Bạn muốn ?")
            print("1.Đánh tiếp")
            print("2.Chạy")
            print("3.Auto đánh")
            option = input("Your choice ?")
            if option == 1:
                pass
            elif option == 2:

                dice = randint(0, 100)
                if player["LUCK"] > dice:
                    print("Bạn đã chạy thoát")
                    break
                else:
                    print("Return")
            elif option == 3:
                auto_đánh = False



def calculate_crit(player)   :
    has_crit = False
    dice = randint(0,100)
    chance = player["LUCK"]+player["AGI"]
    if chance > dice:
        has_crit = True
    return has_crit