# Import Package
from tabulate import tabulate # type: ignore
import datetime

# Variables Definitions
program_title = "iWareHouse - Apple Inventory Management System"
product_categories = ["iPhone", "Macbook", "iPad", "Apple Watch", "AirPods", "iPod"]
warehouse_items = [
    {
        "product_name": "iPhone 13",
        "category": "iPhone",
        "location": "Aisle 1, Shelf 1",
        "price": 699,
        "quantity": 0,
        "reorder_threshold": 30
    },
    {
        "product_name": "iPhone 14",
        "category": "iPhone",
        "location": "Aisle 1, Shelf 2",
        "price": 799,
        "quantity": 40,
        "reorder_threshold": 25
    },
    {
        "product_name": "iPhone 15",
        "category": "iPhone",
        "location": "Aisle 1, Shelf 3",
        "price": 899,
        "quantity": 20,
        "reorder_threshold": 30
    },
    {
        "product_name": "MacBook Air",
        "category": "Macbook",
        "location": "Aisle 2, Shelf 1",
        "price": 999,
        "quantity": 5,
        "reorder_threshold": 25
    },
    {
        "product_name": "MacBook Pro",
        "category": "Macbook",
        "location": "Aisle 2, Shelf 2",
        "price": 1299,
        "quantity": 15,
        "reorder_threshold": 20
    },
    {
        "product_name": "iPad Pro",
        "category": "iPad",
        "location": "Aisle 3, Shelf 1",
        "price": 1099,
        "quantity": 12,
        "reorder_threshold": 10
    },
    {
        "product_name": "Apple Watch Series 7",
        "category": "Apple Watch",
        "location": "Aisle 4, Shelf 1",
        "price": 399,
        "quantity": 0,
        "reorder_threshold": 15
    },
    {
        "product_name": "Apple Watch Series 8",
        "category": "Apple Watch",
        "location": "Aisle 4, Shelf 2",
        "price": 499,
        "quantity": 5,
        "reorder_threshold": 15
    },
    {
        "product_name": "AirPods Pro 2022",
        "category": "AirPods",
        "location": "Aisle 5, Shelf 1",
        "price": 249,
        "quantity": 50,
        "reorder_threshold": 30
    },
    {
        "product_name": "AirPods Pro 2023",
        "category": "AirPods",
        "location": "Aisle 5, Shelf 2",
        "price": 299,
        "quantity": 35,
        "reorder_threshold": 30
    },
    {
        "product_name": "iPod Classic",
        "category": "iPod",
        "location": "Aisle 6, Shelf 1",
        "price": 199,
        "quantity": 0,
        "reorder_threshold": 10
    },
    {
        "product_name": "iPod Nano",
        "category": "iPod",
        "location": "Aisle 6, Shelf 2",
        "price": 149,
        "quantity": 0,
        "reorder_threshold": 10
    },
    {
        "product_name": "iPod Shuffle",
        "category": "iPod",
        "location": "Aisle 6, Shelf 3",
        "price": 49,
        "quantity": 0,
        "reorder_threshold": 10
    }
]
order_shipping_record=[
    {
        'product_name':'iPhone 13',
        'quantity':25,
        'shipping_address':'iBox Pondok Indah Mall',
        'type':'shipment',
        'date':'2024-05-16'
    },
     {
        'product_name':'iPhone 14',
        'quantity':35,
        'shipping_address':'Manufacturer',
        'type':'reorder',
        'date':'2023-12-14'
    },
]

# Main Menu
def mainMenu():
    menu_options = [
        ["1", "Display product information"],
        ["2", "Add a new product or category"],
        ["3", "Update an existing product"],
        ["4", "Delete an existing product"],
        ["5", "Generate a report"],
        ["6", "Ship or Reorder Products"],
        ["7", "Exit Program"]
    ]

    print(f'\n{program_title}')
    print(tabulate(menu_options, headers=['Option', 'Menu'], tablefmt='double_grid', numalign='center'))
    
    chooseMenu = input("Choose an option (1 - 7): ")
    print()  # Enter a new line after every menu interaction
    
    return chooseMenu

