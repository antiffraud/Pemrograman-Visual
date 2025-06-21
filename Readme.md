# Trackerin - To-Do Activity Tracker

![Trackerin Logo](assets/logo.png)

Trackerin adalah aplikasi desktop modern untuk manajemen aktivitas dan tugas harian yang dibangun menggunakan PyQt6. Aplikasi ini memungkinkan pengguna untuk mengelola jadwal, melacak aktivitas, dan mengeksport data dengan antarmuka yang intuitif dan user-friendly.

## 🚀 Fitur Utama

### 📅 Schedule Management
- **Penjadwalan Tugas**: Tambah, edit, dan hapus tugas dengan mudah
- **Calendar Integration**: Pilih tanggal menggunakan calendar widget interaktif
- **Day Selector**: Navigasi cepat antar tanggal dengan tombol hari
- **Time Management**: Atur waktu mulai dan selesai untuk setiap aktivitas
- **Status Tracking**: Tandai tugas sebagai "Finished" atau "Not Yet"

### 👤 Profile Management
- **User Profile**: Kelola informasi personal (nama lengkap, email, student ID)
- **Profile Picture**: Upload dan ganti foto profil
- **Activity History**: Lihat riwayat semua aktivitas dalam tabel yang dapat diurutkan
- **Search & Filter**: Cari aktivitas berdasarkan nama, email, atau tanggal
- **Inline Editing**: Edit aktivitas langsung dengan double-click

### 📊 Data Export
- **CSV Export**: Export semua data aktivitas ke format CSV
- **Data Preview**: Lihat preview data sebelum export
- **Statistics**: Tampilkan statistik total, completed, dan pending tasks
- **Duration Calculation**: Otomatis menghitung durasi aktivitas

### 🎨 User Interface
- **Modern Design**: Antarmuka yang bersih dan profesional
- **Custom Icons**: Support custom navigation icons
- **Responsive Layout**: Layout yang adaptif untuk berbagai ukuran layar
- **Dark Theme Elements**: Elemen dengan nuansa profesional
- **Dock Widgets**: Panel samping yang dapat dipindah dan disembunyikan


---
## 🔧 Instalasi

### 1. Clone Repository
```bash
git clone https://github.com/username/trackerin.git
cd trackerin
```

### 2. Install Dependencies
```bash
pip install PyQt6
```

### 3. Setup Assets Directory
Pastikan struktur folder sebagai berikut:
```
trackerin/
├── assets/
│   ├── logo.png
│   ├── Frame 182.png
│   ├── Standard.png
│   └── icons/
│       ├── schedule_default.png
│       ├── schedule_clicked.png
│       ├── export_default.png
│       ├── export_clicked.png
│       ├── profile_default.png
│       └── profile_clicked.png
├── database.py
├── main.py
├── main_window.py
├── schedule_page.py
├── profile_page.py
├── export_page.py
└── styles.py
```

### 4. Jalankan Aplikasi
```bash
python main.py
```
---
## 📖 Cara Penggunaan

### Menjalankan Aplikasi
1. Buka terminal/command prompt
2. Navigate ke folder trackerin
3. Jalankan `python main.py`
4. Aplikasi akan membuka dengan halaman Schedule sebagai default

### Schedule Page - Mengelola Tugas
1. **Pilih Tanggal**: 
   - Gunakan day selector di bagian atas untuk navigasi cepat
   - Atau klik calendar widget di sebelah kanan
2. **Tambah Tugas Baru**:
   - Isi form "Form To-Do" di panel kanan
   - Set Start Date dan End Date
   - Atur Start Time dan End Time
   - Masukkan nama aktivitas di "Input Activity"
   - Klik tombol "Submit"
3. **Kelola Tugas**:
   - Task cards akan muncul di sebelah kiri
   - Klik "Done" untuk menandai selesai
   - Klik "Decline" untuk menghapus tugas

### Profile Page - Manajemen Profile dan History
1. **Lihat Activity History**:
   - Semua aktivitas ditampilkan dalam tabel
   - Gunakan search box untuk mencari aktivitas
   - Klik "Filter" untuk menyaring data
2. **Edit Aktivitas**:
   - Double-click pada cell yang ingin diedit
   - Masukkan nilai baru dan konfirmasi
3. **Hapus Aktivitas**:
   - Klik tombol "Delete" di kolom Actions
4. **Update Profile**:
   - Buka Profile dock di sebelah kanan
   - Edit informasi di form "Set My Profile"
   - Klik "Submit" untuk menyimpan
5. **Ganti Profile Picture**:
   - Klik "Change Profile" di Profile dock
   - Pilih file gambar (PNG, JPG, JPEG, GIF, BMP)

### Export Page - Export Data
1. **Preview Data**:
   - Lihat preview semua data yang akan di-export
   - Cek statistik total tasks
2. **Export ke CSV**:
   - Klik tombol "Let's Do it!" atau "Submit"
   - Pilih lokasi dan nama file
   - File CSV akan tersimpan dengan timestamp

### Keyboard Shortcuts
- **Ctrl+N**: Buat tugas baru (focus ke input activity)
- **Ctrl+E**: Buka halaman Export
- **Ctrl+V**: Paste dari clipboard ke input yang sedang aktif
- **Ctrl+Q**: Keluar dari aplikasi
- **F1**: Tampilkan informasi aplikasi

---
## 📦 Import Dependencies & PyQt6 Components

### Import Structure Overview

