# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\git\test_tool\sata_tool.ui'
#
# Created: Thu Feb  8 09:01:05 2018
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName(_fromUtf8("main_window"))
        main_window.resize(1202, 881)
        self.groupBox_3 = QtGui.QGroupBox(main_window)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 300, 731, 261))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.serial_log = QtGui.QPushButton(self.groupBox_3)
        self.serial_log.setGeometry(QtCore.QRect(290, 230, 75, 23))
        self.serial_log.setObjectName(_fromUtf8("serial_log"))
        self.listWidget_2 = QtGui.QListWidget(self.groupBox_3)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 20, 701, 192))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.serial_set = QtGui.QPushButton(self.groupBox_3)
        self.serial_set.setGeometry(QtCore.QRect(10, 230, 75, 23))
        self.serial_set.setObjectName(_fromUtf8("serial_set"))
        self.serial_open = QtGui.QPushButton(self.groupBox_3)
        self.serial_open.setGeometry(QtCore.QRect(110, 230, 75, 23))
        self.serial_open.setObjectName(_fromUtf8("serial_open"))
        self.serial_close = QtGui.QPushButton(self.groupBox_3)
        self.serial_close.setGeometry(QtCore.QRect(200, 230, 75, 23))
        self.serial_close.setObjectName(_fromUtf8("serial_close"))
        self.groupBox = QtGui.QGroupBox(main_window)
        self.groupBox.setGeometry(QtCore.QRect(760, 310, 421, 251))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 101, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(340, 210, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 210, 75, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(90, 20, 311, 31))
        self.lineEdit.setMaxLength(8)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 120, 311, 31))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 101, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 70, 51, 31))
        self.lineEdit_3.setText(_fromUtf8(""))
        self.lineEdit_3.setMaxLength(2)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 70, 51, 31))
        self.lineEdit_4.setText(_fromUtf8(""))
        self.lineEdit_4.setMaxLength(2)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(270, 70, 51, 31))
        self.lineEdit_5.setText(_fromUtf8(""))
        self.lineEdit_5.setMaxLength(2)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(350, 70, 51, 31))
        self.lineEdit_6.setText(_fromUtf8(""))
        self.lineEdit_6.setMaxLength(2)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.groupBox_2 = QtGui.QGroupBox(main_window)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 30, 1171, 261))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(1060, 230, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 230, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.device_list = QtGui.QTableWidget(self.groupBox_2)
        self.device_list.setGeometry(QtCore.QRect(10, 20, 1131, 192))
        self.device_list.setObjectName(_fromUtf8("device_list"))
        self.groupBox_4 = QtGui.QGroupBox(main_window)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 570, 1161, 291))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.listWidget_5 = QtGui.QListWidget(self.groupBox_4)
        self.listWidget_5.setGeometry(QtCore.QRect(10, 20, 1141, 261))
        self.listWidget_5.setObjectName(_fromUtf8("listWidget_5"))

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(_translate("main_window", "Form", None))
        self.groupBox_3.setTitle(_translate("main_window", "日志输出", None))
        self.serial_log.setText(_translate("main_window", "保存日志", None))
        self.serial_set.setText(_translate("main_window", "串口设置", None))
        self.serial_open.setText(_translate("main_window", "打开串口", None))
        self.serial_close.setText(_translate("main_window", "关闭串口", None))
        self.groupBox.setTitle(_translate("main_window", "参数配置", None))
        self.label.setText(_translate("main_window", "指令地址", None))
        self.label_3.setText(_translate("main_window", "数据内容", None))
        self.pushButton.setText(_translate("main_window", "发送指令", None))
        self.pushButton_5.setText(_translate("main_window", "选择文件", None))
        self.label_4.setText(_translate("main_window", "指令码", None))
        self.groupBox_2.setTitle(_translate("main_window", "设备列表", None))
        self.pushButton_2.setText(_translate("main_window", "选择设备", None))
        self.pushButton_3.setText(_translate("main_window", "关闭设备", None))
        self.groupBox_4.setTitle(_translate("main_window", "指令结果", None))