# Read Products Menu
def display_product():
    while True:
        menu_options = [
            ["1", "Display All Products"],
            ["2", "Display Product by Product Name"],
            ["3", "Display Product by Category"],
            ["4", "Display Product by Price Range"],
            ["5", "Back To Main Menu"],
        ]

        print(tabulate(menu_options, headers=['Option', 'Display Product Sub-menu'], tablefmt='double_grid', numalign='center'))
        
        option = input("Choose an option (1-5): ")
        
        if option == '1':
            if check_empty_warehouse():
                continue
            display_all_products()
        elif option == '2':
            if check_empty_warehouse():
                continue
            
            product_name = input("\nEnter the product name: ")
            display_product_by_name(product_name)
        elif option == '3':
            if check_empty_warehouse():
                continue
            
            display_available_categories()
            chosen_category = input("\nEnter the category to display products: ")
            display_products_by_category(chosen_category)
        elif option == '4':
            if check_empty_warehouse():
                continue
            
            try:
                min_range = int(input("\nEnter the minimum price to display products: "))
                max_range = int(input("\nEnter the maximum price to display products: "))
                
                if min_range < 0 or max_range < 0:
                    print("\nInvalid input. Please enter positive numbers for the price range.\n")
                elif min_range > max_range:
                    print("\nInvalid input. The minimum price should be less than the maximum price.\n")
                else:
                    display_products_by_price_range(min_range, max_range)
            except ValueError:
                print("\nInvalid input. Please enter valid numbers for the price range.\n")
        elif option == '5':
            break
        else:
            print("\nInvalid option. Please choose a valid option between 1-3.\n")

def display_all_products():    
    print("\nDisplaying all products...")
    print(tabulate(warehouse_items, headers="keys", tablefmt="pretty"))
    print()

def display_product_by_name(product_name):
    product_exist = False
    for product in warehouse_items: # Check if product exists
        if product["product_name"].lower() == product_name.lower():
            print(f"\nDisplaying '{product_name}' information...")
            print(tabulate([product], headers="keys", tablefmt="pretty"))
            print()
            
            product_exist = True
            break
    if not product_exist:
        print(f"\nProduct '{product_name}' was not found.\n")

def display_products_by_category(chosen_category):
    products_found = False
    category_items = []
    for item in warehouse_items:
        if item['category'].lower() == chosen_category.lower():
            category_items.append(item)
            products_found = True
    
    if products_found:
        print(f"\nDisplaying products in category '{chosen_category}':")
        print(tabulate(category_items, headers="keys", tablefmt="pretty"))
        print()
    else:
        print(f"\nNo products found in category '{chosen_category}'.\n")
        
def display_products_by_price_range(min_range, max_range):
    products_in_range = []
    
    for item in warehouse_items:
        if min_range <= item['price'] <= max_range:
            products_in_range.append(item)
    
    if products_in_range:
        print(f"\nProducts in the price range of ${min_range} - ${max_range}:")
        print(tabulate(products_in_range, headers='keys', tablefmt='pretty'))
        print()
    else:
        print(f"\nNo products found in the price range of ${min_range} - ${max_range}.\n")

def check_empty_warehouse():
    if len(warehouse_items) <= 0:
        print("\nWarehouse is empty. Data does not exist.\n")
        return True
    return False

def display_available_categories():
    print('\n\t\t Available Categories')
    print(tabulate([product_categories], tablefmt="pretty"))

# Create Product Menu
def add_product():
    while True:
        menu_options = [
            ["1", "Add a New Product"],
            ["2", "Add a New Category"],
            ["3", "Back to Main Menu"]
        ]
        
        print(tabulate(menu_options, headers=['Option', 'Add New Product Sub-menu'], tablefmt='double_grid', numalign='center'))
        
        option = input("Choose an option (1-2): ")
        
        if option == '1':
            product_name = input_product_name()
            if product_name:
                category = input_product_category(product_name)
                location = input_product_location(product_name)
                price = input_product_price(product_name)
                quantity = input_product_quantity(product_name)
                reorder_threshold = input_product_reorder_threshold(product_name)

                add_new_product(product_name, category, location, price, quantity, reorder_threshold)
        
        elif option == '2':
            display_available_categories()
            add_new_category()
            
        elif option == '3':
            break
        else:
            print("\nInvalid option. Please choose a valid option between 1-3.\n")

