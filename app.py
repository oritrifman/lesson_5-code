import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QSpinBox, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Start / Stop")

        self.spin_box = QSpinBox()
        self.spin_box.setRange(0, 10_000)

        self.toggle_button = QPushButton("Start")
        self.toggle_button.setCheckable(True)
        self.toggle_button.toggled.connect(self.button_method)

        layout = QVBoxLayout()
        layout.addWidget(self.spin_box)
        layout.addWidget(self.toggle_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def button_method(self, is_running: bool) -> None:
        self.toggle_button.setText("Stop" if is_running else "Start")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
