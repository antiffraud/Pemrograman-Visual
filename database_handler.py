import sqlite3
import csv
from typing import List, Tuple, Any, Optional

class DatabaseHandler:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.conn: Optional[sqlite3.Connection] = None
        self.cursor: Optional[sqlite3.Cursor] = None

    def connect(self) -> bool:
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            self.create_table_if_not_exists()
            print(f"Berhasil terhubung ke database: {self.db_name}")
            return True
        except sqlite3.Error as e:
            print(f"Gagal koneksi ke database: {e}")
            self.conn = None
            self.cursor = None
            return False

    def create_table_if_not_exists(self):
        if not self.cursor or not self.conn:
            raise ConnectionError("Database tidak terhubung untuk membuat tabel")
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                judul TEXT NOT NULL,
                pengarang TEXT NOT NULL,
                tahun TEXT NOT NULL
            )''')
        self.conn.commit()

    def get_all_books(self) -> List[Tuple[Any, ...]]:
        if not self.cursor: return []
        try:
            self.cursor.execute("SELECT id, judul, pengarang, tahun FROM books ORDER BY id")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Gagal mengambil data yang diinginkan: {e}")
            return []

    def search_books(self, text: str) -> List[Tuple[Any, ...]]:
        if not self.cursor: return []
        try:
            query_text = f"%{text}%"
            self.cursor.execute("SELECT id, judul, pengarang, tahun FROM books WHERE judul LIKE ? ORDER BY id", (query_text,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Gagal mencari data yang diinginkan: {e}")
            return []

    def add_book(self, judul: str, pengarang: str, tahun: str) -> Optional[int]:
        if not self.cursor or not self.conn: return None
        try:
            self.cursor.execute(
                "INSERT INTO books (judul, pengarang, tahun) VALUES (?, ?, ?)",
                (judul, pengarang, tahun)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Gagal menambahkan data: {e}")
            return None

    def update_book(self, book_id: int, column_name: str, new_value: str) -> bool:
        if not self.cursor or not self.conn: return False
        allowed_columns = ["judul", "pengarang", "tahun"] 
        if column_name not in allowed_columns:
            print(f"Nama kolom tidak valid untuk di-update: {column_name}")
            return False
        try:
            self.cursor.execute(f"UPDATE books SET {column_name}=? WHERE id=?", (new_value.strip(), book_id))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Gagal meng-update data: {e}")
            return False

    def delete_book(self, book_id: int) -> bool:
        if not self.cursor or not self.conn: return False
        try:
            self.cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Gagal menghapus data: {e}")
            return False

    def get_books_for_export(self) -> List[Tuple[str, str, str]]:
        if not self.cursor: return []
        try:
            self.cursor.execute("SELECT judul, pengarang, tahun FROM books ORDER BY id")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Gagal mengambil data untuk diekspor: {e}")
            return []

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None
            print(f"Koneksi ke database ditutup: {self.db_name}")