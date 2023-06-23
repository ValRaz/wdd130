import csv
import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    products_dict = {}

    try:
        with open(filename, "rt") as products_file:
            reader = csv.reader(products_file)
            next(reader)

            for product in reader:
                product_key = product[key_column_index]
                product_info = product[:key_column_index] + product[key_column_index + 1:]
                products_dict[product_key] = product_info

    except FileNotFoundError:
        print(f'Error: {filename} not found. Please enter a valid file name.\n')
    except PermissionError:
        print(f'Error: Permission denied to acces {filename}. Please use a file that you have permission to access.\n')
    
    return products_dict

def check_discount_day():
    today = datetime.datetime.now().weekday()
    return today == 1 or today == 2

def check_discount_time():
    current_time = datetime.datetime.now().time()
    return current_time < datetime.time(11, 0)

def apply_discount(product_price):
    if check_discount_day() or check_discount_time():
        return product_price * 0.9
    return product_price

def print_coupon(products_dict):
    product_keys = list(products_dict.keys())
    if len(product_keys) > 0:
        coupon_product = product_keys[0]
        discount_amount = 0.15  # 15% discount
        product_name = products_dict[coupon_product][0]
        product_price = float(products_dict[coupon_product][1])
        coupon_discount = discount_amount * product_price
        print(f'You\'ve earned 15% off your next purchase of {product_name}.')
        print(f'That\'s a savings of ${coupon_discount:.2f}!')
    else:
        print("No coupon earned today.")
 
def main():
    """Calls the read_dictionary function and stores the compound dictionary in a variable named products_dict.
    Prints the products_dict.
    Opens the request.csv file for reading.
    Skips the first line of the request.csv file because the first line contains column headings.
    Uses a loop that reads and processes each row from the request.csv file. Within the body of the loop, your program must do the following for each row:
    Use the requested product number to find the corresponding item in the products_dict.
    Print the product name, requested quantity, and product price."""

    PRODUCT_NUM_INDEX = 0
    QUANTITY_INDEX = 1


    products_dict = read_dictionary('products.csv', 0)

    itemized_order = []
    total_items_ordered = 0
    subtotal = 0

    print(f'\nBroulim\'s Grocery Store')

    try:
        with open('request.csv', 'rt') as request_file:
            reader = csv.reader(request_file)
            next(reader)

            for request in reader:
                product_number = request[PRODUCT_NUM_INDEX]
                quantity = int(request[QUANTITY_INDEX])

                if product_number in products_dict:
                    product_name = products_dict[product_number][0]
                    product_price = float(products_dict[product_number][1])
                    product_price = apply_discount(product_price)
                    item_total = product_price * quantity
                    itemized_order.append(f'{product_name}: {quantity}@ {product_price}')
                    subtotal += item_total
                    total_items_ordered += quantity
                    print(f'\nProduct: {product_name}\nQuantity: {quantity}\nPrice: {product_price}\n')

    except FileNotFoundError:
        print(f'Error: request.csv not found. Please enter a valid file name.\n')
    except PermissionError:
        print(f'Error: Permission denied to access request.csv. Please use a file you have permission to access.\n')

    for item in itemized_order:
        print(item)
    
    print(f'\nTotal Items Ordered: {total_items_ordered}\n\nSubtotal: ${subtotal:.2f}\n')

    sales_tax_rate = 0.06
    sales_tax_amount = subtotal * sales_tax_rate
    total_amount_due = subtotal + sales_tax_amount
    checkout_date_time = datetime.datetime.now()
    checkout_day = checkout_date_time.strftime('%A')
    checkout_date = checkout_date_time.strftime('%d')
    checkout_month = checkout_date_time.strftime('%B')
    print(f'Sales Tax: ${sales_tax_amount:.2f}\n\nTotal: ${total_amount_due:.2f}\n\nThank you for shopping at Broulim\'s!\n')
    print(f'Order Completed: {checkout_day}, {checkout_month} {checkout_date}')
    print(f'{checkout_date_time}\n')

    print_coupon(products_dict)
    print(f"\nPlease help us continue to provide a great experience by completing our online survey!")

if __name__ == "__main__":
    main()