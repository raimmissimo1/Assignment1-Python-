store_info = ("Small", "Astana, Al-Farabi 16", "+7-705-689-5765")

print("=" * 33)
print(f" ----- {store_info[0]} ----- ")
print(store_info[1])
print(store_info[2])
print("=" * 33)

names = []
prices = []

while True:
    name = input("Enter product name (or 'done' to finish): ")
    if name == "done":
        break

    price = int(input("Enter price: "))
    names.append(name)
    prices.append(price)

print("-" * 30)
print(f"Your cart ({len(names)} items):")
print("-" * 30)

for i in range(len(names)):
    print(f"{names[i]} - {prices[i]} KZT")

print("-" * 30)

weekly_products = set()

while True:
    product = input("Enter product name (or 'done' to finish): ")
    if product == "done":
        break

    weekly_products.add(product)

print(f"Unique products: {len(weekly_products)}")
print(weekly_products)

customer_name = input("Enter customer name: ")

subtotal = sum(prices)

if subtotal < 3000:
    discount = 0
    discount_text = "No discount"
elif subtotal < 7000:
    discount = subtotal * 0.05
    discount_text = "Standard discount"
else:
    discount = subtotal * 0.15
    discount_text = "Premium discount"

receipt = {
    "customer": customer_name,
    "items": len(names),
    "subtotal": subtotal,
    "discount": discount,
    "total": subtotal - discount
}

print("=" * 30)
print(f"RECEIPT - {store_info[0]}")
print("=" * 30)
print(f"Customer : {receipt['customer']}")
print(f"Items : {receipt['items']}")
print("-" * 30)

for i in range(len(names)):
    print(f"{names[i]} - {prices[i]} KZT")

print("-" * 30)
print(f"Subtotal : {receipt['subtotal']} KZT")
print(f"Discount : {receipt['discount']} KZT ({discount_text})")
print(f"Total : {receipt['total']} KZT")
print("=" * 30)