def add_new_product(product_name, category, location, price, quantity, reorder_threshold):
    new_product = {
        "product_name": product_name,
        "category": category,
        "location": location,
        "price": price,
        "quantity": quantity,
        "reorder_threshold": reorder_threshold
    }
    
    print("\nNew product details:")
    print(tabulate([new_product], headers="keys", tablefmt="pretty"))
    
    while True: # User confirmation to save new product
        save_confirmation = input("\nDo you want to save this product? (y/n): ").lower()
        if save_confirmation == 'y':
            warehouse_items.append(new_product)  # Add new product to warehouse_items
            print("\nProduct added successfully!\n")
            break
        elif save_confirmation == 'n':
            print("\nProduct not saved.\n")
            break
        else:
            print("\nInvalid input. Please enter 'y' for yes or 'n' for no.")

def add_new_category():
    new_category = input("Enter the name of the new category: ")
    is_duplicate = False
    
    for category in product_categories:
        if category.lower() == new_category.lower():
            is_duplicate = True
            break
    
    if (new_category) and (not is_duplicate):
        product_categories.append(new_category)
        print(f"\nCategory '{new_category}' added successfully.\n")
    else:
        print("\nInvalid or duplicate category. Please enter a unique category name.\n")

def input_product_name():
    while True:
        product_name = input("\nEnter product name: ")
        product_exist = False
        
        for product in warehouse_items:
            if product["product_name"].lower() == product_name.lower():
                product_exist = True
                break
            
        if product_name == '':
            print(f"\nProduct name can't be empty. Please enter a different product name.\n")
            return False
        if product_exist:
            print(f"\nProduct '{product_name}' already exists. Please enter a different product name.\n")
            return False
        else:
            return product_name

def input_product_category(product_name):
    while True:
        display_available_categories()
        category_input = input(f"Enter a category for '{product_name}': ")
        category_found = False
        
        for val in product_categories:
            if val.lower() == category_input.lower():
                category = val  # Set the category value to the actual category from product_categories
                category_found = True
                break
        
        if category_found:
            return category
        else:
            print("\nInvalid category. Please enter one of the available categories.")

def input_product_location(product_name):
    while True:
        location = input(f"Enter location for '{product_name}' (ex -> Aisle 1, Shelf 3): ")
        
        if 'aisle' in location.lower() and ', ' in location.lower() and 'shelf' in location.lower():
            return location
        else:
            print("\nInvalid location format. Please enter a format like 'Aisle 1, Shelf 3'.\n")

def input_product_price(product_name):
    while True:
        try:
            price = int(input(f"Enter price for '{product_name}': "))
            if price > 0:
                return price
            else:
                print("\nInvalid input. Please enter a valid positive price (ex -> 199).\n")
        except:
            print("\nInvalid input. Please enter a valid positive price (ex -> 199).\n")

def input_product_quantity(product_name):
    while True:
        try:
            quantity = int(input(f"Enter quantity for '{product_name}': "))
            if quantity > 0:
                return quantity
            else:
                print("\nInvalid input. Please enter a valid positive quantity (ex -> 100).\n")
        except:
            print("\nInvalid input. Please enter a valid positive quantity (ex -> 100).\n")

def input_product_reorder_threshold(product_name):
    while True:
        try:
            reorder_threshold = int(input(f"Enter reorder threshold for '{product_name}': "))
            if reorder_threshold > 0:
                return reorder_threshold
            else:
                print("\nInvalid input. Please enter a valid positive reorder threshold (ex -> 25).\n")
        except:
            print("\nInvalid input. Please enter a valid positive reorder threshold (ex -> 25).\n")

