import datetime

products = {
    1: {"name": "Apple", "price": 1.00, "stock": 10},
    2: {"name": "Banana", "price": 0.50, "stock": 20},
    3: {"name": "Orange", "price": 0.75, "stock": 15}
}

orders = []

def main_menu():
    print("\n===== Grocery Store Management System =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Stock")
    print("4. Process Order")
    print("5. View Orders")
    print("6. Exit")
    return input("Enter your choice: ")

def add_product():
    print("\n===== Add Product =====")
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter product stock: "))
    product_id = len(products) + 1
    products[product_id] = {"name": name, "price": price, "stock": stock}
    print("Product added successfully!")

def view_products():
    print("\n===== View Products =====")
    print("ID  | Name\t| Price\t| Stock")
    print("-" * 35)
    for p_id, product in products.items():
        print(f"{p_id}   | {product['name']}\t| ${product['price']}\t| {product['stock']}")

def update_stock():
    print("\n===== Update Stock =====")
    view_products()
    p_id = int(input("Enter product ID to update stock: "))
    if p_id in products:
        new_stock = int(input("Enter new stock quantity: "))
        products[p_id]['stock'] = new_stock
        print("Stock updated successfully!")
    else:
        print("Product not found!")

def process_order():
    print("\n===== Process Order =====")
    view_products()
    p_id = int(input("Enter product ID to purchase: "))
    if p_id in products and products[p_id]['stock'] > 0:
        quantity = int(input("Enter quantity to purchase: "))
        if quantity <= products[p_id]['stock']:
            products[p_id]['stock'] -= quantity
            total_cost = products[p_id]['price'] * quantity
            orders.append({"id": len(orders)+1, "p_id": p_id, "quantity": quantity, "total_cost": total_cost, "timestamp": datetime.datetime.now()})
            print("Order placed successfully!")
        else:
            print("Not enough stock!")
    else:
        print("Product not found or out of stock!")

def view_orders():
    print("\n===== View Orders =====")
    if not orders:
        print("No orders yet.")
    else:
        print("ID  | Product\t| Quantity\t| Total Cost\t| Timestamp")
        print("-" * 65)
        for order in orders:
            product_name = products[order['p_id']]['name']
            print(f"{order['id']}   | {product_name}\t| {order['quantity']}\t\t| ${order['total_cost']}\t| {order['timestamp']}")

while True:
    choice = main_menu()

    if choice == '1':
        add_product()
    elif choice == '2':
        view_products()
    elif choice == '3':
        update_stock()
    elif choice == '4':
        process_order()
    elif choice == '5':
        view_orders()
    elif choice == '6':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")