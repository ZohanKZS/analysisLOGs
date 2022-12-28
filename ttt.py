import sys

from PyQt6.QtWidgets import QApplication, QMainWindow


class AppDialog(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Delete logs files KZS v1.0')
        #self.setWindowIcon(QIcon('..\\logo zohan.ico'))
        self.resize(480, 480)
        self.setFixedSize(970, 480)
        self.move(10, 500)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = AppDialog()
    demo.show()

    app.exec()