menu = {
    'pizza':50,
    'pasta':60,
    'burger':45,
    'salad':70,
    'soup':30,
    'dessert':55,
    'coffee':80,
    'tea':40,
    'juice':65,
    'water':20,
    'soda':45,
    
}
print("Welcome to Sunshine Cafe!")
print("Here is our menu:")
print("pizza: Rs50 \n pasta: Rs60\n burger:Rs45\n salad:Rs70\n soup:Rs30\n dessert:Rs55\n coffee:Rs80\n tea:Rs40\n juice:Rs65\n water:Rs20\n soda:Rs45")

order_total=0

item_1= input("Enter the first item you want to order: ")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"your item {item_1}has been added tp your order")
else:
    print(f"Sorry, we don't have {item_1} on the menu.")

another_order = input("Do you want to order another item? (yes/no): ")
if another_order== "Yes":
    item_2= input("Enter the next item you want to order: ")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"your item {item_2} has been added to your order")
    else:
        print(f"Sorry, we don't have {item_2}on the menu.")
print(f"Your total order amount is Rs{order_total}")
print("Thank you for dining with us!")
print("We hope to see you again soon!")
print("Have a great day!")

      