print("===== You are welcome =====")

customer = input("Enter customer name: ")
product = input("Enter product name: ")
price = float(input("Enter price per unit (tenge): "))
quantity = int(input("Enter quantity: "))

subtotal = price * quantity
discount = subtotal * 0.1 if subtotal > 5000 else 0
total = subtotal - discount

print("=" * 33)
print("SHOP RECEIPT")
print("=" * 33)
print("Customer :", customer)
print("Product :", product)
print("Price :", price, "tenge")
print("Quantity :", quantity)
print("-" * 33)
print("Subtotal :", subtotal, "tenge")
print("Discount :", discount, "tenge")
print("Total :", total, "tenge")
print("=" * 33)

print("Discount applied:", subtotal > 5000)
print("Paid more than 3000:", total > 3000)
