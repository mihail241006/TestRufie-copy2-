# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

from instr import *


class FinalWin(QWidget):
    def __init__(self,exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()
    def initUI(self):
        self.workh_text = QLabel(txt_workheart + self.results())
        self.index_text = QLabel(txt_index + str(self.index))
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)   
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def results(self):
        self.index = (4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index < 14.9 and self.index >= 11:
                return txt_res2
            elif self.index < 10.9 and self.index >= 6:
                return txt_res3
            elif self.index < 5.9 and self.index >= 0.5:
                return txt_res4
            elif self.index <= 0.4:
                return txt_res5
        if self.exp.age < 14 and self.index >= 13:
            if self.index >= 16.5:
                return txt_res1
            elif self.index < 16.4 and self.index >= 12.5:
                return txt_res2
            elif self.index < 12.4 and self.index >= 7.5:
                return txt_res3
            elif self.index < 7.4 and self.index >= 2:
                return txt_res4
            elif self.index <= 1.9:
                return txt_res5
        if self.exp.age < 12 and self.index >= 11:
            if self.index >= 18:
                return txt_res1
            elif self.index < 17.9 and self.index >= 14:
                return txt_res2
            elif self.index < 13.9 and self.index >= 9:
                return txt_res3 
            elif self.index < 8.9 and self.index >= 3.5:
                return txt_res4
            elif self.index <= 3.4:
                return txt_res5
        if self.exp.age < 10 and self.index >= 9:
            if self.index >= 19.5:
                return txt_res1
            elif self.index < 19.4 and self.index >= 15.5:
                return txt_res2
            elif self.index < 15.4 and self.index >= 10.5:
                return txt_res3 
            elif self.index < 10.4 and self.index >= 5:
                return txt_res4
            elif self.index <= 4.9:
                return txt_res5
        if self.exp.age < 8 and self.index >= 7:
            if self.index >= 21:
                return txt_res1
            elif self.index < 20.9 and self.index >= 17:
                return txt_res2
            elif self.index < 16.9 and self.index >= 12:
                return txt_res3 
            elif self.index < 11.9 and self.index >= 6.5:
                return txt_res4
            elif self.index <= 6.4:
                return txt_res5