Aplikasi Trackerin menggunakan berbagai modul Python dan PyQt6 components. Berikut penjelasan detail setiap import dan penggunaannya:

#### **Standard Python Libraries**

```python
import sys                    # System-specific parameters dan functions
import os                     # Operating system interface
import csv                    # CSV file reading dan writing
import sqlite3                # SQLite database operations
import shutil                 # High-level file operations
import platform               # Platform identification
from datetime import datetime, timedelta  # Date dan time manipulation
from typing import List, Dict, Optional   # Type hints untuk better code documentation
```

**Penggunaan dalam Aplikasi:**
- **`sys`**: Digunakan di `main.py` untuk `sys.argv` dan `sys.exit()`
- **`os`**: File path handling, asset checking, directory creation
- **`csv`**: Export functionality di `export_page.py` dan `profile_page.py`
- **`sqlite3`**: Database operations di `database.py`
- **`shutil`**: Copy profile pictures di `profile_page.py`
- **`platform`**: OS detection untuk font selection di `main.py`
- **`datetime`**: Timestamp handling, date calculations di semua modules
- **`typing`**: Type annotations untuk function parameters dan returns

#### **PyQt6 Widget Components**

### Core Application Components

```python
from PyQt6.QtWidgets import QApplication, QMainWindow
```

**QApplication:**
- **File**: `main.py`
- **Fungsi**: Entry point untuk semua GUI applications
- **Kegunaan**: 
  - Mengelola application-wide settings
  - Event loop management
  - System integration (clipboard, fonts)
  - Window management dan lifecycle

**QMainWindow:**
- **File**: `main_window.py`
- **Fungsi**: Main application window dengan built-in features
- **Kegunaan**:
  - Menu bar integration
  - Status bar support
  - Dock widget management
  - Toolbar support
  - Central widget container

### Layout Management Components

```python
from PyQt6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QStackedWidget
)
```

**QVBoxLayout (Vertical Layout):**
- **Files**: Semua UI files
- **Fungsi**: Arrange widgets secara vertikal
- **Kegunaan**:
  - Form layouts (profile forms, task forms)
  - Vertical stacking of components
  - Main page layouts

**QHBoxLayout (Horizontal Layout):**
- **Files**: Semua UI files  
- **Fungsi**: Arrange widgets secara horizontal
- **Kegunaan**:
  - Header navigation buttons
  - Button groups (Done/Decline)
  - Side-by-side components

**QStackedWidget:**
- **File**: `main_window.py`
- **Fungsi**: Container untuk multiple pages dengan satu yang visible
- **Kegunaan**:
  - Page navigation (Schedule/Export/Profile)
  - Memory efficient page management
  - Smooth page transitions

### Input Widgets

```python
from PyQt6.QtWidgets import (
    QLineEdit, QDateEdit, QTimeEdit, QComboBox, 
    QAbstractSpinBox, QCalendarWidget
)
```

**QLineEdit:**
- **Files**: `schedule_page.py`, `profile_page.py`
- **Fungsi**: Single-line text input
- **Kegunaan**:
  - Activity input
  - Search boxes
  - Profile form fields (nama, email, student ID)
  - Placeholder text dan validation

**QDateEdit:**
- **File**: `schedule_page.py`
- **Fungsi**: Date input dengan date picker
- **Kegunaan**:
  - Start date dan end date selection
  - Built-in date validation
  - Calendar popup integration

**QTimeEdit:**
- **File**: `schedule_page.py`
- **Fungsi**: Time input dengan time picker
- **Kegunaan**:
  - Start time dan end time selection
  - AM/PM format support
  - Built-in time validation

**QComboBox:**
- **File**: `profile_page.py`
- **Fungsi**: Dropdown selection list
- **Kegunaan**:
  - Status type selection (Student/Teacher/Staff/Other)
  - Dropdown styling dengan custom arrows
  - Item selection events

**QAbstractSpinBox:**
- **File**: `schedule_page.py`
- **Fungsi**: Base class untuk spin boxes
- **Kegunaan**:
  - Button symbols configuration untuk QDateEdit/QTimeEdit
  - PlusMinus button style

**QCalendarWidget:**
- **File**: `schedule_page.py`
- **Fungsi**: Interactive calendar widget
- **Kegunaan**:
  - Visual date selection
  - Date navigation
  - Custom styling untuk weekends
  - Date click events

### Display Widgets

```python
from PyQt6.QtWidgets import (
    QLabel, QTableWidget, QTableWidgetItem, 
    QScrollArea, QFrame, QGroupBox
)
```

**QLabel:**
- **Files**: Semua UI files
- **Fungsi**: Text dan image display
- **Kegunaan**:
  - Titles dan headings
  - User info display
  - Profile picture display
  - Status labels dengan color coding

**QTableWidget:**
- **Files**: `profile_page.py`, `export_page.py`
- **Fungsi**: Spreadsheet-like table widget
- **Kegunaan**:
  - Activity history display
  - Data preview untuk export
  - Sortable columns
  - Inline editing support
  - Custom cell widgets (buttons)

**QTableWidgetItem:**
- **Files**: `profile_page.py`, `export_page.py`
- **Fungsi**: Individual table cell
- **Kegunaan**:
  - Cell data storage
  - Cell formatting (background colors)
  - Sort data types
  - Selection behavior

**QScrollArea:**
- **Files**: `schedule_page.py`, `export_page.py`
- **Fungsi**: Scrollable container untuk widgets
- **Kegunaan**:
  - Day selector horizontal scroll
  - Task cards vertical scroll
  - Form scroll area
  - Responsive content handling