# Update Product Menu
def update_product():
    while True:
        menu_options = [
            ["1", "Update a Product"],
            ["2", "Back to Main Menu"]
        ]

        print(tabulate(menu_options, headers=['Option', 'Update Product Sub-menu'], tablefmt='double_grid', numalign='center'))

        option = input("Choose an option (1-2): ")

        if option == '1':
            product_name = input("\nEnter the product name to update: ")
            product_exist = False
            product_to_update = None

            for product in warehouse_items:
                if product["product_name"].lower() == product_name.lower():
                    print(f"\nDisplaying '{product_name}' information...")
                    print(tabulate([product], headers="keys", tablefmt="pretty"))
                    print()

                    product_exist = True
                    product_to_update = product
                    break

            if not product_exist:
                print(f"\nProduct '{product_name}' was not found.\n")
                continue

            confirmation = input("Do you want to update this product? (y/n): ").lower()
            if confirmation != 'y':
                print("\nUpdate cancelled.\n")
                continue

            new_product_to_update = product_to_update.copy()  # A temporary variable that holds the product data to change, before the user accepted the update in the end

            update_options = [
                ["1", "Update Product Name"],
                ["2", "Update Category"],
                ["3", "Update Location"],
                ["4", "Update Price"],
                ["5", "Update Reorder Level"],
                ["6", "Save and Exit"]
            ]

            # Update product for each columns starts here
            while True:
                print()
                print(tabulate(update_options, headers=['Option', 'Update Options'], tablefmt='double_grid', numalign='center'))
                update_choice = input("Choose a column to update (1-6): ")

                if update_choice == '1':
                    update_product_name(new_product_to_update)

                elif update_choice == '2':
                    update_product_category(new_product_to_update)

                elif update_choice == '3':
                    update_product_location(new_product_to_update)

                elif update_choice == '4':
                    update_product_price(new_product_to_update)

                elif update_choice == '5':
                    update_product_reorder_threshold(new_product_to_update)

                elif update_choice == '6':
                    if not product_to_update == new_product_to_update:
                        print(f"\nCurrent '{product_to_update['product_name']}' information:")  # Print current vs new product information before saving
                        print(tabulate([product_to_update], headers="keys", tablefmt="pretty"))

                        print(f"\nNew '{product_to_update['product_name']}' information:")
                        print(tabulate([new_product_to_update], headers="keys", tablefmt="pretty"))

                        confirmation = input("\nDo you want to save the changes? (y/n): ").lower()
                        if confirmation == 'y':
                            product_to_update['product_name'] = new_product_to_update['product_name'] # Commit the changes / update for the product
                            product_to_update['category'] = new_product_to_update['category']
                            product_to_update['location'] = new_product_to_update['location']
                            product_to_update['price'] = new_product_to_update['price']
                            product_to_update['quantity'] = new_product_to_update['quantity']
                            product_to_update['reorder_threshold'] = new_product_to_update['reorder_threshold']
                            
                            print("\nProduct updated successfully.\n")
                        else:
                            print("\nUpdate cancelled. No changes were made.\n")
                        break
                    else:
                        print("\nNo changes were made to the product.\n")
                        break
                else:
                    print("\nInvalid option. Please choose a valid option between 1-6.")
                    
        elif option == '2':
            break
        else:
            print("\nInvalid option. Please choose a valid option between 1-2.\n")
            
def update_product_name(new_product_to_update):
    while True:
        new_product_name = input(f"\nEnter new product name [{new_product_to_update['product_name']}]: ")
        if not new_product_name:  # If the user didn't enter anything, it goes back to the column update menu
            break

        product_duplicate = False
        for product in warehouse_items:
            if product["product_name"].lower() == new_product_name.lower():
                product_duplicate = True
                break

        if product_duplicate:
            print(f"\nProduct name '{new_product_name}' already exists. Please enter a different product name.")
        else:
            new_product_to_update['product_name'] = new_product_name
            break

def update_product_category(new_product_to_update):
    while True:
        display_available_categories()
        
        new_category = input(f"\nEnter new category [{new_product_to_update['category']}]: ")
        if not new_category:
            break

        category_found = False
        for val in product_categories:
            if val.lower() == new_category.lower():
                new_product_to_update['category'] = val
                category_found = True
                break

        if category_found:
            break
        else:
            print("\nInvalid category. Please enter one of the available categories.")

def update_product_location(new_product_to_update):
    while True:
        new_location = input(f"\nEnter new location (ex -> Aisle 1, Shelf 3) [{new_product_to_update['location']}]: ")
        if not new_location:
            break

        if 'aisle' in new_location.lower() and ', ' in new_location.lower() and 'shelf' in new_location.lower():
            new_product_to_update['location'] = new_location
            break
        else:
            print("\nInvalid location format. Please enter a format like 'Aisle 1, Shelf 3'.")

