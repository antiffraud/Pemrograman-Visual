from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QSlider, QVBoxLayout, QHBoxLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import sys


class AdjustmenProject(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("F1D022065 - Muhamad Erwin Hariadinata")
        self.setFixedSize(520, 320)

        self.label = QLabel("F1D022065")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QFont("Arial", 24))
        self.label.setStyleSheet("background-color: white; color: black;")

        self.font_slider = self.create_slider(10, 72, 24, 2)

        self.bg_slider = self.create_slider(0, 255, 255, 15)

        self.font_color_slider = self.create_slider(0, 255, 0, 15)

        self.font_slider.valueChanged.connect(self.update_font_size)
        self.bg_slider.valueChanged.connect(self.update_colors)
        self.font_color_slider.valueChanged.connect(self.update_colors)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addSpacing(10)
        layout.addLayout(self.create_slider_layout("Font Size", self.font_slider))
        layout.addLayout(self.create_slider_layout("Background Color", self.bg_slider))
        layout.addLayout(self.create_slider_layout("Font Color", self.font_color_slider))

        self.setLayout(layout)

    def create_slider(self, min_val, max_val, default_val, tick_interval):
        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setRange(min_val, max_val)
        slider.setValue(default_val)
        slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        slider.setTickInterval(tick_interval)
        slider.setSingleStep(1)

        slider.setStyleSheet("""
            QSlider {
                background: transparent;
            }

            QSlider::groove:horizontal {
                border: none;
                height: 6px;
                background: #555;
                margin: 0 0;
                border-radius: 3px;
            }

            QSlider::handle:horizontal {
                background: lightgray;
                border: none;
                width: 14px;
                height: 30px;
                margin: -12px 0;  /* pull handle vertically to center */
                border-radius: 6px;
            }

            QSlider::sub-page:horizontal {
                background: #aaa;
                border-radius: 3px;
            }

            QSlider::add-page:horizontal {
                background: #444;
                border-radius: 3px;
            }

            QSlider::tick-position:below {
                background: white;
            }

            QSlider::tick-mark:horizontal {
                background: white;
                width: 2px;
                height: 8px;
            }
        """)
        return slider

    def create_slider_layout(self, label_text, slider):
        layout = QHBoxLayout()
        label = QLabel(label_text)
        label.setFixedWidth(130)
        layout.addWidget(label)
        layout.addWidget(slider)
        return layout

    def update_font_size(self):
        size = self.font_slider.value()
        font = self.label.font()
        font.setPointSize(size)
        self.label.setFont(font)

    def update_colors(self):
        bg_value = self.bg_slider.value()
        font_value = self.font_color_slider.value()
        self.label.setStyleSheet(
            f"background-color: rgb({bg_value}, {bg_value}, {bg_value});"
            f"color: rgb({font_value}, {font_value}, {font_value});"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdjustmenProject()
    window.show()
    sys.exit(app.exec())
