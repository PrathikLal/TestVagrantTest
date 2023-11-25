# Name: Prathik Lal Naik
# College:BMSIT
# Passing year:2024
# Phone Number:7892884658
# Email:prathiklal@gmail.com



class Product:
    def __init__(self, product_name, unit_cost, gst_percentage, quantity):
        self.product_name = product_name
        self.unit_cost = unit_cost
        self.gst_percentage = gst_percentage
        self.quantity = quantity

    def get_product_name(self):
        return self.product_name

    def calculate_total_cost(self):
        return self.unit_cost * self.quantity * (1 + self.gst_percentage / 100)

    def calculate_gst_amount(self):
        return self.unit_cost * self.quantity * (self.gst_percentage / 100)

    def calculate_discounted_total_cost(self):
        return self.calculate_total_cost() * 0.95 if self.unit_cost >= 500 else self.calculate_total_cost()


def find_product_with_max_gst(product_list):
    max_gst_product = product_list[0]
    max_gst_amount = max_gst_product.calculate_gst_amount()

    for product in product_list[1:]:
        current_gst_amount = product.calculate_gst_amount()
        if current_gst_amount > max_gst_amount:
            max_gst_product = product
            max_gst_amount = current_gst_amount

    return max_gst_product


def main():
    products = [
        Product("Leather Wallet", 1100, 18, 1),
        Product("Umbrella", 900, 12, 4),
        Product("Cigarette", 200, 28, 3),
        Product("Honey", 100, 0, 2)
    ]

    max_gst_product = find_product_with_max_gst(products)

    total_amount_to_pay = sum(product.calculate_discounted_total_cost() for product in products)

    print(f"Product with maximum GST amount: {max_gst_product.get_product_name()}")
    print(f"Total amount to be paid: Rs. {total_amount_to_pay}")


if __name__ == "__main__":
    main()