**QFrame:**
- **Files**: `schedule_page.py`, `export_page.py`
- **Fungsi**: Container dengan visual frame
- **Kegunaan**:
  - TaskCard base class
  - Section separators
  - Visual grouping
  - Custom borders dan backgrounds

**QGroupBox:**
- **File**: `export_page.py`
- **Fungsi**: Container dengan title border
- **Kegunaan**:
  - Data preview section
  - Visual grouping dengan labels
  - Collapsible sections

### Interactive Widgets

```python
from PyQt6.QtWidgets import (
    QPushButton, QMessageBox, QFileDialog,
    QInputDialog, QDockWidget
)
```

**QPushButton:**
- **Files**: Semua UI files
- **Fungsi**: Clickable button
- **Kegunaan**:
  - Navigation buttons (Schedule/Export/Profile)
  - Action buttons (Submit, Done, Decline, Delete)
  - Day selector buttons
  - Custom styling dengan hover effects
  - Icon support

**QMessageBox:**
- **Files**: Semua UI files
- **Fungsi**: Modal dialog untuk messages
- **Kegunaan**:
  - Success notifications
  - Error messages
  - Confirmation dialogs
  - Information displays
  - Custom buttons dan icons

**QFileDialog:**
- **Files**: `profile_page.py`, `export_page.py`
- **Fungsi**: File selection dialog
- **Kegunaan**:
  - Profile picture selection
  - CSV export file save
  - File type filters
  - Directory browsing

**QInputDialog:**
- **File**: `profile_page.py`
- **Fungsi**: Quick input dialogs
- **Kegunaan**:
  - Inline editing inputs
  - Text input dialogs
  - Item selection dialogs
  - Filter option selection

**QDockWidget:**
- **File**: `main_window.py`
- **Fungsi**: Dockable/floatable widget panel
- **Kegunaan**:
  - Profile management panel
  - Resizable dock areas
  - Floating window capability
  - Hide/show functionality
  - Dock area constraints

### Layout Management Additional

```python
from PyQt6.QtWidgets import QHeaderView, QSizePolicy
```

**QHeaderView:**
- **Files**: `profile_page.py`, `export_page.py`
- **Fungsi**: Table header management
- **Kegunaan**:
  - Column width management
  - Resize modes (ResizeToContents, Stretch, Fixed)
  - Header visibility control
  - Section styling

**QSizePolicy:**
- **File**: `schedule_page.py`
- **Fungsi**: Widget size behavior policies
- **Kegunaan**:
  - Widget expansion behavior
  - Minimum/maximum size constraints
  - Responsive layout behavior

#### **PyQt6 Core Components**

```python
from PyQt6.QtCore import Qt, QDate, QTime, QTimer, pyqtSignal
```

**Qt (Namespace):**
- **Files**: Semua UI files
- **Fungsi**: Constants dan enums
- **Kegunaan**:
  - Alignment flags (AlignCenter, AlignLeft, dll)
  - Scroll bar policies
  - Selection behaviors
  - Dock widget areas
  - Key modifiers

**QDate:**
- **File**: `schedule_page.py`
- **Fungsi**: Date handling tanpa time
- **Kegunaan**:
  - Current date tracking
  - Date arithmetic (addDays)
  - Date formatting (toString)
  - Date comparison

**QTime:**
- **File**: `schedule_page.py`
- **Fungsi**: Time handling tanpa date
- **Kegunaan**:
  - Current time display
  - Time arithmetic (addSecs)
  - Time formatting
  - Time validation

**QTimer:**
- **File**: `main_window.py`
- **Fungsi**: Periodic events dan delays
- **Kegunaan**:
  - Auto-refresh status bar setiap menit
  - Timeout signals
  - Single-shot timers
  - Event scheduling

**pyqtSignal:**
- **Files**: `schedule_page.py`, `profile_page.py`
- **Fungsi**: Custom signal definition
- **Kegunaan**:
  - Inter-component communication
  - task_updated signal di TaskCard
  - profile_updated signal di ProfilePage
  - Event-driven architecture

#### **PyQt6 GUI Components**

```python
from PyQt6.QtGui import (
    QAction, QPixmap, QIcon, QFont, QColor, 
    QTextCharFormat, QPainter, QPen, QBrush
)
```

**QAction:**
- **File**: `main_window.py`
- **Fungsi**: Menu dan toolbar actions
- **Kegunaan**:
  - Menu items dengan shortcuts
  - Keyboard shortcuts (Ctrl+N, Ctrl+E, dll)
  - Action triggers
  - Icon dan text properties

**QPixmap:**
- **Files**: `main_window.py`, `profile_page.py`
- **Fungsi**: Image handling dan display
- **Kegunaan**:
  - Logo loading
  - Profile picture processing
  - Image scaling dan transformation
  - Icon creation

**QIcon:**
- **File**: `main_window.py`
- **Fungsi**: Icon management
- **Kegunaan**:
  - Window icon
  - Navigation button icons
  - Custom icon loading
  - Icon state management (default/clicked)

**QFont:**
- **Files**: `main.py`, `export_page.py`
- **Fungsi**: Font configuration
- **Kegunaan**:
  - Platform-specific font selection
  - Font fallback system
  - Table cell font sizing
  - Custom typography

**QColor:**
- **File**: `profile_page.py`
- **Fungsi**: Color management
- **Kegunaan**:
  - Status background colors
  - Cell background coloring
  - Color coding untuk status
  - Custom color schemes

