import sys
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QApplication,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Start / Stop")

        self.counter =0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_method)



        self.spin_box = QSpinBox()
        self.spin_box.setRange(0, 10_000)
        self.spin_box.setReadOnly(True)
        self.spin_box.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spin_box.setStyleSheet("QSpinBox { background-color: lightgray; }")

        self.button = QPushButton("Start")
        self.button.setCheckable(True)
        self.button.toggled.connect(self.button_method)

        layout = QVBoxLayout()
        layout.addWidget(self.spin_box)
        layout.addWidget(self.button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def button_method(self, is_running: bool) -> None:
        self.button.setText("Stop" if is_running else "Start")
        if is_running:
            self.timer.start(1000)
        else:
            self.timer.stop()

    def timer_method(self):
        self.counter +=1
        self.spin_box.setValue(self.counter)
        if self.counter == 500:
            self.timer.stop()
            self.button.setCheked(False)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