def update_product_price(new_product_to_update):
    while True:
        try:
            new_price = int(input(f"\nEnter new price [{new_product_to_update['price']}]: "))

            if new_price > 0:
                new_product_to_update['price'] = new_price
                break
            else:
                print("\nInvalid input. Please enter a valid positive price (ex -> 199).")
        except ValueError:  # Only catch the Error that is from incorrect input.
            print("\nInvalid input. Please enter a valid positive price (ex -> 199).")

def update_product_reorder_threshold(new_product_to_update):
    while True:
        try:
            new_reorder_threshold = int(input(f"\nEnter new reorder threshold [{new_product_to_update['reorder_threshold']}]: "))

            if new_reorder_threshold > 0:
                new_product_to_update['reorder_threshold'] = new_reorder_threshold
                break
            else:
                print("\nInvalid input. Please enter a valid positive reorder threshold (ex -> 100).")
        except ValueError:
            print("\nInvalid input. Please enter a valid positive reorder threshold (ex -> 100).")

# Delete Product Menu
def delete_product():
    while True:
        menu_options = [
            ["1", "Delete a discontinued Product"],
            ["2", "Delete Products by Category"],
            ["3", "Back to Main Menu"]
        ]
        
        print(tabulate(menu_options, headers=['Option', 'Delete Product Sub-menu'], tablefmt='double_grid', numalign='center'))
        
        option = input("Choose an option (1-3): ")
        
        if option == '1':
            product_name = input("\nEnter the product name to delete: ")
            delete_product_by_name(product_name)
        elif option == '2':
            print("\nCurrent Product Categories:")
            display_available_categories()
            
            category_name = input("Enter the category name to delete: ")
            delete_products_by_category(category_name)
        elif option == '3':
            break
        else:
            print("\nInvalid option. Please choose a valid option between 1-3.\n")
            
def delete_product_by_name(product_name):
    product_exist = False
    product_to_delete = None
    
    for product in warehouse_items:
        if product["product_name"].lower() == product_name.lower():
            print(f"\nDisplaying '{product_name}' information...")
            print(tabulate([product], headers="keys", tablefmt="pretty"))
            print()
            
            product_exist = True
            product_to_delete = product
            break
    
    if not product_exist:
        print(f"\nProduct '{product_name}' was not found.\n")
        return
    
    delete_confirmation = input("Are you sure you want to delete this product? (y/n): ").lower()
    if delete_confirmation == 'y':
        warehouse_items.remove(product_to_delete)
        print("\nProduct deleted successfully.\n")
    else:
        print("\nDelete product cancelled.\n")
        
def delete_products_by_category(category_name):
    category_found = False
    for cat in product_categories:
        if cat.lower() == category_name.lower():
            category_found = True
            break
    
    if category_found:
        display_products_by_category(category_name)
        delete_confirmation = input(f"Are you sure you want to delete the category '{category_name}' and all its products? (y/n): ").lower()
        
        if delete_confirmation == 'y':
            products_to_remove = []
            for product in warehouse_items:
                if product["category"].lower() == category_name.lower():
                    products_to_remove.append(product)
            
            for product in products_to_remove:
                warehouse_items.remove(product)
            
            # Update the product_category after removing the category and all its items
            for cat in product_categories:
                if cat.lower() == category_name.lower():
                    product_categories.remove(cat)
                    break
            
            display_all_products()
            print(f"Category '{category_name}' and all its products has been deleted successfully.\n")
        else:
            print("\nDelete category cancelled.\n")
    else:
        print(f"\nCategory '{category_name}' does not exist.\n")

# Generate Report Menu
def generate_report():
    while True:
        menu_options = [
            ["1", "Low Stock Items"],  # Filter out items that have a lower quantity than its reorder threshold
            ["2", "Out of Stock Items"],  # Filter out items that have zero quantity
            ["3", "Total Inventory Value"],  # Take the sum of every item's quantity * its price
            ["4", "Back to Main Menu"]
        ]
        
        print(tabulate(menu_options, headers=['Option', 'Generate Report Sub-menu'], tablefmt='double_grid', numalign='center'))
        
        option = input("Choose an option (1-4): ")
        
        if option == '1':
            get_low_stock_items()
        
        elif option == '2':
            get_out_of_stock_items()
        
        elif option == '3':
            get_total_inventory_value()
        
        elif option == '4':
            break
        
        else:
            print("\nInvalid option. Please choose a valid option between 1-4.\n")

