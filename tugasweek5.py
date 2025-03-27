from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QComboBox, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QGridLayout, QMessageBox
)
from PyQt6.QtCore import Qt
import re

class FormValidation(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("F1D022065 - Muhamad Erwin Hariadinata")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()

        self.age_label = QLabel("Age:")
        self.age_input = QLineEdit()

        self.phone_label = QLabel("Phone Number:")
        self.phone_input = QLineEdit()

        self.address_label = QLabel("Address:")
        self.address_input = QTextEdit()

        self.gender_label = QLabel("Gender:")
        self.gender_dropdown = QComboBox()
        self.gender_dropdown.addItem("")  
        self.gender_dropdown.addItems(["Male", "Female"])

        self.education_label = QLabel("Education:")
        self.education_dropdown = QComboBox()
        self.education_dropdown.addItem("")  
        self.education_dropdown.addItems([
            "Elementary School", "Junior High School", "Senior High School",
            "Diploma", "Bachelor's Degree", "Master's Degree", "Doctoral Degree"
        ])

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.validate_form)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_field)

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.name_label, 0, 0)
        grid_layout.addWidget(self.name_input, 0, 1)
        grid_layout.addWidget(self.email_label, 1, 0)
        grid_layout.addWidget(self.email_input, 1, 1)
        grid_layout.addWidget(self.age_label, 2, 0)
        grid_layout.addWidget(self.age_input, 2, 1)
        grid_layout.addWidget(self.phone_label, 3, 0)
        grid_layout.addWidget(self.phone_input, 3, 1)
        grid_layout.addWidget(self.address_label, 4, 0)
        grid_layout.addWidget(self.address_input, 4, 1)
        grid_layout.addWidget(self.gender_label, 5, 0)
        grid_layout.addWidget(self.gender_dropdown, 5, 1)
        grid_layout.addWidget(self.education_label, 6, 0)
        grid_layout.addWidget(self.education_dropdown, 6, 1)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.clear_button)

        layout.addLayout(grid_layout)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def validate_form(self):
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        age = self.age_input.text().strip()
        phone = self.phone_input.text().strip()
        address = self.address_input.toPlainText().strip()
        gender = self.gender_dropdown.currentText().strip()
        education = self.education_dropdown.currentText().strip()

        if not name or not email or not age or not phone or not address or not gender or not education:
            QMessageBox.warning(self, "Validation Error", "All fields are required!")
            return

        if not re.match(r"^[A-Za-z\s]+$", name):
            QMessageBox.warning(self, "Validation Error", "Name shouldn't contain number")
            return

        if "@" not in email or ".com" not in email:
            QMessageBox.warning(self, "Validation Error", "Please enter a valid email address")
            return

        if not age.isdigit():
            QMessageBox.warning(self, "Validation Error", "Please enter a valid age (integer value)")
            return

        phone_cleaned = phone.replace(" ", "") 
        phone_pattern = r"^\+\d{12,}$"  

        if not re.match(phone_pattern, phone_cleaned):
            QMessageBox.warning(self, "Validation Error", "Please enter a valid digits phone number")
            return

        QMessageBox.information(self, "Success", "Profile Saved Successfully!")
        self.clear_all()

    def clear_field(self):
        focused_widget = QApplication.focusWidget()
        if isinstance(focused_widget, QLineEdit) or isinstance(focused_widget, QTextEdit) or isinstance(focused_widget, QComboBox):
            focused_widget.clear()
        else:
            self.clear_all()

    def clear_all(self):
        self.name_input.clear()
        self.email_input.clear()
        self.age_input.clear()
        self.phone_input.clear()
        self.address_input.clear()
        self.gender_dropdown.setCurrentIndex(0)
        self.education_dropdown.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication([])
    window = FormValidation()
    window.show()
    app.exec()
