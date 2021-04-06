# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'everytime.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import json_reader


class Everytime(object):

    def __init__(self):
        super().__init__() #object class 의 생성자 함수 상속을 해야 gui가 제대로 작동할 수 있습니다.
        self.prof = None
        self.lect_name = None
        self.score = None
        self.assign = None
        self.team = None
        self.grade = None
        self.attendance = None
        self.test = None
        self.lecture_list1 = json_reader.Lecture_list(self.prof, self.lect_name, self.score, self.assign, self.team,
                                                      self.grade, self.attendance, self.test)


    def setupUi(self, Form):#gui를 띄울 시 창을 구성하는 모든 정보가 담겨 있습니다. 단, 각 버튼에 대한 이름은 retranslateUi에서 다시 바꿔 줍니다
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.setEnabled(True)
        Form.resize(1405, 627)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(700, 500))
        Form.setMaximumSize(QtCore.QSize(1500, 950))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        Form.setPalette(palette)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(30, 30, 20, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 30)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setMinimumSize(QtCore.QSize(130, 30))
        self.label_18.setMaximumSize(QtCore.QSize(200, 70))
        self.label_18.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_18.setLineWidth(1)
        self.label_18.setText("")
        self.label_18.setTextFormat(QtCore.Qt.AutoText)
        self.label_18.setPixmap(QtGui.QPixmap("/logo/sgtime30.png"))
        self.label_18.setScaledContents(False)
        self.label_18.setWordWrap(False)
        self.label_18.setIndent(-1)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_10.addWidget(self.label_18)
        self.horizontalLayout_4.addLayout(self.verticalLayout_10)
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_4.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        spacerItem2 = QtWidgets.QSpacerItem(20, 14, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_11.addItem(spacerItem2)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_2.setMaximumSize(QtCore.QSize(300, 50))

        # update 버튼 함수 연결

        print(type(self.lecture_list1))
        self.pushButton_2.clicked.connect(self.update)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(211, 211, 211))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(211, 211, 211))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(211, 211, 211))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(211, 211, 211))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(211, 211, 211))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(211, 211, 211))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(211, 211, 211))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(211, 211, 211))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(211, 211, 211))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("a스피드")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white,stop: 1\n"
