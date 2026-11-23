import sys
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QSlider,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtCore import Qt


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

        self.slider_spin_box = QSpinBox()
        self.slider_spin_box.setRange(0, 255)
        self.slider_spin_box.setReadOnly(True)
        self.slider_spin_box.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.slider_spin_box.setStyleSheet("QSpinBox { background-color: lightgray; }")

        self.slider = QSlider(Qt.Orientation.Vertical)
        self.slider.setRange(0, 255)
        self.slider.valueChanged.connect(self.slider_method)

        self.button = QPushButton("Start")
        self.button.setCheckable(True)
        self.button.toggled.connect(self.button_method)

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.spin_box)
        left_layout.addWidget(self.button)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.slider_spin_box)
        right_layout.addWidget(self.slider)

        layout = QHBoxLayout()
        layout.addLayout(left_layout)
        layout.addLayout(right_layout)

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

    def slider_method(self):
        value = self.slider.value()
        self.slider_spin_box.setValue(value)
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