**QTextCharFormat:**
- **File**: `schedule_page.py`
- **Fungsi**: Text formatting untuk rich text
- **Kegunaan**:
  - Calendar text formatting
  - Weekend highlighting (red Sundays)
  - Text color customization

**QPainter, QPen, QBrush:**
- **Files**: `main_window.py`, `profile_page.py`
- **Fungsi**: Custom drawing operations
- **Kegunaan**:
  - Circular image cropping
  - Profile picture circular masking
  - Custom widget painting
  - Advanced graphics operations

### Component Usage Matrix

| Component | main.py | main_window.py | schedule_page.py | profile_page.py | export_page.py |
|-----------|---------|----------------|------------------|-----------------|----------------|
| QApplication | ✅ Primary | ❌ | ❌ | ❌ | ❌ |
| QMainWindow | ❌ | ✅ Primary | ❌ | ❌ | ❌ |
| QDockWidget | ❌ | ✅ Setup | ❌ | ✅ Content | ❌ |
| QStackedWidget | ❌ | ✅ Navigation | ❌ | ❌ | ❌ |
| QCalendarWidget | ❌ | ❌ | ✅ Primary | ❌ | ❌ |
| QTableWidget | ❌ | ❌ | ❌ | ✅ Primary | ✅ Primary |
| QScrollArea | ❌ | ❌ | ✅ Multiple | ❌ | ❌ |
| pyqtSignal | ❌ | ❌ | ✅ TaskCard | ✅ Profile | ❌ |
| QTimer | ❌ | ✅ Status | ❌ | ❌ | ❌ |

### Integration Patterns

**1. Signal-Slot Communication:**
```python
# TaskCard emits signal ketika task updated
self.task_updated.emit()  # schedule_page.py

# ProfilePage emits signal ketika profile changed  
self.profile_updated.emit()  # profile_page.py

# MainWindow listens dan responds
self.profile_page.profile_updated.connect(self.refresh_header_profile)
```

**2. Database Integration:**
```python
# Setiap page component menerima DatabaseHandler instance
self.schedule_page = SchedulePage(self.db)  # main_window.py
self.export_page = ExportPage(self.db)      # main_window.py
self.profile_page = ProfilePage(self.db)    # main_window.py
```

**3. Styling Integration:**
```python
# Centralized styling dari styles.py
from styles import Styles, COLORS
widget.setStyleSheet(Styles.COMPONENT_STYLE)
```

**Sistem import ini memungkinkan aplikasi untuk:**
- **Modular Architecture**: Setiap component independen
- **Reusable Components**: Shared functionality across pages
- **Type Safety**: Type hints untuk better development experience
- **Cross-Platform Compatibility**: Platform-specific handling
- **Rich GUI Features**: Advanced PyQt6 capabilities

## 🏗️ Arsitektur Aplikasi

### Struktur File dan Modul

#### `main.py` - Entry Point Aplikasi
Entry point aplikasi yang mengatur inisialisasi dan konfigurasi awal.

---
**Fungsi Utama:**
```python
def main():
    """
    Fungsi utama untuk menjalankan aplikasi Trackerin
    - Membuat QApplication instance
    - Setup font berdasarkan platform OS
    - Inisialisasi MainWindow
    - Error handling untuk startup
    """
```

**Detail Implementasi:**
- **Platform Detection**: Menggunakan `platform.system()` untuk mendeteksi OS
- **Font Fallback System**: 
  - macOS: Helvetica Neue → Arial → System
  - Windows: Segoe UI → Arial
  - Linux: Ubuntu → DejaVu Sans → Arial
- **Exception Handling**: Try-catch untuk graceful error handling saat startup
- **Window Icon**: Setup icon aplikasi dari `assets/logo.png`

---

#### `database.py` - DatabaseHandler Class
Class utama untuk manajemen database SQLite dengan operasi CRUD lengkap.

---
**Constructor:**
```python
def __init__(self, db_path: str = "trackerin.db"):
    """
    Inisialisasi database handler
    Args:
        db_path (str): Path file database SQLite
    """
```

**Database Initialization:**
```python
def init_database(self):
    """
    Membuat struktur database awal
    - Tabel 'tasks': Menyimpan semua aktivitas/tugas
    - Tabel 'user_profile': Menyimpan informasi profile user
    - Insert default user profile jika belum ada
    """
```

**Task Management Functions:**

