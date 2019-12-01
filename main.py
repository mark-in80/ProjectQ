import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication, qApp)
from PyQt5 import Qt
from PyQt5.Qt import (QSyntaxHighlighter, QTextCharFormat, QIcon, QColor, QFont, QRegularExpression)


class MainWindow(QMainWindow):
    def __init__(self):
        """Main Window
        Menu, Status Bar"""
        super(MainWindow, self).__init__()

        # Main window 980х850
        self.resize(980, 850)
        # main window and name
        self.setGeometry(518, 70, 980, 850)
        self.setWindowTitle('')

    def font(self):
        """Font text"""
        # Install font
        self.font_size = Qt.QSpinBox()
        self.font_size.setRange(5, 40)
        self.font_size.valueChanged.connect(self.font_size_changed)
        # Install widget
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        layout = Qt.QVBoxLayout()
        layout.addWidget(self.font_size)
        layout.addWidget(self.textEdit)
        central_widget = Qt.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = MainWindow()
    GUI.show()
    sys.exit(app.exec_())
