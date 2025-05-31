import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLineEdit, QComboBox,
    QSpinBox, QGridLayout, QInputDialog
)
from PyQt6.QtCore import Qt

class ClickableLineEdit(QLineEdit):
    def __init__(self, text, slot):
        super().__init__(text)
        self.setReadOnly(True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        # visually identical to normal inputs
        self.slot = slot

    def mousePressEvent(self, event):
        self.slot()
        # optional: select all after dialog if you want
        super().mousePressEvent(event)


class InteractiveInputDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Dialog demo")
        self.resize(400, 160)

        layout = QGridLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # left  = clickable read‑only QLineEdit
        # right = actual input widget

        # Row 1: language
        self.left_lang = ClickableLineEdit("Choose from list", self.open_language_dialog)
        self.right_lang = QComboBox()
        self.right_lang.addItems(["C", "Java", "Python"])
        layout.addWidget(self.left_lang, 0, 0)
        layout.addWidget(self.right_lang, 0, 1)

        # Row 2: name
        self.left_name = ClickableLineEdit("get name", self.open_name_dialog)
        self.right_name = QLineEdit("Irfan")
        layout.addWidget(self.left_name, 1, 0)
        layout.addWidget(self.right_name, 1, 1)

        # Row 3: integer
        self.left_int = ClickableLineEdit("Enter an integer", self.open_int_dialog)
        self.right_int = QSpinBox()
        self.right_int.setRange(0, 9999)
        self.right_int.setValue(2025)
        layout.addWidget(self.left_int, 2, 0)
        layout.addWidget(self.right_int, 2, 1)

        self.setLayout(layout)

    def open_language_dialog(self):
        items = ["C", "Java", "Python"]
        val, ok = QInputDialog.getItem(
            self, "Select language", "List of languages",
            items, current=self.right_lang.currentIndex(),
            editable=False
        )
        if ok:
            self.right_lang.setCurrentText(val)

    def open_name_dialog(self):
        txt, ok = QInputDialog.getText(
            self, "Enter name", "Your name:",
            text=self.right_name.text()
        )
        if ok:
            self.right_name.setText(txt)

    def open_int_dialog(self):
        num, ok = QInputDialog.getInt(
            self, "Enter integer", "A number:",
            value=self.right_int.value(), min=0, max=9999
        )
        if ok:
            self.right_int.setValue(num)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    # (re‑apply your QSS here if you like)
    win = InteractiveInputDemo()
    win.show()
    sys.exit(app.exec())