power = True
resources = {
    "Water": 1000,
    "Milk": 500,
    "Coffee": 500,
    "Money": 0,
}

espresso = {
    "Name": "espresso",
    "Water": 100,
    "Milk": 50,
    "Coffee": 50,
    "Money": 1,
}

cappuccino = {
    "Name": "cappuccino",
    "Water": 150,
    "Milk": 100,
    "Coffee": 30,
    "Money": 1.5,
}

latte = {
    "Name": "latte",
    "Water": 150,
    "Milk": 100,
    "Coffee": 40,
    "Money": 2,
}

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}


def check_resources(drink):
    if resources["Water"] < drink["Water"]:
        print("Sorry there is not enough water.")
    if resources["Milk"] < drink["Milk"]:
        print("Sorry there is not enough milk.")
    if resources["Coffee"] < drink["Coffee"]:
        print("Sorry there is not enough coffee.")


def update_resources(drink):
    resources["Water"] -= drink["Water"]
    resources["Milk"] -= drink["Milk"]
    resources["Coffee"] -= drink["Coffee"]
    resources["Money"] += drink["Money"]


def total_money():
    print("Please insert coins.\U0001F4B2")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    return 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies


def select_drink(drink):
    check_resources(drink)
    update_resources(drink)
    print(f"price for {drink['Name']} is: {drink['Money']}")
    money = total_money()
    if money < drink['Money']:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Here is {(money - drink['Money']):.2f}$ in change.")
        print(f"Here is your {drink['Name']}. Enjoy!")


while power:
    user_select = input("What would you like? (espresso/latte/cappuccino): ")
    if user_select == "off":
        power = False
    if user_select == "report":
        print(f'Water: {resources["Water"]}ml \n'
              f'Milk: {resources["Milk"]}ml \n'
              f'Coffee: {resources["Coffee"]}g \n'
              f'Money: {resources["Money"]}$ \n')
    if user_select == "espresso":
        select_drink(espresso)
    if user_select == "latte":
        select_drink(latte)
    if user_select == "cappuccino":
        select_drink(cappuccino)
