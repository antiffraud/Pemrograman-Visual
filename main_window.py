# main_window.py
import sys
import csv
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QClipboard
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QMessageBox, QTabWidget, QLabel, QFileDialog, QHeaderView, QInputDialog,
    QSizePolicy, QDockWidget, QStatusBar, QScrollArea, QTextEdit, QApplication
)

import config
from styles import Styles
from database_handler import DatabaseHandler

class BookManager(QMainWindow):
    def __init__(self, db_name: str):
        super().__init__()
        self.db_handler = DatabaseHandler(db_name)
        if not self.db_handler.connect():
            QMessageBox.critical(self, "Database Error",
                                 f"Tidak dapat terhubung dengan database: {db_name}.\nAplikasi keluar.")
            return 

        self.setWindowTitle("Manajemen Buku - New Version")
        self.setGeometry(100, 100, 1150, 800)

        self.clipboard = QApplication.clipboard()
        self.setStyleSheet(Styles.MAIN_WINDOW_STYLE + Styles.GENERAL_WIDGET_STYLE + Styles.TAB_WIDGET_STYLE)

        self.init_status_bar()
        self.init_menu_bar()
        self.init_ui_elements()
        self.init_dock_widgets()

        self.load_data()
        self.update_status("Aplikasi siap digunakan 👍")

    def init_status_bar(self):
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.student_info_label = QLabel(config.STUDENT_INFO_STRING)
        self.student_info_label.setStyleSheet(Styles.STUDENT_INFO_STATUS_STYLE)
        self.student_info_label.setToolTip(config.STUDENT_INFO_STRING)
        self.status_bar.addPermanentWidget(self.student_info_label)
        self.status_bar.showMessage("Memuat aplikasi...")

    def update_status(self, message: str):
        self.status_bar.showMessage(message, 3000)

    def init_menu_bar(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        export_action = file_menu.addAction("Ekspor ke CSV")
        export_action.triggered.connect(self.export_to_csv)
        file_menu.addSeparator()
        exit_action = file_menu.addAction("Keluar")
        exit_action.triggered.connect(self.close)

        edit_menu = menubar.addMenu("Edit")
        search_action = edit_menu.addAction("Cari Judul")
        search_action.triggered.connect(lambda: self.search_input.setFocus() if hasattr(self, 'search_input') else None)
        delete_action = edit_menu.addAction("Hapus Data")
        delete_action.triggered.connect(self.delete_data)
        edit_menu.addSeparator()
        paste_action = edit_menu.addAction("Tempel dari Clipboard")
        paste_action.triggered.connect(self.paste_from_clipboard)

        view_menu = menubar.addMenu("View")
        self.search_dock_action = view_menu.addAction("Panel Pencarian")
        self.search_dock_action.setCheckable(True)
        self.search_dock_action.setChecked(True)
        self.info_dock_action = view_menu.addAction("Panel Informasi")
        self.info_dock_action.setCheckable(True)
        self.info_dock_action.setChecked(True)

    def init_ui_elements(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_scroll = QScrollArea()
        main_scroll.setWidgetResizable(True)
        main_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        main_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll_content_widget = QWidget()
        main_scroll.setWidget(scroll_content_widget)
        self.tabs = QTabWidget()
        self.tab_data = QWidget()
        self.tab_export = QWidget()
        self.tabs.addTab(self.tab_data, "Data Buku")
        self.tabs.addTab(self.tab_export, "Ekspor")
        self.init_data_tab_content()
        self.init_export_tab_content()
        scroll_layout = QVBoxLayout(scroll_content_widget)
        scroll_layout.addWidget(self.tabs)
        central_layout = QVBoxLayout(central_widget)
        central_layout.addWidget(main_scroll)

    def create_student_info_widget(self) -> QWidget:
        container_widget = QWidget()
        container_widget.setStyleSheet(Styles.STUDENT_INFO_CARD_STYLE) 

        layout = QVBoxLayout(container_widget)
        layout.setContentsMargins(20, 15, 20, 15)
        layout.setSpacing(5)                     

        name_label_text_from_config = config.STUDENT_INFO_CARD_HEADER 
        self.name_label = QLabel(name_label_text_from_config)
        self.name_label.setStyleSheet("color: black; background-color: white; font-size: 16px; border: 1px solid black; padding: 5px;")

        nim_label_text_from_config = config.STUDENT_INFO_CARD_NIM
        self.nim_label = QLabel(nim_label_text_from_config)
        self.nim_label.setStyleSheet("color: black; background-color: white; font-size: 16px; border: 1px solid black; padding: 5px;")

        layout.addWidget(self.name_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.nim_label, alignment=Qt.AlignmentFlag.AlignCenter)
        return container_widget

    def create_input_form_widget(self) -> QWidget:
        form_widget = QWidget()
        form_widget.setStyleSheet(Styles.FORM_WIDGET_STYLE)
        form_layout = QVBoxLayout(form_widget)
        form_layout.setSpacing(15)
        form_title = QLabel("📝 Input Data Buku")
        form_title.setStyleSheet(Styles.FORM_TITLE_STYLE)
        form_layout.addWidget(form_title)
        fields_layout = QFormLayout()
        fields_layout.setSpacing(10)
        self.judul_input = QLineEdit()
        self.judul_input.setPlaceholderText("Masukkan judul buku...")
        self.judul_input.setStyleSheet(Styles.LINE_EDIT_STYLE)
        self.pengarang_input = QLineEdit()
        self.pengarang_input.setPlaceholderText("Masukkan nama pengarang...")
        self.pengarang_input.setStyleSheet(Styles.LINE_EDIT_STYLE)
        self.tahun_input = QLineEdit()
        self.tahun_input.setPlaceholderText("Masukkan tahun terbit...")
        self.tahun_input.setStyleSheet(Styles.LINE_EDIT_STYLE)
        fields_layout.addRow("Judul Buku:", self.judul_input)
        fields_layout.addRow("Pengarang:", self.pengarang_input)
        fields_layout.addRow("Tahun Terbit:", self.tahun_input)
        form_layout.addLayout(fields_layout)
        clipboard_layout = QHBoxLayout()
        clipboard_layout.setSpacing(8)
        clipboard_label = QLabel("📋 Clipboard Tools:")
        clipboard_label.setStyleSheet(Styles.CLIPBOARD_LABEL_STYLE)
        clipboard_layout.addWidget(clipboard_label)
        self.paste_judul_btn = QPushButton("Tempel Judul")
        self.paste_judul_btn.setStyleSheet(Styles.CLIPBOARD_BUTTON_STYLE)
        self.paste_judul_btn.clicked.connect(lambda: self.paste_to_field(self.judul_input))
        self.paste_pengarang_btn = QPushButton("Tempel Pengarang")
        self.paste_pengarang_btn.setStyleSheet(Styles.CLIPBOARD_BUTTON_STYLE)
        self.paste_pengarang_btn.clicked.connect(lambda: self.paste_to_field(self.pengarang_input))
        self.paste_tahun_btn = QPushButton("Tempel Tahun")
        self.paste_tahun_btn.setStyleSheet(Styles.CLIPBOARD_BUTTON_STYLE)
        self.paste_tahun_btn.clicked.connect(lambda: self.paste_to_field(self.tahun_input))
        clipboard_layout.addWidget(self.paste_judul_btn)
        clipboard_layout.addWidget(self.paste_pengarang_btn)
        clipboard_layout.addWidget(self.paste_tahun_btn)
        clipboard_layout.addStretch()
        form_layout.addLayout(clipboard_layout)
        return form_widget

    def create_save_button_layout(self) -> QHBoxLayout:
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(10, 20, 10, 20)
        self.save_btn = QPushButton("💾 Simpan Data")
        self.save_btn.setFixedSize(150, 40)
        self.save_btn.setStyleSheet(Styles.SAVE_BUTTON_STYLE)
        self.save_btn.clicked.connect(self.save_data)
        button_layout.addStretch()
        button_layout.addWidget(self.save_btn)
        button_layout.addStretch()
        return button_layout

    def create_data_table_widget(self) -> QWidget:
        table_container = QWidget()
        table_container.setStyleSheet(Styles.TABLE_CONTAINER_STYLE)
        table_layout = QVBoxLayout(table_container)
        table_layout.setContentsMargins(15, 15, 15, 15)
        table_title = QLabel("📊 Data Buku")
        table_title.setStyleSheet(Styles.TABLE_TITLE_STYLE)
        table_layout.addWidget(table_title)

        self.table = QTableWidget()
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(config.TABLE_COLUMN_COUNT)

        for i, label_text in enumerate(config.TABLE_HEADERS):
            if i < self.table.columnCount():
                item = QTableWidgetItem(str(label_text))
                self.table.setHorizontalHeaderItem(i, item)
                print(f"  Set Header Col {i} to '{label_text}'")

        horizontal_header = self.table.horizontalHeader()
        horizontal_header.setVisible(True)
        horizontal_header.show()         
        
        self.table.setStyleSheet(Styles.TABLE_STYLE) 
        
        horizontal_header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        horizontal_header.setVisible(True) 


        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.cellDoubleClicked.connect(self.edit_cell)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setMinimumHeight(350)

        table_layout.addWidget(self.table)
        return table_container

    def create_delete_button_layout(self) -> QHBoxLayout:
        delete_container = QHBoxLayout()
        delete_container.setContentsMargins(10, 10, 10, 20)
        self.delete_btn = QPushButton("🗑️ Hapus Data Terpilih")
        self.delete_btn.setFixedSize(180, 35)
        self.delete_btn.setStyleSheet(Styles.DELETE_BUTTON_STYLE)
        self.delete_btn.clicked.connect(self.delete_data)
        delete_container.addWidget(self.delete_btn)
        delete_container.addStretch()
        return delete_container

    def init_data_tab_content(self):
        data_scroll = QScrollArea()
        data_scroll.setWidgetResizable(True)
        data_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        data_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        data_content_widget = QWidget()
        data_scroll.setWidget(data_content_widget)
        data_layout = QVBoxLayout(data_content_widget)
        data_layout.addWidget(self.create_student_info_widget())
        data_layout.addWidget(self.create_input_form_widget())
        data_layout.addLayout(self.create_save_button_layout())
        data_layout.addWidget(self.create_data_table_widget())
        data_layout.addLayout(self.create_delete_button_layout())
        tab_data_layout = QVBoxLayout(self.tab_data)
        tab_data_layout.addWidget(data_scroll)

    def init_export_tab_content(self):
        export_layout = QVBoxLayout(self.tab_export)
        export_info = QLabel("Ekspor data buku ke format CSV untuk backup atau penggunaan di aplikasi lain.")
        export_info.setWordWrap(True)
        export_info.setStyleSheet("color: #7f8c8d; margin: 20px;")
        export_layout.addWidget(export_info)
        self.export_btn_tab = QPushButton("📊 Ekspor ke CSV")
        self.export_btn_tab.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.export_btn_tab.setStyleSheet(Styles.EXPORT_BUTTON_STYLE)
        self.export_btn_tab.clicked.connect(self.export_to_csv)
        export_layout.addWidget(self.export_btn_tab, alignment=Qt.AlignmentFlag.AlignCenter)
        export_layout.addStretch()

    def create_search_dock_content(self) -> QWidget:
        search_widget = QWidget()
        search_widget.setStyleSheet(Styles.DOCK_WIDGET_STYLE)
        search_layout = QVBoxLayout(search_widget)
        search_layout.setContentsMargins(15, 15, 15, 15)
        search_layout.setSpacing(10)
        search_label = QLabel("🔍 Pencarian Cepat")
        search_label.setStyleSheet(Styles.DOCK_TITLE_STYLE)
        search_layout.addWidget(search_label)
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Cari berdasarkan judul...")
        self.search_input.setStyleSheet(Styles.SEARCH_INPUT_STYLE)
        self.search_input.textChanged.connect(self.search_data)
        search_layout.addWidget(self.search_input)
        clear_search_btn = QPushButton("✖ Bersihkan Pencarian")
        clear_search_btn.clicked.connect(self.clear_search)
        clear_search_btn.setStyleSheet(Styles.CLEAR_SEARCH_BUTTON_STYLE)
        search_layout.addWidget(clear_search_btn)
        search_layout.addStretch()
        return search_widget

    def create_info_dock_content(self) -> QWidget:
        info_widget = QWidget()
        info_widget.setStyleSheet(Styles.DOCK_WIDGET_STYLE) 

        info_layout = QVBoxLayout(info_widget)
        info_layout.setContentsMargins(10, 10, 10, 8)  
        info_layout.setSpacing(5) 
        info_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        info_title = QLabel("ℹ️ Panduan Penggunaan")
        info_title.setStyleSheet(Styles.DOCK_TITLE_STYLE) 
        info_layout.addWidget(info_title)

        self.help_text_edit = QTextEdit() 
        self.help_text_edit.setReadOnly(True)
        self.help_text_edit.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        self.help_text_edit.setHtml(config.HELP_TEXT_HTML)
        self.help_text_edit.setStyleSheet(Styles.HELP_TEXT_EDIT_STYLE) 
        info_layout.addWidget(self.help_text_edit)
        return info_widget

    def init_dock_widgets(self):
        self.search_dock = QDockWidget("🔍 Panel Pencarian", self)
        self.search_dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea |
                                        Qt.DockWidgetArea.RightDockWidgetArea |
                                        Qt.DockWidgetArea.TopDockWidgetArea)
        self.search_dock.setMinimumWidth(250)
        self.search_dock.setWidget(self.create_search_dock_content())
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.search_dock)
        if hasattr(self, 'search_dock_action'):
            self.search_dock_action.triggered.connect(self.search_dock.setVisible)
            self.search_dock.visibilityChanged.connect(self.search_dock_action.setChecked)

        self.info_dock = QDockWidget("ℹ️ Panel Informasi", self)
        self.info_dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea |
                                      Qt.DockWidgetArea.RightDockWidgetArea |
                                      Qt.DockWidgetArea.BottomDockWidgetArea)
        self.info_dock.setMinimumWidth(300)
        self.info_dock.setWidget(self.create_info_dock_content())
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.info_dock)
        if hasattr(self, 'info_dock_action'):
            self.info_dock_action.triggered.connect(self.info_dock.setVisible)
            self.info_dock.visibilityChanged.connect(self.info_dock_action.setChecked)

    def paste_to_field(self, field: QLineEdit):
        clipboard_text = self.clipboard.text()
        if clipboard_text:
            field.setText(clipboard_text)
            field_id = field.objectName() if field.objectName() else "field"
            self.update_status(f"Teks berhasil ditempel ke {field_id}")
        else:
            QMessageBox.information(self, "Clipboard Kosong", "Tidak ada teks di clipboard untuk ditempel.")
            self.update_status("Clipboard kosong")

    def paste_from_clipboard(self):
        clipboard_text = self.clipboard.text()
        if not clipboard_text:
            QMessageBox.information(self, "Clipboard Kosong", "Tidak ada teks di clipboard untuk ditempel.")
            self.update_status("Clipboard kosong")
            return

        parts = []
        if '|' in clipboard_text:
            parts = [p.strip() for p in clipboard_text.split('|')]
        elif ' - ' in clipboard_text and clipboard_text.count(' - ') >= 2:
            parts = [p.strip() for p in clipboard_text.split(' - ', 2)]

        if len(parts) == 3:
            self.judul_input.setText(parts[0])
            self.pengarang_input.setText(parts[1])
            self.tahun_input.setText(parts[2])
            self.update_status("Data buku berhasil diparsing dari clipboard")
        else:
            focused_widget = QApplication.focusWidget()
            if isinstance(focused_widget, QLineEdit) and focused_widget in [self.judul_input, self.pengarang_input, self.tahun_input]:
                focused_widget.setText(clipboard_text)
            elif not self.judul_input.text():
                self.judul_input.setText(clipboard_text)
            elif not self.pengarang_input.text():
                self.pengarang_input.setText(clipboard_text)
            elif not self.tahun_input.text():
                self.tahun_input.setText(clipboard_text)
            else:
                self.judul_input.setText(clipboard_text)
            self.update_status("Teks ditempel dari clipboard")

    def clear_search(self):
        if hasattr(self, 'search_input'):
            self.search_input.clear()
        self.update_status("Pencarian dibersihkan")

    def add_book_to_table(self, book_data_tuple: tuple):
        row_number = self.table.rowCount()
        self.table.insertRow(row_number)
        for column_index, item_data in enumerate(book_data_tuple):
            self.table.setItem(row_number, column_index, QTableWidgetItem(str(item_data)))

    def load_data(self):
        self.table.setRowCount(0)
        all_books = self.db_handler.get_all_books()
        if all_books is not None:
            for book in all_books:
                self.add_book_to_table(book)
            self.update_status(f"Memuat {len(all_books)} record dari database")
        else:
            QMessageBox.warning(self, "Load Data", "Tidak dapat memuat data buku dari database.")
            self.update_status("Gagal memuat data buku")

    def save_data(self):
        judul = self.judul_input.text().strip()
        pengarang = self.pengarang_input.text().strip()
        tahun = self.tahun_input.text().strip()

        if not (judul and pengarang and tahun):
            QMessageBox.warning(self, "Peringatan 🚧", "Semua field harus diisi!")
            self.update_status("Gagal menyimpan - field kosong")
            return

        book_id = self.db_handler.add_book(judul, pengarang, tahun)
        if book_id is not None:
            self.load_data()
            self.judul_input.clear()
            self.pengarang_input.clear()
            self.tahun_input.clear()
            self.update_status(f"Data '{judul}' berhasil disimpan ✅ (ID: {book_id})")
        else:
            QMessageBox.critical(self, "Error Penyimpanan", "Gagal menyimpan data ke database.")
            self.update_status("Gagal menyimpan data")

    def delete_data(self):
        selected_rows = self.table.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Peringatan ⚠️", "Tidak ada baris yang dipilih untuk dihapus.")
            self.update_status("Tidak ada data yang dipilih untuk dihapus")
            return

        current_row = self.table.currentRow()
        if current_row < 0: return

        try:
            book_id_item = self.table.item(current_row, config.TABLE_HEADERS.index("ID"))
            book_title_item = self.table.item(current_row, config.TABLE_HEADERS.index("Judul"))
            if not book_id_item or not book_title_item:
                QMessageBox.critical(self, "Error", "Data baris tidak lengkap untuk dihapus.")
                return
            book_id = int(book_id_item.text())
            book_title = book_title_item.text()
            confirm = QMessageBox.question(
                self, "Konfirmasi Hapus ❔",
                f"Apakah Anda yakin ingin menghapus buku '{book_title}' (ID: {book_id})?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            if confirm == QMessageBox.StandardButton.Yes:
                if self.db_handler.delete_book(book_id):
                    self.load_data()
                    self.update_status(f"Data '{book_title}' berhasil dihapus 🗑️")
                else:
                    QMessageBox.critical(self, "Error Penghapusan", f"Gagal menghapus data '{book_title}' dari database.")
                    self.update_status(f"Gagal menghapus data '{book_title}'")
        except (ValueError, AttributeError, IndexError) as e:
            QMessageBox.critical(self, "Error", f"Kesalahan saat memproses penghapusan: {e}")

    def search_data(self, text: str):
        self.table.setRowCount(0)
        query_text = text.strip()
        search_results = []
        if query_text:
            search_results = self.db_handler.search_books(query_text)
            status_msg = f"Ditemukan {len(search_results)} hasil pencarian 🔍"
        else:
            search_results = self.db_handler.get_all_books()
            status_msg = f"Menampilkan semua data ({len(search_results)} record)"
        if search_results is not None:
            for book in search_results:
                self.add_book_to_table(book)
        self.update_status(status_msg)

    def edit_cell(self, row: int, column: int):
        if column == config.TABLE_HEADERS.index("ID"):
            self.update_status("ID buku tidak dapat diubah.")
            return
        try:
            current_item = self.table.item(row, column)
            book_id_item = self.table.item(row, config.TABLE_HEADERS.index("ID"))
            book_title_item = self.table.item(row, config.TABLE_HEADERS.index("Judul"))
            if not current_item or not book_id_item or not book_title_item:
                QMessageBox.warning(self, "Edit Error", "Data sel tidak lengkap untuk diedit.")
                return
            current_value = current_item.text()
            field_name = config.TABLE_HEADERS[column]
            book_id = int(book_id_item.text())
            book_title_for_prompt = book_title_item.text()
        except (ValueError, AttributeError, IndexError) as e:
            QMessageBox.critical(self, "Error", f"Kesalahan saat mengambil data sel untuk diedit: {e}")
            return

        new_value, ok = QInputDialog.getText(
            self, f"Edit {field_name}",
            f"Masukkan {field_name.lower()} baru untuk '{book_title_for_prompt}':",
            text=current_value
        )
        if ok and new_value.strip() != current_value.strip():
            db_column_name = config.TABLE_DB_COLUMNS[column]
            if self.db_handler.update_book(book_id, db_column_name, new_value.strip()):
                self.load_data()
                self.update_status(f"{field_name} untuk '{book_title_for_prompt}' berhasil diperbarui 🔄")
            else:
                QMessageBox.critical(self, "Error Update", f"Gagal memperbarui {field_name} di database.")
                self.update_status(f"Gagal memperbarui {field_name}")

    def export_to_csv(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Simpan File CSV", "data_buku.csv", "CSV Files (*.csv)"
        )
        if path:
            books_to_export = self.db_handler.get_books_for_export()
            if books_to_export is not None:
                try:
                    with open(path, mode='w', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        writer.writerow([config.TABLE_HEADERS[1], config.TABLE_HEADERS[2], config.TABLE_HEADERS[3]])
                        writer.writerows(books_to_export)
                    QMessageBox.information(
                        self, "Berhasil Ekspor 🎉",
                        f"Data berhasil diekspor ke CSV.\nFile: {path}\nTotal: {len(books_to_export)} record"
                    )
                    self.update_status(f"Data berhasil diekspor ke {path}")
                except IOError as e:
                    QMessageBox.critical(self, "Error Ekspor IO", f"Gagal menulis file CSV: {e}")
                    self.update_status(f"Gagal mengekspor data: {e}")
            else:
                QMessageBox.warning(self, "Ekspor Gagal", "Tidak ada data untuk diekspor atau terjadi kesalahan database.")
                self.update_status("Gagal mengekspor data")

    def closeEvent(self, event):
        if self.db_handler:
            self.db_handler.close()
        self.update_status("Aplikasi ditutup 👋")
        event.accept()