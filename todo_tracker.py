from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QFrame, QVBoxLayout, QHBoxLayout,
    QScrollArea, QCalendarWidget, QGroupBox, QDateEdit, QTimeEdit, QLineEdit, QMessageBox
)
from PyQt6.QtGui import QTextCharFormat, QFont
from PyQt6.QtCore import Qt, QDate, QTime
import sys

class Ui_ToDoTracker(object):
    def setupUi(self, ToDoTracker):
        ToDoTracker.setObjectName("ToDoTracker")
        ToDoTracker.resize(960, 720)
        ToDoTracker.setStyleSheet("background-color: #2b2b2b; color: white;")

        # Penyimpanan
        self.tasks = {}

        self.dayScrollArea = QScrollArea(ToDoTracker)
        self.dayScrollArea.setGeometry(QtCore.QRect(20, 20, 600, 60))
        self.dayScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.dayScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.dayScrollArea.setWidgetResizable(True)
        self.dayContainer = QWidget()
        self.dayLayout = QHBoxLayout(self.dayContainer)
        self.dayLayout.setContentsMargins(0, 0, 0, 0)
        self.dayScrollArea.setWidget(self.dayContainer)
        self.dayContainer = QWidget()
        self.dayLayout = QHBoxLayout(self.dayContainer)
        self.dayLayout.setContentsMargins(0, 0, 0, 0)
        self.dayScrollArea.setWidget(self.dayContainer)
        self.dayButtons = {}
        for i in range(14):
            dt = QDate.currentDate().addDays(i)
            btn = QPushButton(dt.toString("dd\nMMM"))
            btn.setCheckable(True)
            btn.setFixedSize(70, 50)
            btn.setStyleSheet("background: #3b3b3b; color: white; border-radius: 8px;")
            btn.clicked.connect(lambda checked, d=dt: self.onDaySelected(d))
            self.dayLayout.addWidget(btn)
            self.dayButtons[dt] = btn

        self.taskScrollArea = QScrollArea(ToDoTracker)
        self.taskScrollArea.setGeometry(QtCore.QRect(20, 100, 600, 580))
        self.taskScrollArea.setWidgetResizable(True)
        self.taskScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.taskContainer = QWidget()
        self.taskLayout = QVBoxLayout(self.taskContainer)
        self.taskLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.taskScrollArea.setWidget(self.taskContainer)

        # Panel kanan: calendar + form
        self.calendar = QCalendarWidget(ToDoTracker)
        self.calendar.setGeometry(QtCore.QRect(640, 20, 300, 300))
        fmt = QTextCharFormat()
        fmt.setForeground(Qt.GlobalColor.red)

        # Set hanya hari Minggu ke merah
        self.calendar.setWeekdayTextFormat(Qt.DayOfWeek.Sunday, fmt)

        # Reset hari Sabtu agar tidak merah
        default_fmt = QTextCharFormat()
        self.calendar.setWeekdayTextFormat(Qt.DayOfWeek.Saturday, default_fmt)
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendar.setStyleSheet("background: #2b2b2b; color: white;")
        self.calendar.clicked.connect(self.onDaySelected)
        

        # Form To-Do
        self.leaveGroupBox = QGroupBox(ToDoTracker)
        self.leaveGroupBox.setGeometry(QtCore.QRect(640, 340, 300, 280))
        self.leaveGroupBox.setStyleSheet("""
            QGroupBox {
                border: 1px solid #555;
                border-radius: 8px;
                color: white;
            }
        """)
        font = QFont()
        font.setPointSize(18)      
        font.setBold(True)           
        self.leaveGroupBox.setFont(font)
        self.leaveGroupBox.setTitle("")

        self.formTitle = QLabel("Form To-Do", ToDoTracker)
        self.formTitle.setFont(font)
        self.formTitle.setStyleSheet("color: white;")
        self.formTitle.setGeometry(740, 350, 180, 30)

        # Set Date
        lbl_date = QLabel("Set Date       :", self.leaveGroupBox)
        lbl_date.setGeometry(QtCore.QRect(10, 50, 90, 20))
        lbl_date.setStyleSheet("color: white;")
        self.dateEdit = QDateEdit(self.leaveGroupBox)
        self.dateEdit.setGeometry(QtCore.QRect(100, 50, 180, 25))
        self.dateEdit.setStyleSheet("background: #3b3b3b; color: white;")
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit.dateChanged.connect(self.onDaySelected)


        # Start Time
        lbl_start = QLabel("Start Time    :", self.leaveGroupBox)
        lbl_start.setGeometry(QtCore.QRect(10, 90, 80, 20))
        lbl_start.setStyleSheet("color: white;")
        self.startTimeEdit = QTimeEdit(self.leaveGroupBox)
        self.startTimeEdit.setGeometry(QtCore.QRect(100, 90, 180, 25))
        self.startTimeEdit.setStyleSheet("background: #3b3b3b; color: white;")
        self.startTimeEdit.setTime(QTime.currentTime())

        # End Time
        lbl_end = QLabel("End Time      :", self.leaveGroupBox)
        lbl_end.setGeometry(QtCore.QRect(10, 130, 80, 20))
        lbl_end.setStyleSheet("color: white;")
        self.endTimeEdit = QTimeEdit(self.leaveGroupBox)
        self.endTimeEdit.setGeometry(QtCore.QRect(100, 130, 180, 25))
        self.endTimeEdit.setStyleSheet("background: #3b3b3b; color: white;")
        self.endTimeEdit.setTime(QTime.currentTime().addSecs(3600))

        # Input Activity
        lbl_act = QLabel("Input your To-Do below :", self.leaveGroupBox)
        lbl_act.setGeometry(QtCore.QRect(10, 160, 150, 30))
        lbl_act.setStyleSheet("color: white;")
        self.activityInput = QLineEdit(self.leaveGroupBox)
        self.activityInput.setGeometry(QtCore.QRect(10, 195, 270, 30))
        self.activityInput.setStyleSheet("background: #3b3b3b; color: white;")

        # Submit
        self.submitButton = QPushButton("Submit", self.leaveGroupBox)
        self.submitButton.setGeometry(QtCore.QRect(100, 240, 100, 30))
        self.submitButton.setStyleSheet("background: #0d2c74; color: white;")
        self.submitButton.clicked.connect(self.addTaskCard)

        # Penanda untuk tanggal hari ini
        today = QDate.currentDate()
        if today in self.dayButtons:
            self.onDaySelected(today)
        QtCore.QMetaObject.connectSlotsByName(ToDoTracker)

    def onDaySelected(self, date):
        for d, b in self.dayButtons.items():
            b.setChecked(False)
            b.setStyleSheet("background: #3b3b3b; color: white; border-radius: 8px;")
        btn = self.dayButtons.get(date)
        if btn:
            btn.setChecked(True)
            btn.setStyleSheet("background-color: #0d2c74; color: white; border-radius: 8px;")
        self.currentDate = date
        self.dateEdit.setDate(date)
        self.calendar.setSelectedDate(date)
        self.dateEdit.setDate(date)
        self.refreshTasks()

    def addTaskCard(self):
        sel_date = self.dateEdit.date()

        activity = self.activityInput.text().strip()
        if not activity:
            QMessageBox.warning(
                None,
                "Peringatan",
                "Mohon isi aktivitas terlebih dahulu sebelum submit."
            )
            return

        start_time = self.startTimeEdit.time()
        end_time   = self.endTimeEdit.time()
        if start_time > end_time:
            QMessageBox.warning(
                None,
                "Waktu Tidak Valid",
                "Waktu mulai tidak boleh lebih besar dari waktu selesai."
            )
            return
        if sel_date < QDate.currentDate():
            QMessageBox.warning(None, "Invalid", "Pilihan tanggal anda kurang tepat", "Mohon diatur tidak lebih dari tanggal hari ini")
            return
        activity = self.activityInput.text().strip()
        if not activity:
            return
        start_str = self.startTimeEdit.time().toString("hh:mm AP")
        end_str = self.endTimeEdit.time().toString("hh:mm AP")

        card = QFrame()
        card.setFrameShape(QFrame.Shape.Box)
        card.setStyleSheet("background-color: #f0f4f8; border:1px solid #ccc; border-radius:12px; padding:10px;")
        card.setFixedWidth(550)
        layout = QVBoxLayout(card)
        layout.setSpacing(8)

        hl = QHBoxLayout()
        title = QLabel("List To - Do")
        font = QFont()
        font.setPointSize(16)      
        font.setBold(True) 
        title.setFont(font)
        title.setStyleSheet("font-weight:bold; color:#0d2c74;")
        hl.addWidget(title)
        hl.addStretch()
        status = QLabel("Not Yet.")
        status.setStyleSheet("background-color:#f8bbd0; padding:4px 8px; border-radius:4px; color:black;")
        hl.addWidget(status)
        layout.addLayout(hl)

        card.status_label = status

        # Warna font terpisah untuk card
        content = QLabel(activity)
        content.setStyleSheet("font-size:13px; color:black; background: white; padding:4px; border:1px solid #ddd; border-radius:4px;")
        layout.addWidget(content)
        timer_lbl = QLabel(f"{start_str} - {end_str}")
        timer_lbl.setStyleSheet("font-size:12px; color:black; background: white; padding:4px; border:1px solid #ddd; border-radius:4px;")
        layout.addWidget(timer_lbl)

        bl = QHBoxLayout()
        done = QPushButton("Done")
        done.setStyleSheet("background-color:#5D9C59; color:white; padding:6px 12px; border-radius:8px;")
        decline = QPushButton("Decline")
        decline.setStyleSheet("background-color:#B31312; color:white; padding:6px 12px; border-radius:8px;")

        def on_done():
            status.setText("Finished")
            status.setStyleSheet("background-color:#ccff90; padding:4px 8px; border-radius:4px; color:black;")
            done.hide()
            decline.hide()

            # ambil list kartu untuk tanggal ini
            tasks_list = self.tasks.get(sel_date, [])

            # keluarkan dulu kartu ini
            if card in tasks_list:
                tasks_list.remove(card)

            # hitung berapa kartu sudah berstatus Finished
            finished_count = sum(
                1 for c in tasks_list
                if c.status_label.text() == "Finished"
            )

            # sisipkan kembali di index = finished_count
            tasks_list.insert(finished_count, card)
            self.refreshTasks()

        done.clicked.connect(on_done)
        decline.clicked.connect(lambda: self.removeCard(sel_date, card))
        
        bl.addWidget(done)
        bl.addWidget(decline)
        bl.addStretch()
        layout.addLayout(bl)

        self.tasks.setdefault(sel_date, []).append(card)
        self.refreshTasks()
        self.activityInput.clear()

    def refreshTasks(self):
        while self.taskLayout.count():
            w = self.taskLayout.takeAt(0).widget()
            if w:
                w.setParent(None)
        for c in self.tasks.get(self.currentDate, []):
            self.taskLayout.addWidget(c)

    def removeCard(self, date, card):
        card.setParent(None)
        if date in self.tasks:
            self.tasks[date].remove(card)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    ui = Ui_ToDoTracker()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec())
