
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Item(QWidget):
    def __init__(self, name, addr, remain_stat):
        QWidget.__init__(self, flags=Qt.Widget)
        self.layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout.setContentsMargins(QMargins())
        self.name = QtWidgets.QLabel(self)
        self.name.setMinimumSize(80,20)
        self.name.setObjectName("name")
        self.name.setMaximumSize(80,20)
        self.name.setText(name)

        self.addr = QtWidgets.QLabel(self)
        self.addr.setMinimumSize(170,20)
        self.addr.setObjectName("addr")
        self.addr.setMaximumSize(170,20)
        self.addr.setText(addr)

        self.remain_stat = QtWidgets.QLabel(self)
        self.remain_stat.setMinimumSize(50,20)
        self.remain_stat.setObjectName("remain_stat")
        self.remain_stat.setMaximumSize(50,20)
        self.remain_stat.setText(remain_stat)



        self.pb = QPushButton("X")
        self.pb.setMinimumSize(30,20)
        self.pb.setMaximumSize(30,20)
        self.layout.addWidget(self.name)
        self.layout.addWidget(self.addr)
        self.layout.addWidget(self.remain_stat)
        self.layout.setSizeConstraint(QBoxLayout.SetDefaultConstraint)
        self.setLayout(self.layout)
