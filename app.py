import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from main_window import BookManager
import config

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = BookManager(db_name=config.DB_NAME)
    if window.db_handler and window.db_handler.conn:
        window.show()
        sys.exit(app.exec())
    else:
        print("Aplikasi tidak dapat berjalan karena terjadi (ex: koneksi database).")
        sys.exit(1) # Keluar kalo db gabisa konek