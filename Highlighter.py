from PyQt5.Qt import *


class MyHighlighter(QSyntaxHighlighter):
    def __init__(self, parent):
        super().__init__(parent)

        self.regexp_by_format = dict()
        self.initForIni()

    def initForIni(self):
        char_format = QTextCharFormat()
        char_format.setFontItalic(False)
        char_format.setForeground(QColor("red"))
        self.regexp_by_format[r'\='] = char_format

        char_format = QTextCharFormat()
        char_format.setFontWeight(QFont.Bold)
        char_format.setForeground(QColor("red"))
        self.regexp_by_format[r'(.+?)(\=|\s|\b)'] = char_format

        char_format = QTextCharFormat()
        char_format.setFontItalic(True)
        char_format.setForeground(QColor("white"))
        self.regexp_by_format[r'(\=|\s\=)(.*)'] = char_format

        char_format = QTextCharFormat()
        char_format.setForeground(QColor("gray"))
        self.regexp_by_format[r'\[(.+?)\]'] = char_format

        char_format = QTextCharFormat()
        char_format.setForeground(QColor("lightgray"))
        self.regexp_by_format[r'(\;|\#)(.+?)$'] = char_format

    def initForJSON(self):

        char_format = QTextCharFormat()
        char_format.setFontItalic(False)
        char_format.setForeground(QColor("#87e7ff"))
        self.regexp_by_format[r'.'] = char_format

        char_format = QTextCharFormat()
        char_format.setFontItalic(True)
        char_format.setForeground(QColor("#ffb787"))
        self.regexp_by_format[r'(true|false|null)'] = char_format

        char_format = QTextCharFormat()
        char_format.setFontItalic(False)
        char_format.setForeground(QColor("red"))
        self.regexp_by_format[r'\"(.+?)\"'] = char_format

        char_format = QTextCharFormat()
        char_format.setFontWeight(QFont.Light)
        char_format.setForeground(QColor("gray"))
        self.regexp_by_format[r'\{'] = char_format
        self.regexp_by_format[r'\}'] = char_format
        self.regexp_by_format[r'\,'] = char_format
        self.regexp_by_format[r'\#'] = char_format  # comments in python style


    def highlightBlock(self, text):
        for regexp, char_format in self.regexp_by_format.items():
            expression = QRegularExpression(regexp)
            it = expression.globalMatch(text)
            while it.hasNext():
                match = it.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), char_format)


if __name__ == '__main__':
    app = QApplication([])

    mw = QTextEdit()
    mw.setStyleSheet("QTextEdit{font-size:20px;background-color: white; color: white;}")

    highlighter = MyHighlighter(mw.document())

    mw.show()

    app.exec()
