import sys
import random
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtCore import Qt, QPoint, QEvent

class MouseTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tugas Week 3 - (F1D022065 - Muhamad Erwin Hariadinata)")
        self.background_pixmap = QPixmap("Background.webp")
        self.resize(1000, 600)

        self.label = QLabel("Catch Me If You Can!", self)
        self.label.setGeometry(100, 100, 200, 50)
        self.label.setStyleSheet("""
            background-color: rgba(255, 255, 255, 150);
            color: red;
            font-size: 18px;
            font-weight: bold;
            border: 2px solid black;
            border-radius: 10px;
        """)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.installEventFilter(self)
        self.label.setMouseTracking(True)
        self.setMouseTracking(True)

    def paintEvent(self, event):
        painter = QPainter(self)
        scaled_pixmap = self.background_pixmap.scaled(
            self.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        x = (self.width() - scaled_pixmap.width()) // 2
        y = (self.height() - scaled_pixmap.height()) // 2
        painter.drawPixmap(x, y, scaled_pixmap)

        super().paintEvent(event)

    def mouseMoveEvent(self, event):
        x = int(event.position().x())
        y = int(event.position().y())
        self.label.setText(f"x: {x}, y: {y}")

    def eventFilter(self, source, event):
        if source == self.label and event.type() == QEvent.Type.Enter:
            self.move_label()
        return super().eventFilter(source, event)

    def move_label(self):
        new_x = random.randint(0, self.width() - self.label.width())
        new_y = random.randint(0, self.height() - self.label.height())
        self.label.move(QPoint(new_x, new_y))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MouseTracker()
    window.show()
    sys.exit(app.exec())