```python
def add_task(self, title: str, description: str, start_date: str, 
             end_date: str, start_time: str, end_time: str) -> bool:
    """
    Menambah tugas baru ke database
    Args:
        title (str): Judul aktivitas
        description (str): Deskripsi detail aktivitas
        start_date (str): Tanggal mulai (format: YYYY-MM-DD)
        end_date (str): Tanggal selesai (format: YYYY-MM-DD)
        start_time (str): Waktu mulai (format: HH:MM:SS)
        end_time (str): Waktu selesai (format: HH:MM:SS)
    Returns:
        bool: True jika berhasil, False jika gagal
    """

def get_tasks_by_date(self, date: str) -> List[Dict]:
    """
    Mengambil semua tugas berdasarkan tanggal tertentu
    Args:
        date (str): Tanggal (format: YYYY-MM-DD)
    Returns:
        List[Dict]: List dictionary berisi data tugas
        Sorting: Finished tasks di bawah, kemudian by start_time
    """

def get_all_tasks(self) -> List[Dict]:
    """
    Mengambil semua tugas dari database
    Returns:
        List[Dict]: Semua tugas, sorted by start_date DESC, start_time ASC
    """

def update_task_status(self, task_id: int, status: str) -> bool:
    """
    Update status tugas (Not Yet/Finished)
    Args:
        task_id (int): ID unik tugas
        status (str): Status baru ("Not Yet" atau "Finished")
    Returns:
        bool: True jika berhasil update
    """

def update_task(self, task_id: int, title: str, description: str, 
                start_date: str, end_date: str, start_time: str, end_time: str) -> bool:
    """
    Update informasi lengkap tugas
    Args:
        task_id (int): ID tugas yang akan diupdate
        [parameters lain]: Data baru untuk tugas
    Returns:
        bool: Status keberhasilan update
    """

def delete_task(self, task_id: int) -> bool:
    """
    Hapus tugas dari database
    Args:
        task_id (int): ID tugas yang akan dihapus
    Returns:
        bool: True jika berhasil dihapus
    """

def search_tasks(self, search_term: str) -> List[Dict]:
    """
    Pencarian tugas berdasarkan title atau description
    Args:
        search_term (str): Kata kunci pencarian
    Returns:
        List[Dict]: Tugas yang cocok dengan kriteria pencarian
    """
```

**User Profile Functions:**

```python
def get_user_profile(self) -> Optional[Dict]:
    """
    Mengambil data profile user terbaru
    Returns:
        Optional[Dict]: Data profile atau None jika tidak ada
    """

def update_user_profile(self, fullname: str, email: str, 
                       student_id: str, status_type: str) -> bool:
    """
    Update informasi profile user
    Args:
        fullname (str): Nama lengkap
        email (str): Alamat email
        student_id (str): ID mahasiswa/pegawai
        status_type (str): Tipe status (Student/Teacher/Staff/Other)
    Returns:
        bool: Status keberhasilan update
    """

def update_user_profile_picture(self, picture_path: str) -> bool:
    """
    Update foto profile user
    Args:
        picture_path (str): Path file gambar profile
    Returns:
        bool: True jika berhasil update
    """

def get_task_statistics(self) -> Dict:
    """
    Mengambil statistik tugas untuk dashboard
    Returns:
        Dict: {
            'total_tasks': int,
            'completed_tasks': int, 
            'pending_tasks': int,
            'today_tasks': int
        }
    """
```

---

#### `main_window.py` - MainWindow Class
Window utama aplikasi yang mengatur layout, navigasi, dan integrasi semua komponen.

---
**Constructor & Initialization:**
```python
def __init__(self):
    """
    Inisialisasi main window dengan:
    - Database handler
    - UI setup
    - Menu bar dan status bar
    - Profile dock
    - Timer untuk auto-refresh
    """

def init_ui(self):
    """
    Setup UI utama:
    - Central widget dengan layout
    - Header dengan logo dan navigasi
    - Stacked widget untuk page management
    - Inisialisasi semua pages (Schedule, Export, Profile)
    """
```

**Navigation System:**
```python
def load_navigation_icon(self, icon_name: str, state: str = "default"):
    """
    Load custom navigation icons
    Args:
        icon_name (str): Nama icon (schedule/export/profile)
        state (str): State icon (default/clicked)
    Returns:
        QIcon atau None jika file tidak ditemukan
    """

def setup_navigation_button(self, button, icon_name: str, text: str, default_emoji: str):
    """
    Setup button navigasi dengan icon custom atau emoji fallback
    Args:
        button: QPushButton instance
        icon_name (str): Nama file icon
        text (str): Text label button
        default_emoji (str): Emoji fallback jika icon tidak ada
    """

def update_navigation_button_state(self, button, is_active: bool):
    """
    Update visual state button navigasi
    Args:
        button: QPushButton yang akan diupdate
        is_active (bool): Apakah button sedang aktif
    """
```

**Header Management:**
```python
def create_header(self, main_layout):
    """
    Membuat header bar dengan:
    - Logo aplikasi
    - Navigation buttons (Schedule/Export/Profile)
    - User info display (nama, foto profile)
    """

def load_header_profile_picture(self):
    """
    Load dan crop foto profile menjadi circular
    - Resize ke 40x40 pixels
    - Crop circular dengan QPainter
    - Fallback ke emoji jika gagal load
    """

def refresh_header_profile(self):
    """
    Refresh informasi profile di header
    - Update nama dan status type
    - Reload profile picture
    - Error handling untuk data yang hilang
    """
```

**Menu & Status Bar:**
```python
def setup_menu_bar(self):
    """
    Setup menu bar dengan shortcuts:
    - File: New Task (Ctrl+N), Export (Ctrl+E), Exit (Ctrl+Q)
    - Edit: Paste from Clipboard (Ctrl+V)
    - View: Toggle Profile Dock
    - Help: Application Info (F1), User Guide
    """

def setup_status_bar(self):
    """
    Setup status bar dengan:
    - Informasi student (nama, ID)
    - Copyright notice
    - Auto-update setiap menit
    """

def safe_update_status_bar(self):
    """
    Update status bar dengan error handling
    - Tampilkan current time
    - Update info user dari database
    - Fallback ke default info jika error
    """
```

**Page Management:**
```python
def show_schedule_page(self):
    """Tampilkan halaman Schedule dan refresh data"""

def show_export_page(self):
    """Tampilkan halaman Export dan refresh data"""

def show_profile_page(self):
    """Tampilkan halaman Profile dan show dock"""
```

