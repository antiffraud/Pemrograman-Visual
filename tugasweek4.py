from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QComboBox, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QGridLayout
)
from PyQt6.QtCore import Qt

class POSApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("F1D022065 - Muhamad Erwin Hariadinata")
        self.cart = []
        self.total_price = 0
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.product_label = QLabel("Product")
        self.product_dropdown = QComboBox()
        self.products = {
            " ": 0,  
            "Bimoli (Rp. 20.000)": 20000,
            "Beras 5 Kg (Rp. 75.000)": 75000,
            "Kecap ABC (Rp. 7.000)": 7000,
            "Saos Saset (Rp. 2.500)": 2500
        }
        self.product_dropdown.addItems(self.products.keys())

        self.quantity_label = QLabel("Quantity")
        self.quantity_input = QLineEdit()
        self.quantity_input.setPlaceholderText("Enter quantity")

        self.discount_label = QLabel("Discount")
        self.discount_dropdown = QComboBox()
        self.discounts = {"0%": 0, "5%": 5, "10%": 10, "15%": 15}  
        self.discount_dropdown.addItems(self.discounts.keys())

        self.add_button = QPushButton("Add to Cart")
        self.add_button.clicked.connect(self.add_to_cart)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_selected_item)

        self.cart_display = QTextEdit()
        self.cart_display.setReadOnly(True)

        self.total_label = QLabel("Total: Rp. 0")

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.product_label, 0, 0)
        grid_layout.addWidget(self.product_dropdown, 0, 1)
        grid_layout.addWidget(self.quantity_label, 1, 0)
        grid_layout.addWidget(self.quantity_input, 1, 1)
        grid_layout.addWidget(self.discount_label, 2, 0)
        grid_layout.addWidget(self.discount_dropdown, 2, 1)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.clear_button)

        layout.addLayout(grid_layout)
        layout.addLayout(button_layout)
        layout.addWidget(self.cart_display)
        layout.addWidget(self.total_label)

        self.setLayout(layout)

    def add_to_cart(self):
        product = self.product_dropdown.currentText()
        price = self.products.get(product, 0)
        quantity_text = self.quantity_input.text()
        discount_text = self.discount_dropdown.currentText()

        if product == " " or not quantity_text.isdigit() or int(quantity_text) <= 0:
            self.total_label.setText("Invalid Input!")
            return

        quantity = int(quantity_text)
        discount = self.discounts[discount_text]

        subtotal = price * quantity
        discount_amount = subtotal * (discount / 100)
        final_price = subtotal - discount_amount

        cart_entry = f"{product} (Rp. {price}) - {quantity} x Rp. {subtotal} (disc {discount}%)"
        self.cart.append(cart_entry)

        self.total_price += final_price
        self.cart_display.setPlainText("\n".join(self.cart))
        self.total_label.setText(f"Total: Rp. {int(self.total_price)}")

        self.clear_form()

    def clear_selected_item(self):
        product = self.product_dropdown.currentText()

        new_cart = []
        item_removed = False
        for item in self.cart:
            if product in item and not item_removed:
                item_removed = True
                price_start = item.rfind("Rp. ") + 4
                price_end = item.rfind(" (disc")
                price_value = int(item[price_start:price_end].replace(",", ""))
                self.total_price -= price_value
            else:
                new_cart.append(item)

        self.cart = new_cart
        self.cart_display.setPlainText("\n".join(self.cart))

        if not self.cart:
            self.total_label.setText("Total: Rp. 0")
        else:
            self.total_label.setText(f"Total: Rp. {int(self.total_price)}")

    def clear_form(self):
        self.quantity_input.clear()
        self.discount_dropdown.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication([])
    window = POSApplication()
    window.show()
    app.exec()
