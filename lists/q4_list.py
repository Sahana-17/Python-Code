def fillShoppingList(shopping_list):
    item_list = []

    item = str(input("Enter the item : "))
    quantity = int(input("Enter the quantity : "))
    price = float(input("Enter the price : "))

    total_price = quantity * price

    item_list.append(item)
    item_list.append(quantity)
    item_list.append(price)
    item_list.append(total_price)

    print(item_list)

    shopping_list.append(item_list)

def computeTotalBill(shopping_list):
    TotalBill = 0
    for i in range(0,3):
        item_list = shopping_list[i]
        TotalBill = TotalBill + item_list[3]

    return TotalBill

    



def main():
    list = []
    for i in range(1,4):
        fillShoppingList(list)
    print(list)

    grandtotal = computeTotalBill(list)
    print("Grand Total : ", grandtotal)
main()
