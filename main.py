DATA = """
100
200
300

400
250

100

600
700
900

300
"""

def find_value_of_largest_order():
    orders = DATA.split('\n')
    largest_Value_Order=0
    order_value=0 
    for item in orders:
        if item.strip():
            item_price=int(item)
            order_value +=item_price
        else:
            if order_value > largest_Value_Order:
                largest_Value_Order = order_value

            order_value=0
    return largest_Value_Order
if __name__ == "__main__":
    highest_order = find_value_of_largest_order()

    output = "The value of the largest order is: £" + str(highest_order)
    print(output)
