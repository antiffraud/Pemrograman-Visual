import sys
from PyQt6.QtWidgets import (QApplication, QDialog, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QRadioButton,
                             QComboBox, QFormLayout, QVBoxLayout, QMessageBox)
from PyQt6.QtCore import Qt

class RegistrationForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Week 2 : Layout - User Registration Form")

        self.createIdentitasGroupBox()
        self.createNavigationLayout()
        self.createUserRegistrationGroupBox()
        self.createActionsLayout()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.identitasGroupBox)
        mainLayout.addLayout(self.navigationLayout)
        mainLayout.addWidget(self.userRegistrationGroupBox)
        mainLayout.addLayout(self.actionsLayout)

        self.setLayout(mainLayout)

    def createIdentitasGroupBox(self):
        self.identitasGroupBox = QGroupBox("Identitas")

        namaLabel = QLabel("Nama:")
        self.namaLineEdit = QLineEdit()
        self.namaLineEdit.setPlaceholderText("Muhamad Erwin Hariadinata")
        self.namaLineEdit.setReadOnly(True)

        nimLabel = QLabel("NIM:")
        self.nimLineEdit = QLineEdit()
        self.nimLineEdit.setPlaceholderText("F1D022065")
        self.nimLineEdit.setReadOnly(True)

        kelasLabel = QLabel("Kelas:")
        self.kelasLineEdit = QLineEdit()
        self.kelasLineEdit.setPlaceholderText("C")
        self.kelasLineEdit.setReadOnly(True)

        formLayout = QFormLayout()
        formLayout.addRow(namaLabel, self.namaLineEdit)
        formLayout.addRow(nimLabel, self.nimLineEdit)
        formLayout.addRow(kelasLabel, self.kelasLineEdit)

        self.identitasGroupBox.setLayout(formLayout)

    def createNavigationLayout(self):
        self.navigationLayout = QHBoxLayout()
        self.homeButton = QPushButton("Home")
        self.aboutButton = QPushButton("About")
        self.contactButton = QPushButton("Contact")

        self.navigationLayout.addWidget(self.homeButton)
        self.navigationLayout.addWidget(self.aboutButton)
        self.navigationLayout.addWidget(self.contactButton)
        self.navigationLayout.addStretch()

    def createUserRegistrationGroupBox(self):
        self.userRegistrationGroupBox = QGroupBox("User Registration (form layout)")

        fullNameLabel = QLabel("Full Name:")
        self.fullNameLineEdit = QLineEdit()

        emailLabel = QLabel("Email:")
        self.emailLineEdit = QLineEdit()

        phoneLabel = QLabel("Phone:")
        self.phoneLineEdit = QLineEdit()

        genderLabel = QLabel("Gender:")
        self.maleRadioButton = QRadioButton("Male")
        self.femaleRadioButton = QRadioButton("Female")
        self.maleRadioButton.setChecked(True)

        genderLayout = QHBoxLayout()
        genderLayout.addWidget(self.maleRadioButton)
        genderLayout.addWidget(self.femaleRadioButton)

        countryLabel = QLabel("Country:")
        self.countryComboBox = QComboBox()
        self.countryComboBox.addItems(["Select country", "Indonesia", "America", "Japan", "Australia"])

        formLayout = QFormLayout()
        formLayout.addRow(fullNameLabel, self.fullNameLineEdit)
        formLayout.addRow(emailLabel, self.emailLineEdit)
        formLayout.addRow(phoneLabel, self.phoneLineEdit)
        formLayout.addRow(genderLabel, genderLayout)
        formLayout.addRow(countryLabel, self.countryComboBox)

        self.userRegistrationGroupBox.setLayout(formLayout)

    def createActionsLayout(self):
        self.actionsLayout = QHBoxLayout()
        self.submitButton = QPushButton("Submit")
        self.cancelButton = QPushButton("Cancel")

        self.submitButton.clicked.connect(self.onSubmit)
        self.cancelButton.clicked.connect(self.onCancel)

        self.actionsLayout.addWidget(self.submitButton)
        self.actionsLayout.addWidget(self.cancelButton)
        self.actionsLayout.addStretch()

    def onSubmit(self):
        QMessageBox.information(self, "Form Submitted", "Your form was submitted successfully!")

    def onCancel(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec())
