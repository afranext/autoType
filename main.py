import sys
from PyQt5.Qt import *
import glob
import os
import pyautogui
import time


def adapt_files(file_path):
    return os.path.basename(os.path.normpath(file_path))


class Widget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('AutoType')
        self.setFixedWidth(300)
        self.setFixedHeight(100)

        self.button = QPushButton("Start Typing")
        self.button.clicked.connect(self.on_click)

        self.current_text = None

        self.combo = QComboBox(self)
        files_paths = glob.glob("/home/ali/AutoType/*")
        files_paths.insert(0, "Select a file")
        files_names = list(map(adapt_files, files_paths))
        self.combo.addItems(files_names)
        self.combo.currentTextChanged.connect(self.on_combobox_func)

        v_box = QVBoxLayout()
        v_box.addWidget(self.combo)
        v_box.addWidget(self.button)
        v_box.addStretch()

        h_box = QHBoxLayout(self)
        h_box.addLayout(v_box)

    def on_combobox_func(self, text):
        self.current_text = text

    def on_click(self):
        self.close()
        opened_file = open("/home/ali/AutoType/" + self.current_text, "r")
        time.sleep(1)
        for character in opened_file.read():
            pyautogui.typewrite(character)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Widget()
    demo.show()
    sys.exit(app.exec_())