**Dock Widget:**
```python
def setup_profile_dock(self):
    """
    Setup dock widget untuk profile management:
    - Dockable/floatable/closable
    - Minimum/maximum width constraints
    - Right dock area default
    - Hidden by default
    """

def toggle_profile_dock(self):
    """Toggle visibility profile dock"""
```

**Utility Functions:**
```python
def new_task_shortcut(self):
    """Shortcut Ctrl+N: Focus ke schedule page dan input activity"""

def paste_from_clipboard(self):
    """
    Paste clipboard content ke input yang sedang fokus
    - Detect active input widget
    - Show confirmation dialog
    - Handle error jika clipboard empty
    """

def show_modern_about(self):
    """
    Tampilkan modern about dialog dengan:
    - Logo dan branding
    - Feature list dengan icons
    - Version dan copyright info
    - Custom styling
    """

def safe_get_user_profile(self):
    """
    Safely get user profile dengan comprehensive error handling
    Returns:
        Dict atau None: Data profile user
    """
```

---

#### `schedule_page.py` - SchedulePage Class
Halaman utama untuk manajemen jadwal dan tugas harian.

---
**TaskCard Component:**
```python
class TaskCard(QFrame):
    task_updated = pyqtSignal()  # Signal untuk komunikasi dengan parent
    
    def __init__(self, task_data: Dict, db: DatabaseHandler):
        """
        Widget card untuk menampilkan individual task
        Args:
            task_data (Dict): Data tugas dari database
            db (DatabaseHandler): Database handler instance
        """
    
    def init_ui(self):
        """
        Setup UI card dengan:
        - Header: Title "List To-Do" dan status badge
        - Content: Nama aktivitas dengan word wrap
        - Time info: Start time - End time
        - Action buttons: Done/Decline (jika belum finished)
        """
    
    def mark_as_done(self):
        """
        Mark task sebagai finished:
        - Update database status
        - Update visual status badge
        - Hide action buttons
        - Emit signal untuk refresh parent
        """
    
    def decline_task(self):
        """
        Decline (delete) task dengan confirmation:
        - Show confirmation dialog
        - Delete dari database jika confirmed
        - Emit signal untuk refresh
        """
```

**SchedulePage Main Class:**
```python
def __init__(self, db: DatabaseHandler):
    """
    Inisialisasi schedule page dengan:
    - Database handler
    - Current date tracking
    - Day buttons dictionary
    - Task cards list
    """

def init_ui(self):
    """
    Setup layout utama:
    - Left panel: Day selector dan task cards area
    - Right panel: Calendar dan form input
    - Fixed width untuk responsive layout
    """
```

**Day Selection System:**
```python
def create_day_selector(self, parent_layout):
    """
    Membuat horizontal scroll area dengan day buttons:
    - 14 hari ke depan dari hari ini
    - Button checkable dengan tanggal dan bulan
    - Auto-scroll horizontal
    - Styling dengan hover effects
    """

def select_date(self, date):
    """
    Handle pemilihan tanggal:
    - Update current_date tracker
    - Update visual state semua day buttons
    - Sync dengan calendar widget
    - Update form default dates
    - Refresh task display
    """

def select_today(self):
    """Shortcut untuk select hari ini"""

def on_date_changed(self, date):
    """Handler untuk perubahan date dari form input"""
```

**Calendar Integration:**
```python
def create_calendar(self, parent_layout):
    """
    Setup QCalendarWidget dengan:
    - Fixed size untuk consistency
    - Custom styling (red Sundays)
    - Click handler untuk date selection
    - Integration dengan day selector
    """
```

**Form Input System:**
```python
def create_complete_form(self, parent_layout):
    """
    Membuat form input dalam scroll area:
    - Start Date/End Date dengan QDateEdit
    - Start Time/End Time dengan QTimeEdit
    - Activity input dengan QLineEdit
    - Submit button dengan validation
    - Responsive layout dalam scroll area
    """

def add_task(self):
    """
    Handler untuk submit form:
    - Validasi input (empty title, past dates, time logic)
    - Insert ke database
    - Clear form inputs
    - Refresh task display
    - Show success/error messages
    """
```

**Task Management:**
```python
def refresh_tasks(self):
    """
    Refresh task display:
    - Clear existing task cards
    - Get tasks untuk current date
    - Create TaskCard untuk setiap task
    - Setup signal connections
    - Add stretch untuk proper spacing
    """

def refresh_current_view(self):
    """Public method untuk refresh dari external calls"""

def focus_task_input(self):
    """Focus ke activity input (untuk shortcut Ctrl+N)"""

def paste_to_active_input(self, text: str):
    """
    Paste text ke input yang sedang fokus
    Args:
        text (str): Text dari clipboard
    """
```

---

#### `profile_page.py` - ProfilePage Class
Halaman untuk manajemen profile dan viewing activity history.

---
**Constructor & Signals:**
```python
class ProfilePage(QWidget):
    profile_updated = pyqtSignal()  # Signal ketika profile diupdate
    
    def __init__(self, db: DatabaseHandler):
        """
        Inisialisasi dengan:
        - Database handler
        - Current tasks cache
        - Main window reference
        - Profile picture frame reference
        """
```