def get_low_stock_items():
    print("\nLow Stock Items (Below Reorder Threshold):")
    low_stock_items = []
    for item in warehouse_items:
        if (item['quantity'] < item['reorder_threshold'] and item['quantity'] > 0):
            low_stock_items.append(item)
            
    if low_stock_items:
        print(tabulate(low_stock_items, headers="keys", tablefmt="pretty"))
        print()
    else:
        print("All items are above the reorder threshold.\n")

def get_out_of_stock_items():
    print("\nOut of Stock Items:")
    out_of_stock_items = []
    for item in warehouse_items:
        if item['quantity'] == 0:
            out_of_stock_items.append(item)
                
    if out_of_stock_items:
        print(tabulate(out_of_stock_items, headers="keys", tablefmt="pretty"))
        print()
    else:
        print("No items are out of stock.\n")

def get_total_inventory_value():
    total_inventory_value = 0
    financial_report = []
    
    for item in warehouse_items:
        item_total_value = item['price'] * item['quantity']
        financial_report.append({
            'product_name': item['product_name'],
            'quantity': item['quantity'],
            'price': f"${item['price']}",
            'total_value': f"${item_total_value}"
        })
        total_inventory_value += item_total_value
    
    print("\nInventory Value Report:")
    print(tabulate(financial_report, headers='keys', tablefmt='pretty'))
    print(f"Total Inventory Value: ${total_inventory_value}\n")

# Reorder Stock Menu 
def ship_reorder_stock():
    while True:
        menu_options = [
            ["1", "View Shipments and Reorder Reports"],
            ["2", "Ship a product"],
            ["3", "Reorder All Items"],
            ["4", "Select an Item to Reorder"],
            ["5", "Back To Main Menu"]
        ]
        
        print(tabulate(menu_options, headers=['Option', 'Reorder Stock Sub-menu'], tablefmt='double_grid', numalign='center'))
        
        option = input("Choose an option (1-5): ")
        
        if option == '1':
            view_shipments_and_reorder_reports()
        elif option == '2':
            ship_product()
        elif option == '3':
            reorder_all_items()
        elif option == '4':
            reorder_selected_item()
        elif option == '5':
            break
        
        else:
            print("\nInvalid option. Please choose a valid option between 1-5.\n")

def view_shipments_and_reorder_reports():
    if not order_shipping_record:
        print("\nNo shipment or reorder records found.\n")
        return
    
    print("\nShipments and Reorder Reports:")
    print(tabulate(order_shipping_record, headers="keys", tablefmt="pretty"))
    print()

def ship_product():
    shipment_items = []
    for item in warehouse_items:
        if item['quantity'] > 0:
            shipment_items.append(item)
                    
    if not shipment_items:
        print("\nNo items need to be shipped.\n")
        return
    
    print("\nItems to Ship:")
    print(tabulate(shipment_items, headers='keys', tablefmt='pretty'))
    print()
    
    product_name = input("Enter product name to ship: ")
    product_found = False
    
    for product in warehouse_items:
        if product['product_name'].lower() == product_name.lower():
            while True:
                try:
                    quantity_to_ship = int(input("Enter quantity to ship: "))
                    if quantity_to_ship <= 0:
                        print("\nQuantity to ship must be a positive number. Please try again.\n")
                    elif quantity_to_ship > product['quantity']:
                        print(f"\nInsufficient stock to ship {quantity_to_ship} units of {product_name}. Available quantity: {product['quantity']}\n")
                    else:
                        break
                except ValueError:
                    print("\nInvalid input. Please enter a valid integer.\n")
            
            shipping_address = input("Enter shipping address: ")
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            
            product['quantity'] -= quantity_to_ship  # Update the product quantity
            
            order_shipping_record.append({ # Add a new record (dict) to list order_shipping_record
                'product_name': product_name,
                'quantity': quantity_to_ship,
                'shipping_address': shipping_address,
                'type': 'shipment',
                'date': current_date
            })
            
            print(f"\nShipped {quantity_to_ship} units of {product_name} to {shipping_address} on {current_date}.\n")
            product_found = True
            break
    
    if not product_found:
        print(f"\nProduct '{product_name}' not found.\n")

