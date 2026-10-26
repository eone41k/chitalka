from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QApplication, QWidget, QGridLayout, QStackedLayout, QTabWidget, QFontDialog, QFileDialog
from PyQt5.QtGui import QPalette, QColor, QPixmap

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.pages = []
        self.current_page = 0
        
        self.central_widget.setStyleSheet("""
            QWidget#central_widget {
                background-image: url("фон2.jpg") 0 0 0 0 stretch stretch;
            }
        """)

        self.text_edit.setStyleSheet("""
            QTextEdit {
                background-color: rgba(255, 255, 150, 100);
                color: #202938;
                font-size: 16px;
                border: 1px solid rgba(255, 255, 250, 150);
                border-radius: 10px;
                padding: 12px;
            }
        """)

    def initUI(self):
        self.setWindowTitle('читалка')
        self.resize(1000, 1000)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.v_maket = QVBoxLayout()
        self.central_widget.setLayout(self.v_maket)

        self.h_maket = QHBoxLayout()

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        self.text_edit.setGeometry(50, 50, 900, 800)
        self.text_edit.setStyleSheet(("font-size: 16px; color: black;"))
        self.v_maket.addWidget(self.text_edit)

        self.v_maket.addLayout(self.h_maket)

        self.push_btn_prev = self.create_button('<<<предыдущая страница', '#B8D189', '#B6E861')
        self.push_btn_prev.clicked.connect(self.prev_list)
        self.h_maket.addWidget(self.push_btn_prev)

        self.push_btn_font = self.create_button('изменить шрифт', '#CACC54', '#E3E647')
        self.push_btn_font.clicked.connect(self.change_font)
        self.h_maket.addWidget(self.push_btn_font)

        self.push_btn_file = self.create_button('выбрать файл', '#CACC54', '#E3E647')
        self.push_btn_file.clicked.connect(self.change_file)
        self.h_maket.addWidget(self.push_btn_file)

        self.push_btn_next = self.create_button('следущая страница>>>', '#B8D189', '#B6E861')
        self.push_btn_next.clicked.connect(self.next_list)
        self.h_maket.addWidget(self.push_btn_next)

    def change_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.text_edit.setFont(font)

    def change_file(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        with open(fname, 'r', encoding= 'utf-8') as f:
            data = f.read()
            self.split_text_into_page(data)
            self.show_page(0)

    def split_text_into_page(self, text):
        self.pages = []
        lines = text.splitlines()
        page_size = 10
        for x in range(0, len(lines), page_size):
            page = "\n".join(lines[x:x + page_size])
            self.pages.append(page)

        self.current_page = 0

    def show_page(self, page_index):
        if 0<=page_index<len(self.pages):
            self.text_edit.setPlainText(self.pages[page_index])
            self.current_page = page_index

    def next_list(self):
        if self.current_page<len(self.pages)-1:
            self.show_page(self.current_page + 1)

    def prev_list(self):
        if self.current_page>0:
            self.show_page(self.current_page-1)

    def create_button(self, text_btn, color, hover_color):
        button = QPushButton()
        button.setText(f'{text_btn}')
        button.setStyleSheet(
            f"""
                        QPushButton {{
                            background-color: {color};  /* Красный цвет */
                            color: white;
                            font-size: 14px;
                            padding: 10px;
                            border-radius: 5px;
                        }}
                        QPushButton:hover {{
                            background-color: {hover_color};  /* Темно-красный цвет при наведении */
                        }}
                        """
        )
        return button

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())