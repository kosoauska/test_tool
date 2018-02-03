# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\python_pro\sata_tool.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        main_window.resize(765, 601)
        self.groupBox_3 = QtGui.QGroupBox(main_window)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 300, 381, 251))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 220, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.listWidget_2 = QtGui.QListWidget(self.groupBox_3)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 20, 361, 192))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.groupBox = QtGui.QGroupBox(main_window)
        self.groupBox.setGeometry(QtCore.QRect(420, 310, 351, 251))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.textBrowser = QtGui.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(90, 20, 231, 31))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.textBrowser_3 = QtGui.QTextBrowser(self.groupBox)
        self.textBrowser_3.setGeometry(QtCore.QRect(90, 70, 231, 31))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 101, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(240, 210, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 210, 75, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.groupBox_2 = QtGui.QGroupBox(main_window)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 30, 761, 261))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 230, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 230, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.device_list = QtGui.QTableWidget(self.groupBox_2)
        self.device_list.setGeometry(QtCore.QRect(10, 20, 721, 192))
        self.device_list.setObjectName(_fromUtf8("device_list"))
        self.device_list.setColumnCount(0)
        self.device_list.setRowCount(0)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(_translate("main_window", "Form", None))
        self.groupBox_3.setTitle(_translate("main_window", "日志输出", None))
        self.pushButton_4.setText(_translate("main_window", "保存日志", None))
        self.groupBox.setTitle(_translate("main_window", "参数配置", None))
        self.label.setText(_translate("main_window", "指令地址", None))
        self.label_3.setText(_translate("main_window", "数据内容", None))
        self.pushButton.setText(_translate("main_window", "发送指令", None))
        self.pushButton_5.setText(_translate("main_window", "选择文件", None))
        self.groupBox_2.setTitle(_translate("main_window", "设备列表", None))
        self.pushButton_2.setText(_translate("main_window", "选择设备", None))
        self.pushButton_3.setText(_translate("main_window", "关闭设备", None))

