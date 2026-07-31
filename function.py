def greet_customer():
    print("Welcome to the Lemonade Stand!")
    print("Fresh lemonade, made just for you")

greet_customer()


price_per_cup = float(input("Enter the price per cup"))
cups_sold = int(input("Enter the number of cups you sold"))

def calculate_total(price, cups):
    total = price * cups
    return total
A = calculate_total(price_per_cup,cups_sold)
B = round(A,2)
print(B)  