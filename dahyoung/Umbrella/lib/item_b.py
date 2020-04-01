
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Intro_Item(QWidget):
    def __init__(self, data):
        QWidget.__init__(self, flags=Qt.Widget)
        self.layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout.setContentsMargins(QMargins())
        #확진환자
        self.patient = QtWidgets.QLabel(self)
        self.patient.setMinimumSize(20,20)
        self.patient.setObjectName("patient")
        self.patient.setMaximumSize(50,20)
        self.patient.setText(str(data[0])+" "+str(data[1]))
        #완치자
        self.perfect = QtWidgets.QLabel(self)
        self.perfect.setMinimumSize(20,20)
        self.perfect.setObjectName("perfect")
        self.perfect.setMaximumSize(100,20)
        self.perfect.setText(str(data[2])+" "+str(data[3]))
        # self.addr.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        #치료중
        self.care = QtWidgets.QLabel(self)
        self.care.setMinimumSize(50,20)
        self.care.setObjectName("care")
        self.care.setMaximumSize(150,20)
        self.care.setText(str(data[4])+" "+str(data[5]))
        #사망자
        self.dead = QtWidgets.QLabel(self)
        self.dead.setMinimumSize(50,20)
        self.dead.setObjectName("dead")
        self.dead.setMaximumSize(70,20)
        self.dead.setText(str(data[6])+" "+str(data[7]))


        self.layout.addWidget(self.patient)
        self.layout.addWidget(self.perfect)
        self.layout.addWidget(self.care)
        self.layout.addWidget(self.dead)
        self.layout.setSizeConstraint(QBoxLayout.SetDefaultConstraint)
        self.setLayout(self.layout)
