def show_item(game_item):
    for key, value in game_item.items():
        print( key, ":", value)



steel_gaunlet = {
    "NAME": "Steel gaunlet",
    "HP": 10,
    "STR": 100,
    "AGI": 5,
}
bronze_shield = {
    "NAME": "Bronze shield",
    "HP": 5,
    "AGI": 1,
    "STR": 100,
}
golden_stick = {
    "NAME": "Golden stick",
    "AGI":15,
    "HP":20,
    "STR": 100,
}

inventory = [steel_gaunlet, bronze_shield, golden_stick]
