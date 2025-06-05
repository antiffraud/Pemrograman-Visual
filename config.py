DB_NAME = 'books.db'

TABLE_COLUMN_COUNT = 4
TABLE_HEADERS = ["ID", "Judul", "Pengarang", "Tahun"]
TABLE_DB_COLUMNS = ["id", "judul", "pengarang", "tahun"] 

STUDENT_NAME = "Muhamad Erwin Hariadinata"
STUDENT_NIM = "F1D022065"
STUDENT_INFO_STRING = f"{STUDENT_NAME} - {STUDENT_NIM}"

STUDENT_INFO_CARD_HEADER = f"Nama: {STUDENT_NAME}"
STUDENT_INFO_CARD_NIM = f"NIM: {STUDENT_NIM}"

HELP_TEXT_HTML = """
<div style='font-family: Arial, sans-serif; font-size: 12px; line-height: 1.5;'>
<b>🚀 Cara Menggunakan Aplikasi:</b><br><br>
<b>➕ Menambah Data Buku:</b><br>
1. Isi form Judul, Pengarang, dan Tahun<br>
2. Gunakan tombol clipboard untuk menempel teks<br>
3. Klik tombol "Simpan Data"<br><br>
<b>🔍 Mencari Data:</b><br>
• Gunakan kotak pencarian di panel kiri<br>
• Ketik judul buku yang ingin dicari<br>
• Data akan tersaring secara otomatis<br><br>
<b>✏️ Mengedit Data:</b><br>
• Double-click pada sel di tabel untuk mengedit<br>
• Masukkan data baru dan tekan OK<br><br>
<b>🗑️ Menghapus Data:</b><br>
1. Pilih baris data di tabel<br>
2. Klik tombol "Hapus Data Terpilih"<br>
3. Konfirmasi penghapusan<br><br>
<b>📊 Ekspor Data:</b><br>
• Gunakan tab "Ekspor" untuk menyimpan ke CSV<br>
• File dapat dibuka di Excel atau aplikasi lain<br><br>
<b>📋 Fitur Clipboard:</b><br>
• Copy teks dari aplikasi lain<br>
• Gunakan tombol "Tempel" untuk memasukkan data<br>
• Format khusus: "Judul|Pengarang|Tahun"
</div>
"""