player = {
    "NAME": "Player",
    "HP": 200,
    "ATK": 50,
    "SPD": 20,
    "DEF": 100,
}

S_Beast = {
    "NAME": "Small Beast",
    "HP": 150,
    "ATK": 20,
    "SPD": 30,
    "DEF": 30,
}

B_Beast = {
    "NAME": "Big Beast",
    "HP": 300,
    "ATK": 40,
    "SPD": 10,
    "DEF": 150,
}

def combat(attacker, defender):
    print(attacker["NAME"], "still fight", defender["NAME"])
    damage = attacker["ATK"] - defender["DEF"]
    if damage > 0:
        defender["HP"] -= damage
        print(defender["NAME"], "lost", damage, "HP")
    else:
        attacker["HP"] = abs(damage)
        print(attacker["NAME"], "lost", damage, "HP")

print("bạn đang ở trong chiến trường")
print("bạn có 2 lựa chọn: ")
print("1.Attack")
print("2.Fall Back")
cmd = ("lựa chọn của bạn: ")
if cmd == "1":
    print("có hai con đường: ")
    print("1.con đường đất vào rùng")
    print("2.con đường nhựa vào thành phố kế bên")
    cmd = input("bạn sẽ đi con đường nào")
    if cmd == "1":
        print("bạn gặp 1 con Beast")
        print("Quick!!! you must: ")
        print("1.Fight")
        print("2.run away")
        cmd == input("bạn sẽ chọn gì?")
        if cmd == "1":
            while True:
                combat(player,s_orc)
                if player["HP"] <= 0 or s_orc["HP"] <= 0:
                    break
                combat(s_orc,player)
                if player["HP"] <= 0 or s_orc["HP"] <= 0:
                    break
            if player["HP"] >= 0:
                print("the beast has been defeated")
                print("sau khi đánh nhau với Beast")
                print("thì bạn tình cờ gặp ngôi nhà nhỏ")
                print("bạn có 2 lựa chọn")
                print("1.chạy đến đó")
                print("2.bỏ qua")
                cmd = input("bạn sẽ làm gì? ")
                if cmd == "1":
                    print("bạn gặp 1 con big beast đánh lừa")
                    print("nó chạy đến đánh bạn")
                    print("bạn có 2 lựa chọn")
                    print("1.đánh nó nếu đủ sức")
                    print("2.chạy và tìm con đường khác")
                    cmd = input("bạn sẽ làm gì? ")
                    if cmd == 1:
                        while True:
                            combat(l_orc,player)
                            if player["HP"] <= 0 or l_orc["HP"] <= 0:
                                break
                            combat(player,l_orc)
                            if player["HP"] <= 0 or l_orc["HP"] <= 0:
                                break
                        if player["HP"] >= 0:
                            print("bạn đã hoàn thành thử thách và chiến thắng.")
                            print("hết game")
                        elif player["HP"] <= 0:
                            print("bạn đã chết")
                            print("no way to retune the game")
                            print("thank for playing")
                            print("produce by gamemaker JuryBongo")
                    elif cmd == "2":
                        print("bạn dần kiệt sức và chạy chậm lại")
                        print("con orc bắt đc bạn và bạn chết")
            elif player["HP"] <= 0:
                print("bạn đã thua")
                print("no way to retune the game")
                print("thank for playing")
                print("produce by gamemaker JuryBongo")
    elif cmd == "2":
        print("bạn gặp nhiều đám orc nhỏ")
        print("bạn sẽ làm gì")
        print("1.bỏ đi")
        print("2.đánh nhau")
        cmd = input("bạn sẽ làm gì? ")
        if cmd == "1":
            print("vì bạn bỏ đi")
            print("and you are have a new aventures")
            print("comming soon")
        elif cmd == "2":
            print("băng cướp rất đông")
            print("sát thương của bạn yếu")
            print("bạn bị chúng đánh chết")
            print("you lose")

elif cmd == "2":
    print("quân đội của bạn chết dần nên bạn bị thua")
    print("you lose")
    print("thank for playing")
    print("produce by gamemaker JuryBongo")