**Activity History Table:**
```python
def create_activity_history(self, parent_layout):
    """
    Membuat section activity history dengan:
    - Title label
    - Search/filter controls
    - Activity table dengan 7 kolom
    - Pagination info
    """

def create_activity_table(self, parent_layout):
    """
    Setup QTableWidget dengan:
    - 7 kolom: Date, Activity, Start Time, End Time, Duration, Status, Actions
    - Header resize modes (ResizeToContents, Stretch, Fixed)
    - Sorting enabled
    - Row selection behavior
    - Double-click editing enabled
    - Custom styling
    """

def populate_table(self, tasks: List[Dict]):
    """
    Populate tabel dengan data tasks:
    - Create QTableWidgetItem untuk setiap cell
    - Calculate duration otomatis
    - Color coding untuk status (green/red background)
    - Create delete button untuk setiap row
    - Error handling untuk data yang corrupt
    """

def calculate_duration(self, start_time: str, end_time: str) -> str:
    """
    Hitung durasi antara start dan end time
    Args:
        start_time (str): Format HH:MM:SS
        end_time (str): Format HH:MM:SS
    Returns:
        str: Format "Xh Ym" atau "N/A" jika error
    """
```

**Search & Filter System:**
```python
def search_tasks(self, text: str):
    """
    Real-time search handler:
    - Query database dengan search term
    - Support pencarian di title dan description
    - Update table display
    - Handle empty search (show all)
    """

def show_filter_options(self):
    """
    Tampilkan filter options dialog:
    - All Tasks
    - Completed Only
    - Pending Only  
    - Today's Tasks
    - Apply filter dan update display
    """
```

**Inline Editing System:**
```python
def edit_task_column(self, item: QTableWidgetItem):
    """
    Handler untuk double-click editing:
    - Detect kolom yang diklik
    - Show appropriate input dialog
    - Validate input (format time, dll)
    - Update database
    - Refresh display
    
    Supported columns:
    - Activity: Text input
    - Start Time/End Time: Time format validation
    - Status: Dropdown selection
    - Date: Read-only warning
    - Duration: Calculated field warning
    """

def delete_task(self, task_id: int):
    """
    Delete task dengan confirmation:
    - Show confirmation dialog
    - Delete dari database
    - Refresh table display
    - Show success/error message
    """
```

**Profile Management:**
```python
def get_profile_dock_content(self) -> QWidget:
    """
    Membuat widget content untuk profile dock:
    - Profile picture display (circular crop)
    - Change profile button
    - Profile form (nama, email, student ID, status)
    - Submit button dengan validation
    """

def load_profile_image(self, image_path: str):
    """
    Load dan process profile image:
    - Resize ke 100x100 pixels
    - Crop circular dengan QPainter
    - Return QPixmap atau emoji fallback
    """

def update_profile(self):
    """
    Handler untuk submit profile form:
    - Validate required fields
    - Update database
    - Emit profile_updated signal
    - Show success/error message
    """

def change_profile_picture(self):
    """
    Handler untuk ganti profile picture:
    - Open file dialog (PNG, JPG, JPEG, GIF, BMP)
    - Copy file ke assets directory dengan timestamp
    - Update database dengan new path
    - Update UI display
    - Emit profile_updated signal
    """
```

**Data Management:**
```python
def load_data(self):
    """
    Load semua tasks dari database dengan error handling
    - Cache ke current_tasks
    - Populate table
    """

def refresh_table(self):
    """Public method untuk refresh table dari external calls"""

def export_to_csv(self):
    """
    Export current tasks ke CSV:
    - File dialog dengan timestamp
    - Write CSV dengan proper headers
    - Handle encoding (UTF-8)
    - Show success message dengan file location
    """

def paste_to_active_input(self, text: str):
    """
    Paste ke input yang sedang fokus:
    - Detect focused widget
    - Handle different input types
    - Show confirmation message
    """
```

---

#### `export_page.py` - ExportPage Class
Halaman untuk preview dan export data ke format CSV.

---
**Constructor & Layout:**
```python
def __init__(self, db: DatabaseHandler):
    """
    Inisialisasi export page dengan database handler
    """

def init_ui(self):
    """
    Setup layout utama:
    - Title label
    - Export section dengan background image/gradient
    - Data preview section
    """
```

**Export Section:**
```python
def create_export_section(self, parent_layout):
    """
    Membuat export section dengan:
    - Background image dari assets/Frame 182.png
    - Fallback ke gradient jika image tidak ada
    - Export button dengan custom styling
    - Center alignment untuk button
    """
```

**Data Preview:**
```python
def create_data_preview(self, parent_layout):
    """
    Membuat preview table dengan:
    - 7 kolom: Date, Activity, Start Time, End Time, Duration, Status, Created
    - Header resize modes untuk optimal display
    - Fixed height table dengan scroll
    - Statistics label untuk summary info
    """

def load_export_data(self):
    """
    Load data untuk preview dengan error handling:
    - Get all tasks dari database
    - Populate preview table
    - Handle error dengan empty data fallback
    """

def populate_preview_table(self, tasks: List[Dict]):
    """
    Populate preview table dengan:
    - Format data untuk display
    - Calculate duration untuk setiap task
    - Color coding untuk status
    - Update statistics label
    - Error handling untuk corrupt data
    """
```

**Export Functionality:**
```python
def export_to_csv(self):
    """
    Main export function:
    - Validate ada data untuk export
    - Show file save dialog dengan timestamp
    - Write CSV dengan proper headers dan encoding
    - Include semua field: Date, Activity, Description, Times, Duration, Status, Created
    - Show success dialog dengan file info
    - Comprehensive error handling
    """

def calculate_duration(self, start_time: str, end_time: str) -> str:
    """
    Calculate duration sama seperti di profile page
    - Handle overnight tasks (end < start)
    - Return format "Xh Ym"
    - Error handling return "N/A"
    """

def refresh_data(self):
    """
    Public method untuk refresh data dari external calls
    - Reload export data
    - Update preview display
    """
```

