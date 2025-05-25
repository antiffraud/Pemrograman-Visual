import sys
import sqlite3
import csv
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QMessageBox, QTabWidget, QLabel, QFileDialog, QHeaderView, QInputDialog,
    QSizePolicy, QGridLayout
)

DB_NAME = 'books.db'

class BookManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manajemen Buku")
        self.setGeometry(100, 100, 700, 500)

        # Menu Bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        save_action = file_menu.addAction("Simpan")
        save_action.triggered.connect(self.save_data)
        export_action = file_menu.addAction("Ekspor ke CSV")
        export_action.triggered.connect(self.export_to_csv)
        exit_action = file_menu.addAction("Keluar")
        exit_action.triggered.connect(self.close)

        edit_menu = menubar.addMenu("Edit")
        search_action = edit_menu.addAction("Cari Judul")
        search_action.triggered.connect(lambda: self.search_input.setFocus())
        delete_action = edit_menu.addAction("Hapus Data")
        delete_action.triggered.connect(self.delete_data)

        self.init_db()
        self.init_ui()
        self.load_data()

    def init_db(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.c = self.conn.cursor()
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                judul TEXT,
                pengarang TEXT,
                tahun TEXT
            )''')
        self.conn.commit()

    def init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        self.tabs = QTabWidget()
        self.tab_data = QWidget()
        self.tab_export = QWidget()

        self.tabs.addTab(self.tab_data, "Data Buku")
        self.tabs.addTab(self.tab_export, "Ekspor")

        data_layout = QVBoxLayout()
        info_grid = QGridLayout()
        info_grid.setHorizontalSpacing(10)
        info_grid.setVerticalSpacing(2)
        label_nama = QLabel("Nama :")
        value_nama = QLabel("Muhamad Erwin Hariadinata")
        label_nim = QLabel("NIM    :")
        value_nim = QLabel("F1D022065")
        for lbl in (label_nama, label_nim):
            lbl.setStyleSheet("font-weight: bold; font-size: 12px;")
        for val in (value_nama, value_nim):
            val.setStyleSheet("font-size: 12px;")
        info_grid.addWidget(label_nama, 0, 0)
        info_grid.addWidget(value_nama, 0, 1)
        info_grid.addWidget(label_nim, 1, 0)
        info_grid.addWidget(value_nim, 1, 1)

        hcenter = QHBoxLayout()
        hcenter.addStretch()
        hcenter.addLayout(info_grid)
        hcenter.addStretch()
        data_layout.addLayout(hcenter)

        form_layout = QFormLayout()
        self.judul_input = QLineEdit()
        self.pengarang_input = QLineEdit()
        self.tahun_input = QLineEdit()
        form_layout.addRow("Judul:", self.judul_input)
        form_layout.addRow("Pengarang:", self.pengarang_input)
        form_layout.addRow("Tahun:", self.tahun_input)
        data_layout.addLayout(form_layout)

        self.save_btn = QPushButton("Simpan")
        self.save_btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        data_layout.addWidget(self.save_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.save_btn.clicked.connect(self.save_data)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Cari judul...")
        self.search_input.textChanged.connect(self.search_data)
        data_layout.addWidget(self.search_input)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Judul", "Pengarang", "Tahun"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.cellDoubleClicked.connect(self.edit_cell)
        data_layout.addWidget(self.table)

        hbox = QHBoxLayout()
        self.delete_btn = QPushButton("Hapus Data")
        self.delete_btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.delete_btn.clicked.connect(self.delete_data)
        hbox.addWidget(self.delete_btn, alignment=Qt.AlignmentFlag.AlignLeft)
        data_layout.addLayout(hbox)

        self.tab_data.setLayout(data_layout)

        export_layout = QVBoxLayout()
        self.export_btn = QPushButton("Ekspor ke CSV")
        self.export_btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        export_layout.addWidget(self.export_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        self.export_btn.clicked.connect(self.export_to_csv)
        self.tab_export.setLayout(export_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tabs)
        central.setLayout(main_layout)

    def load_data(self):
        self.table.setRowCount(0)
        self.c.execute("SELECT * FROM books")
        for row_data in self.c.fetchall():
            row_number = self.table.rowCount()
            self.table.insertRow(row_number)
            for column, data in enumerate(row_data):
                self.table.setItem(row_number, column, QTableWidgetItem(str(data)))

    def save_data(self):
        judul = self.judul_input.text().strip()
        pengarang = self.pengarang_input.text().strip()
        tahun = self.tahun_input.text().strip()

        if not (judul and pengarang and tahun):
            QMessageBox.warning(self, "Peringatan", "Semua field harus diisi!")
            return

        self.c.execute(
            "INSERT INTO books (judul, pengarang, tahun) VALUES (?, ?, ?)", (judul, pengarang, tahun)
        )
        self.conn.commit()
        self.load_data()
        self.judul_input.clear()
        self.pengarang_input.clear()
        self.tahun_input.clear()

    def delete_data(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "Peringatan", "Tidak ada baris yang dipilih.")
            return
        confirm = QMessageBox.question(
            self, "Konfirmasi Hapus", "Apakah Anda yakin ingin menghapus data ini?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirm == QMessageBox.StandardButton.Yes:
            book_id = self.table.item(selected, 0).text()
            self.c.execute("DELETE FROM books WHERE id=?", (book_id,))
            self.conn.commit()
            self.load_data()

    def search_data(self, text):
        self.table.setRowCount(0)
        self.c.execute("SELECT * FROM books WHERE judul LIKE ?", (f"%{text}%",))
        for row_data in self.c.fetchall():
            row_number = self.table.rowCount()
            self.table.insertRow(row_number)
            for column, data in enumerate(row_data):
                self.table.setItem(row_number, column, QTableWidgetItem(str(data)))

    def edit_cell(self, row, column):
        if column == 0:
            return
        current = self.table.item(row, column).text()
        field = self.table.horizontalHeaderItem(column).text().lower()
        new_value, ok = QInputDialog.getText(
            self, f"Edit {field.capitalize()}", f"Masukkan {field} baru:", text=current
        )
        if ok and new_value:
            book_id = self.table.item(row, 0).text()
            col_name = ["id", "judul", "pengarang", "tahun"][column]
            self.c.execute(f"UPDATE books SET {col_name}=? WHERE id=?", (new_value, book_id))
            self.conn.commit()
            self.load_data()

    def export_to_csv(self):
        path, _ = QFileDialog.getSaveFileName(self, "Simpan CSV", "data_buku.csv", "CSV Files (*.csv)")
        if path:
            with open(path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Judul", "Pengarang", "Tahun"])
                self.c.execute("SELECT judul, pengarang, tahun FROM books")
                for row in self.c.fetchall():
                    writer.writerow(row)
            QMessageBox.information(self, "Berhasil", "Data berhasil diekspor ke CSV.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BookManager()
    window.show()
    sys.exit(app.exec())