"lightgray);\n"
"    border: 1px solid lightgray;\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_11.addWidget(self.pushButton_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, -1, 10, -1)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_17 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMinimumSize(QtCore.QSize(60, 35))
        self.label_17.setMaximumSize(QtCore.QSize(60, 35))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어OTF Bold")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_8.addWidget(self.label_17)
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어OTF Light")
        font.setPointSize(11)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 8px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_8.addWidget(self.lineEdit_3)
        self.lineEdit_3.textChanged.connect(self.inputProfessor)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(60, 35))
        self.label_13.setMaximumSize(QtCore.QSize(60, 35))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어OTF Bold")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_14.addWidget(self.label_13)
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어OTF Light")
        font.setPointSize(11)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 8px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_14.addWidget(self.lineEdit_4)
        self.lineEdit_4.textChanged.connect(self.inputLectureName)
        self.verticalLayout_6.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_15 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QtCore.QSize(60, 35))
        self.label_15.setMaximumSize(QtCore.QSize(60, 35))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어OTF Bold")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.comboBox_12 = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.comboBox_12.sizePolicy().hasHeightForWidth())
        self.comboBox_12.setSizePolicy(sizePolicy)
        self.comboBox_12.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_12.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어,Lucida,Verdana,sans-serif")
        font.setPointSize(10)
        self.comboBox_12.setFont(font)
        self.comboBox_12.setStyleSheet("QComboBox {\n"
"font-family:  \"나눔스퀘어\", Lucida, Verdana, sans-serif;\n"
"border: 1px solid #D3D3D3;\n"
"border-radius: 8px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #EEEEEE, stop: 1 #FFFFFF);\n"
"color: #333;\n"
"font-size: 10pt;\n"
"padding: 8px;\n"
"}\n"
" \n"
"QComboBox:on {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #D5D5D5, stop: 1 #EEEEEE);\n"
" }\n"
" \n"
"QComboBox::drop-down {\n"
"border: 0px solid #D3D3D3;\n"
"border-radius: 8px;\n"
" }\n"
"\n"
"")
        self.comboBox_12.setObjectName("comboBox_12")#12. 총점  9. 과제  7. 팀플  11. 학점  8. 출결
        self.comboBox_12.addItem("")
        self.comboBox_12.setItemText(0, "")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.currentIndexChanged.connect(self.inputScore)
        self.horizontalLayout_2.addWidget(self.comboBox_12)  #12. 총점  9. 과제  7. 팀플  11. 학점  8. 출결
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_14 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(60, 35))
        self.label_14.setMaximumSize(QtCore.QSize(60, 35))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어OTF Bold")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_9.addWidget(self.label_14)
        self.comboBox_9 = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.comboBox_9.sizePolicy().hasHeightForWidth())
        self.comboBox_9.setSizePolicy(sizePolicy)
        self.comboBox_9.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_9.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어,Lucida,Verdana,sans-serif")
        font.setPointSize(10)
        self.comboBox_9.setFont(font)
        self.comboBox_9.setStyleSheet("QComboBox {\n"
"font-family:  \"나눔스퀘어\", Lucida, Verdana, sans-serif;\n"
"border: 1px solid #D3D3D3;\n"
"border-radius: 8px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #EEEEEE, stop: 1 #FFFFFF);\n"
"color: #333;\n"
"font-size: 10pt;\n"
"padding: 8px;\n"
"}\n"
" \n"
"QComboBox:on {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #D5D5D5, stop: 1 #EEEEEE);\n"
" }\n"
" \n"
"QComboBox::drop-down {\n"
"border: 0px solid #D3D3D3;\n"
"border-radius: 8px;\n"
" }\n"
"\n"
"")
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.setItemText(0, "")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.currentIndexChanged.connect(self.inputAssignment)#12. 총점  9. 과제  7. 팀플  11. 학점  8. 출결
        self.horizontalLayout_9.addWidget(self.comboBox_9)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_10 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(60, 35))
        self.label_10.setMaximumSize(QtCore.QSize(60, 35))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어OTF Bold")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_15.addWidget(self.label_10)
        self.comboBox_7 = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.comboBox_7.sizePolicy().hasHeightForWidth())
        self.comboBox_7.setSizePolicy(sizePolicy)
        self.comboBox_7.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_7.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어,Lucida,Verdana,sans-serif")
        font.setPointSize(10)
        self.comboBox_7.setFont(font)
        self.comboBox_7.setStyleSheet("QComboBox {\n"
"font-family:  \"나눔스퀘어\", Lucida, Verdana, sans-serif;\n"
"border: 1px solid #D3D3D3;\n"
"border-radius: 8px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #EEEEEE, stop: 1 #FFFFFF);\n"
"color: #333;\n"
"font-size: 10pt;\n"
"padding: 8px;\n"
"}\n"
" \n"
"QComboBox:on {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #D5D5D5, stop: 1 #EEEEEE);\n"
" }\n"
" \n"
"QComboBox::drop-down {\n"
"border: 0px solid #D3D3D3;\n"
"border-radius: 8px;\n"
" }\n"
"\n"
"")
        self.comboBox_7.setObjectName("comboBox_7")#12. 총점  9. 과제  7. 팀플  11. 학점  8. 출결
        self.comboBox_7.addItem("")
        self.comboBox_7.setItemText(0, "")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.currentIndexChanged.connect(self.inputTeam)
        self.horizontalLayout_15.addWidget(self.comboBox_7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_16 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QtCore.QSize(60, 35))
        self.label_16.setMaximumSize(QtCore.QSize(60, 35))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어OTF Bold")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_6.addWidget(self.label_16)
        self.comboBox_11 = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.comboBox_11.sizePolicy().hasHeightForWidth())
        self.comboBox_11.setSizePolicy(sizePolicy)
        self.comboBox_11.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_11.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어,Lucida,Verdana,sans-serif")
        font.setPointSize(10)
        self.comboBox_11.setFont(font)
        self.comboBox_11.setStyleSheet("QComboBox {\n"
"font-family:  \"나눔스퀘어\", Lucida, Verdana, sans-serif;\n"
"border: 1px solid #D3D3D3;\n"
"border-radius: 8px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #EEEEEE, stop: 1 #FFFFFF);\n"
"color: #333;\n"
"font-size: 10pt;\n"
"padding: 8px;\n"
"}\n"
" \n"
"QComboBox:on {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #D5D5D5, stop: 1 #EEEEEE);\n"
" }\n"
" \n"
"QComboBox::drop-down {\n"
"border: 0px solid #D3D3D3;\n"
"border-radius: 8px;\n"
" }\n"
"\n"
"")
        self.comboBox_11.setObjectName("comboBox_11")#12. 총점  9. 과제  7. 팀플  11. 학점  8. 출결
        self.comboBox_11.addItem("")
        self.comboBox_11.setItemText(0, "")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.currentIndexChanged.connect(self.inputGrade)
        self.horizontalLayout_6.addWidget(self.comboBox_11)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_12 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(60, 35))
        self.label_12.setMaximumSize(QtCore.QSize(60, 35))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어OTF Bold")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        self.comboBox_8 = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.comboBox_8.sizePolicy().hasHeightForWidth())
        self.comboBox_8.setSizePolicy(sizePolicy)
        self.comboBox_8.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_8.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어,Lucida,Verdana,sans-serif")
        font.setPointSize(10)
        self.comboBox_8.setFont(font)
        self.comboBox_8.setStyleSheet("QComboBox {\n"
"font-family:  \"나눔스퀘어\", Lucida, Verdana, sans-serif;\n"
"border: 1px solid #D3D3D3;\n"
"border-radius: 8px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #EEEEEE, stop: 1 #FFFFFF);\n"
"color: #333;\n"
"font-size: 10pt;\n"
"padding: 8px;\n"
"}\n"
" \n"
"QComboBox:on {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #D5D5D5, stop: 1 #EEEEEE);\n"
" }\n"
" \n"
"QComboBox::drop-down {\n"
"border: 0px solid #D3D3D3;\n"
"border-radius: 8px;\n"
" }\n"
"\n"
"")
        self.comboBox_8.setObjectName("comboBox_8")#12. 총점  9. 과제  7. 팀플  11. 학점  8. 출결
        self.comboBox_8.addItem("")
        self.comboBox_8.setItemText(0, "")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.currentIndexChanged.connect(self.inputAttendance)
        self.horizontalLayout_10.addWidget(self.comboBox_8)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_11 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(60, 35))
        self.label_11.setMaximumSize(QtCore.QSize(60, 35))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어OTF Bold")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_16.addWidget(self.label_11)
        self.comboBox_10 = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.comboBox_10.sizePolicy().hasHeightForWidth())
        self.comboBox_10.setSizePolicy(sizePolicy)
        self.comboBox_10.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_10.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어,Lucida,Verdana,sans-serif")
        font.setPointSize(10)
        self.comboBox_10.setFont(font)
        self.comboBox_10.setStyleSheet("QComboBox {\n"
"font-family:  \"나눔스퀘어\", Lucida, Verdana, sans-serif;\n"
"border: 1px solid #D3D3D3;\n"
"border-radius: 8px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #EEEEEE, stop: 1 #FFFFFF);\n"
"color: #333;\n"
"font-size: 10pt;\n"
"padding: 8px;\n"
"}\n"
" \n"
"QComboBox:on {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #D5D5D5, stop: 1 #EEEEEE);\n"
" }\n"
" \n"
"QComboBox::drop-down {\n"
"border: 0px solid #D3D3D3;\n"
"border-radius: 8px;\n"
" }\n"
"\n"
"")
        self.comboBox_10.setObjectName("comboBox_10")#12. 총점  9. 과제  7. 팀플  11. 학점  8. 출결
        self.comboBox_10.addItem("")
        self.comboBox_10.setItemText(0, "")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.currentIndexChanged.connect(self.inputTest)
        self.horizontalLayout_16.addWidget(self.comboBox_10)
        self.verticalLayout_6.addLayout(self.horizontalLayout_16)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem4 = QtWidgets.QSpacerItem(160, 25, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(70, 35))
        self.pushButton_3.setMaximumSize(QtCore.QSize(70, 35))
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white,stop: 1\n"
"lightgray);\n"
"    border: 0px solid lightgray;\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_7.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(self.sort)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout_9.addWidget(self.tableWidget)
        spacerItem6 = QtWidgets.QSpacerItem(1500, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_9.addItem(spacerItem6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "도와줘! 수강타임"))
        self.pushButton_2.setText(_translate("Form", "UPDATE!"))
        self.label_17.setText(_translate("Form", "교수명"))
        self.label_13.setText(_translate("Form", "강의명"))
        self.label_15.setText(_translate("Form", "최소 총점"))
        self.comboBox_12.setItemText(1, _translate("Form", "1")) #12. 총점  9. 과제  7. 팀플  11. 학점  8. 출결
        self.comboBox_12.setItemText(2, _translate("Form", "2"))
        self.comboBox_12.setItemText(3, _translate("Form", "3"))
        self.comboBox_12.setItemText(4, _translate("Form", "4"))
        self.comboBox_12.setItemText(5, _translate("Form", "5"))
        self.label_14.setText(_translate("Form", "과제"))
        self.comboBox_9.setItemText(1, _translate("Form", "없음"))
        self.comboBox_9.setItemText(2, _translate("Form", "보통"))
        self.comboBox_9.setItemText(3, _translate("Form", "많음"))
        self.label_10.setText(_translate("Form", "팀플"))
        self.comboBox_7.setItemText(1, _translate("Form", "많음"))
        self.comboBox_7.setItemText(2, _translate("Form", "보통"))
        self.comboBox_7.setItemText(3, _translate("Form", "없음"))
        self.label_16.setText(_translate("Form", "학점"))
        self.comboBox_11.setItemText(1, _translate("Form", "학점느님"))
        self.comboBox_11.setItemText(2, _translate("Form", "비율 채워줌"))
        self.comboBox_11.setItemText(3, _translate("Form", "매우 깐깐함"))
        self.comboBox_11.setItemText(4, _translate("Form", "F 폭격기"))
        self.label_12.setText(_translate("Form", "출결"))
        self.comboBox_8.setItemText(1, _translate("Form", "혼용"))
        self.comboBox_8.setItemText(2, _translate("Form", "직접호명"))
        self.comboBox_8.setItemText(3, _translate("Form", "지정좌석"))
        self.comboBox_8.setItemText(4, _translate("Form", "전자출결"))
        self.comboBox_8.setItemText(5, _translate("Form", "반영안함"))
        self.label_11.setText(_translate("Form", "시험"))
        self.comboBox_10.setItemText(1, _translate("Form", "네 번 이상"))
        self.comboBox_10.setItemText(2, _translate("Form", "세 번"))
        self.comboBox_10.setItemText(3, _translate("Form", "두 번"))
        self.comboBox_10.setItemText(4, _translate("Form", "한 번"))
        self.comboBox_10.setItemText(5, _translate("Form", "없음"))
        self.pushButton_3.setText(_translate("Form", "검  색"))

    # 각 조건을 입력 받을 때마다 변수의 값을 변경해줍니다.
    def inputProfessor(self):
        self.prof = self.lineEdit_3.text()
    def inputLectureName(self):
        self.lect_name = self.lineEdit_4.text()
    def inputScore(self):
        self.score = self.comboBox_12.currentText()
    def inputAssignment(self):
        self.assign = self.comboBox_9.currentText()
    def inputTeam(self):
        self.team = self.comboBox_7.currentText()
    def inputGrade(self):
        self.grade = self.comboBox_11.currentText()
    def inputAttendance(self):
        self.attendance = self.comboBox_8.currentText()
    def inputTest(self):
        self.test = self.comboBox_10.currentText()

    # Host.py가 만들어준 list.json을 불러옵니다.
    def update(self):
        self.lecture_list1.update()

    def sort(self):

        self.lecture_list1.search(self.prof, self.lect_name, self.score, self.assign, self.team, self.grade, self.attendance, self.test)
        #try:

        self.result = self.lecture_list1.result_list

        #except:
        #    print("검색 결과가 없습니다.")

        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(len(self.result)-1)
        column_headers = ['교수','과목명','평점','과제','팀플','학점','출석','시험횟수']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        k = 1

        #엑셀 형태로 결과 리스트를 보여줍니다.
        if len(self.result) == 1:
            self.resultLine = self.result[0]# 결과가 안나올 시 보여주는 상황을 대비한 값입니다 전부 None값을 받습니다
            self.tableWidget.setItem(k - 1, 0, QTableWidgetItem(self.resultLine['prof']))
            self.tableWidget.setItem(k - 1, 1, QTableWidgetItem(self.resultLine['lecture_name']))
            self.tableWidget.setItem(k - 1, 2, QTableWidgetItem(self.resultLine['score']))
            self.tableWidget.setItem(k - 1, 3, QTableWidgetItem(self.resultLine['assign']))
            self.tableWidget.setItem(k - 1, 4, QTableWidgetItem(self.resultLine['team']))
            self.tableWidget.setItem(k - 1, 5, QTableWidgetItem(self.resultLine['grade']))
            self.tableWidget.setItem(k - 1, 6, QTableWidgetItem(self.resultLine['attendance']))
            self.tableWidget.setItem(k - 1, 7, QTableWidgetItem(self.resultLine['test_count']))
        else:
            while k < len(self.result):#조건을 만족할 시 만족하는 결과 리스트를 출력합니다
                self.tableWidget.setItem(k - 1, 0, QTableWidgetItem(self.result[k]['prof']))
                self.tableWidget.setItem(k - 1, 1, QTableWidgetItem(self.result[k]['lecture_name']))
                self.tableWidget.setItem(k - 1, 2, QTableWidgetItem(self.result[k]['score']))
                self.tableWidget.setItem(k - 1, 3, QTableWidgetItem(self.result[k]['assign']))
                self.tableWidget.setItem(k - 1, 4, QTableWidgetItem(self.result[k]['team']))
                self.tableWidget.setItem(k - 1, 5, QTableWidgetItem(self.result[k]['grade']))
                self.tableWidget.setItem(k - 1, 6, QTableWidgetItem(self.result[k]['attendance']))
                self.tableWidget.setItem(k - 1, 7, QTableWidgetItem(self.result[k]['test_count']))
                k = k + 1


'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Everytime()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
'''