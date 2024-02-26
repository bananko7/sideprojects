from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QListWidget
from PyQt5.QtCore import QTimer, QTime, QDateTime

class Clock(QWidget):
    def __init__(self):
        super().__init__()

        self.chrono_timer = QTimer()
        self.system_timer = QTimer()
        self.chrono_time = QTime(0, 0)

        self.is_chrono_running = False

        self.init_ui()

    def init_ui(self):
        self.chrono_timer.timeout.connect(self.update_chrono_timer)
        self.system_timer.timeout.connect(self.update_system_clock)

        self.chrono_label = QLabel()
        self.chrono_label.setStyleSheet('font-size: 30px')

        self.system_label = QLabel()
        self.system_label.setStyleSheet('font-size: 30px')

        self.btn_start_stop = QPushButton('Start')
        self.btn_start_stop.clicked.connect(self.start_stop_chrono)

        self.btn_reset = QPushButton('Reset')
        self.btn_reset.clicked.connect(self.reset_chrono)

        self.btn_lap = QPushButton('Lap')
        self.btn_lap.clicked.connect(self.lap_time)

        self.btn_clear = QPushButton('Clear')
        self.btn_clear.clicked.connect(self.clear_laps)

        self.lap_list = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.system_label)
        layout.addWidget(self.chrono_label)
        layout.addWidget(self.btn_start_stop)
        layout.addWidget(self.btn_reset)
        layout.addWidget(self.btn_lap)
        layout.addWidget(self.btn_clear)
        layout.addWidget(self.lap_list)

        self.setLayout(layout)

        self.system_timer.start(1000)

    def start_stop_chrono(self):
        if self.is_chrono_running:
            self.chrono_timer.stop()
            self.btn_start_stop.setText('Start')
        else:
            self.chrono_timer.start(1)
            self.btn_start_stop.setText('Stop')

        self.is_chrono_running = not self.is_chrono_running

    def reset_chrono(self):
        self.chrono_time = QTime(0, 0)
        self.chrono_label.setText(self.chrono_time.toString('hh:mm:ss.zzz'))

    def lap_time(self):
        lap_time = self.chrono_time.toString('hh:mm:ss.zzz')
        self.lap_list.addItem(lap_time)

    def clear_laps(self):
        self.lap_list.clear()

    def update_chrono_timer(self):
        self.chrono_time = self.chrono_time.addMSecs(1)
        self.chrono_label.setText(self.chrono_time.toString('hh:mm:ss.zzz'))

    def update_system_clock(self):
        current_time = QDateTime.currentDateTime().toString('hh:mm:ss')
        self.system_label.setText(current_time)

app = QApplication([])
clock = Clock()
clock.show()
app.exec_()