def reorder_all_items():
    reorder_items = []
    for item in warehouse_items:
        if item['quantity'] < item['reorder_threshold']:
            reorder_items.append(item)
                    
    if not reorder_items:
        print("\nNo items need to be reordered.\n")
        return
    
    print("\nItems to Reorder:")
    print(tabulate(reorder_items, headers='keys', tablefmt='pretty'))
    print()
    
    confirmation = input("Are you sure you want to reorder all items? (y/n): ").lower()
    if confirmation == 'y':
        for item in warehouse_items:
            if item['quantity'] < item['reorder_threshold']:
                reorder_amount = item['reorder_threshold'] - item['quantity']
                item['quantity'] += reorder_amount  # Update the quantity of all products to meet its threshold
                
                current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                order_shipping_record.append({ # Add a reorder record to list order_shipping_record
                'product_name': item['product_name'],
                'quantity': reorder_amount,
                'shipping_address': 'Manufacturer',
                'type': 'reorder',
                'date': current_date
                })
                
        print("\nAll items reordered successfully.\n")
        
        print("Updated Inventory:")
        print(tabulate(warehouse_items, headers='keys', tablefmt='pretty'))  # Display updated inventory
        print()
    else:
        print("\nReorder cancelled.\n")

def reorder_selected_item():
    reorder_items = []
    for item in warehouse_items:
        if item['quantity'] < item['reorder_threshold']:
            reorder_items.append(item)

    if not reorder_items:
        print("\nNo items need to be reordered.\n")
        return
    
    print("\nItems to Reorder:")
    print(tabulate(reorder_items, headers='keys', tablefmt='pretty'))
    
    selected_product_name = input("\nEnter the name of the product to reorder: ")
    
    found_item = None
    for item in reorder_items:
        if item['product_name'].lower() == selected_product_name.lower():
            found_item = item
            break
    
    if found_item:
        while True:
            try:
                reorder_amount = int(input(f"Enter quantity to reorder for '{found_item['product_name']}' (current stock: {found_item['quantity']}): "))
                
                if reorder_amount > 0:
                    confirmation = input(f"\nAre you sure you want to reorder {reorder_amount} units of '{found_item['product_name']}'? (y/n): ").lower()
                    if confirmation == 'y':
                        found_item = None
                        for item in warehouse_items:  # Get the actual item to update from warehouse_items
                            if item['product_name'].lower() == selected_product_name.lower():
                                found_item = item
                                break

                        if found_item:
                            found_item['quantity'] += reorder_amount
                            print(f"\n'{found_item['product_name']}' reordered successfully.\n")
                            
                            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                            order_shipping_record.append({  # Add a reorder record to list order_shipping_record
                                'product_name': found_item['product_name'],
                                'quantity': reorder_amount,
                                'shipping_address': 'Manufacturer',
                                'type': 'reorder',
                                'date': current_date
                            })
                            
                            print(f"Updated {found_item['product_name']} quantity:")
                            print(tabulate([found_item], headers='keys', tablefmt='pretty'))
                            print()
                        break
                    else:
                        print("\nReorder cancelled.\n")
                        break
                else:
                    print("\nInvalid input. Please enter a positive number.\n")
            except ValueError:
                print("\nInvalid input. Please enter a valid number.\n")
    else:
        print(f"\nProduct '{selected_product_name}' was not found or does not require a reorder.\n")

# Main Program
while True:
    chooseMenu=mainMenu()

    if(chooseMenu=='1'):
        display_product()
    elif(chooseMenu=='2'):
        add_product()
    elif(chooseMenu=='3'): 
        update_product()
    elif(chooseMenu=='4'): 
        delete_product()
    elif(chooseMenu=='5'): 
        generate_report()
    elif(chooseMenu=='6'): 
        ship_reorder_stock()
    elif(chooseMenu=='7'):
        confirmation = input('Are you sure you want to exit the program? (y/n): ').lower()
        if (confirmation == 'y'):
            print('\nExiting program...')
            print('Thank you!')
            break
        else:
            continue
    else:
        print('==================================')
        print('The menu you entered is not valid.')
        print('==================================')
        