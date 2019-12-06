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

    def menu(self):
        """Menu file window"""
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        # Menu File - part Exit
        newAction = QAction(QIcon('new.png'), '&New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('New file')
        # newAction.triggered.connect(self.new_file)
        # Menu File - part Open
        openAction = QAction(QIcon('open.png'), '&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open File')
        # openAction.triggered.connect(self.open_file)
        # Menu File - part Save As
        save_asAction = QAction(QIcon('save_as.png'), '&Save As...', self)
        save_asAction.setShortcut('Ctrl+S')
        save_asAction.setStatusTip('Save file as...')
        # save_asAction.triggered.connect(self.save_As)
        # Initialization buttons menu
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(save_asAction)
        fileMenu.addAction(exitAction)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = MainWindow()
    GUI.menu()
    GUI.show()
    sys.exit(app.exec_())