---

#### `styles.py` - Styling System
File konfigurasi styling terpusat untuk konsistensi visual di seluruh aplikasi.

---

**Color Palette:**
```python
COLORS = {
    'primary': '#0E2C75',           # Warna utama aplikasi
    'primary_light': '#0E2C75',     # Variant terang primary
    'secondary': '#f8f9fa',         # Warna secondary (light gray)
    'accent': '#17a2b8',           # Warna accent (cyan)
    'success': '#28a745',          # Hijau untuk success state
    'warning': '#ffc107',          # Kuning untuk warning
    'danger': '#dc3545',           # Merah untuk danger/delete
    'light': '#f8f9fa',            # Background terang
    'dark': '#495057',             # Text gelap
    'white': '#ffffff',            # Pure white
    'text_primary': '#2c3e50',     # Primary text color
    'text_secondary': '#6c757d',   # Secondary text color
    'border': '#dee2e6',           # Border color
    'finished_bg': '#d4edda',      # Background untuk status finished
    'not_yet_bg': '#f8d7da',       # Background untuk status not yet
}
```

**Component Styles:**

**Main Window & General:**
```python
MAIN_WINDOW_STYLE = """..."""       # Background untuk main window
GENERAL_WIDGET_STYLE = """..."""    # Default widget styling
```

**Header & Navigation:**
```python
HEADER_STYLE = """..."""            # Header bar styling
TAB_WIDGET_STYLE = """..."""        # Tab widget (jika digunakan)
```

**Schedule Page Styles:**
```python
SCHEDULE_TITLE_STYLE = """..."""    # Title styling
DAY_BUTTON_STYLE = """..."""        # Day selector buttons
CALENDAR_STYLE = """..."""          # Calendar widget dengan blue theme
TASK_CARD_STYLE = """..."""         # Task card complete styling
```

**Form & Input Styles:**
```python
FORM_WIDGET_STYLE = """..."""       # Form containers
LINE_EDIT_STYLE = """..."""         # Input fields, date/time edits, combobox
SAVE_BUTTON_STYLE = """..."""       # Primary action buttons
```

**Table Styles:**
```python
TABLE_STYLE = """..."""             # Table widget complete styling
TABLE_CONTAINER_STYLE = """..."""   # Table container wrapper
DELETE_BUTTON_STYLE = """..."""     # Delete buttons dalam table
```

**Export & Profile Styles:**
```python
EXPORT_SECTION_STYLE = """..."""    # Export section background
EXPORT_BUTTON_STYLE = """..."""     # Export action button
SEARCH_INPUT_STYLE = """..."""      # Search input fields
DOCK_WIDGET_STYLE = """..."""       # Profile dock styling
```

**Status Bar & UI Elements:**
```python
STATUS_BAR_STYLE = """..."""        # Bottom status bar
STUDENT_INFO_STATUS_STYLE = """...""" # Student info dalam status bar
MESSAGE_BOX_STYLE = """..."""       # Dialog boxes
```

**Utility Function:**
```python
def get_complete_stylesheet() -> str:
    """
    Menggabungkan semua styles menjadi satu stylesheet
    Returns:
        str: Complete CSS stylesheet untuk aplikasi
    """
```

**Design Philosophy:**
- **Consistent Color Scheme**: Menggunakan COLORS dictionary untuk konsistensi
- **Component-Based**: Setiap komponen memiliki style terpisah
- **Responsive**: Style yang adaptif untuk berbagai ukuran
- **Modern Look**: Flat design dengan subtle shadows dan borders
- **Accessibility**: Contrast ratio yang baik untuk readability
- **Professional**: Blue-based theme untuk corporate look

## 🎯 Contoh Penggunaan Advanced

### Custom Icons Setup
1. Buat folder `assets/icons/`
2. Tambahkan icon files dengan naming convention:
   ```
   schedule_default.png  # Icon default
   schedule_clicked.png  # Icon saat active
   export_default.png
   export_clicked.png
   profile_default.png
   profile_clicked.png
   ```
3. Icons akan otomatis terdeteksi dan digunakan

### Database Customization
```python
# Extend DatabaseHandler untuk custom queries
class CustomDB(DatabaseHandler):
    def get_tasks_by_week(self, start_date):
        # Custom query untuk weekly view
        pass
    
    def get_productivity_stats(self):
        # Custom analytics
        pass
```

### Custom Task Card Styling
```python
CUSTOM_TASK_CARD = """
    QFrame#taskCard {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                  stop:0 #your_color, stop:1 #your_other_color);
        border-radius: 20px;
    }
"""
```

## 📝 Changelog

### Version 1.1 (Current)
- ✅ Modern UI dengan custom icons
- ✅ Profile picture support
- ✅ Advanced search dan filtering
- ✅ Inline editing untuk activities
- ✅ Comprehensive error handling
- ✅ Clipboard paste support
- ✅ Dock widgets untuk profile management

### Future Features (Roadmap)
- 🔄 **v1.2**: Dark mode toggle
- 🔄 **v1.3**: Export ke format lain (PDF, Excel)
- 🔄 **v1.4**: Reminder notifications
- 🔄 **v1.5**: Data synchronization dengan cloud
- 🔄 **v1.6**: Mobile companion app
- 🔄 **v1.7**: Team collaboration features

