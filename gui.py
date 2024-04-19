from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow():
    def __init__(self, size_window: tuple[int, int]=(600,700)):
        super(self).__init__()
        self.resize(size_window)


if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    window.show()
    app.exec()
