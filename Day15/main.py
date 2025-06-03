from data import MENU, resources

waterAmount = resources["water"]
milkAmount = resources["milk"]
coffeeAmount = resources["coffee"]
mybalance = 0

def reports():
    """Print current resource levels and money balance"""
    print(f"Water: {waterAmount}ml\nMilk: {milkAmount}ml\nCoffee: {coffeeAmount}g\nMoney: ${mybalance:.2f}")

def check_resources(water, milk, coffee):
    """Check if sufficient resources are available"""
    if waterAmount < water:
        return "Sorry there is not enough water."
    if milkAmount < milk:
        return "Sorry there is not enough milk."
    if coffeeAmount < coffee:
        return "Sorry there is not enough coffee."
    return True

def process_coins():
    """Calculate total value of coins inserted"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    return (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)


while True:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    
    if choice == 'off':
        break
        
    if choice == 'report':
        reports()
        continue
        
    if choice not in MENU:
        print("Invalid selection. Please choose from espresso, latte, or cappuccino.")
        continue
        
    drink = MENU[choice]
    cost = drink["cost"]
    ingredients = drink["ingredients"]
    
    
    water_needed = ingredients["water"]
    milk_needed = ingredients.get("milk", 0)
    coffee_needed = ingredients["coffee"]
    
    
    resource_check = check_resources(water_needed, milk_needed, coffee_needed)
    if resource_check != True:
        print(resource_check)
        continue
        
    
    payment = process_coins()
    
    if payment < cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        waterAmount -= water_needed
        milkAmount -= milk_needed
        coffeeAmount -= coffee_needed
        mybalance += cost
        
        
        if payment > cost:
            change = payment - cost
            print(f"Here is ${change:.2f} in change.")
        
        print(f"Here is your {choice} ☕. Enjoy!")