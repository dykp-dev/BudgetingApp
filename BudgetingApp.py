import time

total =  0.0
amount = ""
category = ""
income = ""
Media = 0
Food = 0
Transport = 0
Living = 0
new_income = 0
new_media = 0
new_food = 0
new_transport = 0
new_living = 0

def get_expense():
    return float(input("Enter how much your expense is this month "))

while True:
    amount = input("Please enter 1,2,3,4. 1 for income 2 for expenses 3 for Month summary and 4 to exit. ")
    if amount == "1":
        income = float(input("Please add an income "))
        total += income
        new_income += income
        print(total)
    elif amount == "2":
        expenses = ["Entertainment, Food, Transport, Living "]
        for expense in expenses:
            print(expense)
            category = input("What is your expense? ")
            if category == "Entertainment":
                amount = get_expense()
                Media += amount
                new_media = Media
                print(f'Your total expense on Entertainment is {Media}')
                if Media >= 0.3 * total :
                    print("Your expense on entertainment is quite high, spend less!")
                total -= amount
                print(f'Your new total is {total}')
                continue
            if category == "Food":
                amount = get_expense()
                Food += amount
                new_food += Food
                print(f'Your total expense on Food is {Food}')
                if Food >= 0.3 * total :
                    print("You expense on food is quite high, spend less!")
                total -= amount
                print(f'Your new total is {total}')
                continue
            if category == "Transport":
                amount = get_expense()
                Transport += amount
                new_transport += Transport
                print(f'Your total expense on Transport is {Transport}')
                if Transport >= 0.2 * total:
                    print("Your expense on transport is quite high, spend less!")
                total -= amount
                print(f'Your new total is {total}')
                continue
            if category == "Living":
                amount = get_expense()
                Living += amount
                new_living += amount
                print(f'Your total expense on Living is {Living}')
                if Living >= 0.5 * total :
                    print("Your expense on living is quite high, spend less!")
                total -= amount
                print(f'Your new total is {total}')
                continue
    elif amount == "3":
                print(f'''
                    This month summary:
                    Income: {new_income}
                    Breakdown: 
                    Food: {new_food}
                    Transport: {new_transport}
                    Entertainment: {new_media}
                    Living: {new_living}
                    
                    ''')
                continue
    elif amount == "4":
        print("Thank you for your time!")
        time.sleep(4)
        break
























