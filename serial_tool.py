# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\git\sata_test_tool\serial_tool.ui'
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

class Ui_serial(object):
    def setupUi(self, serial):
        serial.setObjectName(_fromUtf8("serial"))
        serial.resize(522, 372)
        self.groupBox = QtGui.QGroupBox(serial)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 251, 331))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.ser_port = QtGui.QComboBox(self.groupBox)
        self.ser_port.setGeometry(QtCore.QRect(110, 50, 91, 20))
        self.ser_port.setObjectName(_fromUtf8("ser_port"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 50, 24, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.ser_buad = QtGui.QComboBox(self.groupBox)
        self.ser_buad.setGeometry(QtCore.QRect(110, 100, 91, 20))
        self.ser_buad.setObjectName(_fromUtf8("ser_buad"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 36, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.ser_bits = QtGui.QComboBox(self.groupBox)
        self.ser_bits.setGeometry(QtCore.QRect(110, 150, 91, 20))
        self.ser_bits.setObjectName(_fromUtf8("ser_bits"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 48, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.ser_stop = QtGui.QComboBox(self.groupBox)
        self.ser_stop.setGeometry(QtCore.QRect(110, 200, 91, 20))
        self.ser_stop.setObjectName(_fromUtf8("ser_stop"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 36, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(30, 250, 36, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.ser_pari = QtGui.QComboBox(self.groupBox)
        self.ser_pari.setGeometry(QtCore.QRect(110, 250, 90, 20))
        self.ser_pari.setObjectName(_fromUtf8("ser_pari"))
        self.groupBox_2 = QtGui.QGroupBox(serial)
        self.groupBox_2.setGeometry(QtCore.QRect(310, 20, 181, 91))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.ser_dtr = QtGui.QCheckBox(self.groupBox_2)
        self.ser_dtr.setGeometry(QtCore.QRect(20, 20, 111, 16))
        self.ser_dtr.setObjectName(_fromUtf8("ser_dtr"))
        self.ser_rts = QtGui.QCheckBox(self.groupBox_2)
        self.ser_rts.setGeometry(QtCore.QRect(20, 40, 111, 16))
        self.ser_rts.setObjectName(_fromUtf8("ser_rts"))
        self.ser_xon = QtGui.QCheckBox(self.groupBox_2)
        self.ser_xon.setGeometry(QtCore.QRect(20, 60, 111, 16))
        self.ser_xon.setObjectName(_fromUtf8("ser_xon"))
        self.groupBox_3 = QtGui.QGroupBox(serial)
        self.groupBox_3.setGeometry(QtCore.QRect(310, 130, 181, 101))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 61, 36, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.set_back = QtGui.QComboBox(self.groupBox_3)
        self.set_back.setGeometry(QtCore.QRect(71, 61, 81, 20))
        self.set_back.setObjectName(_fromUtf8("set_back"))
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(11, 21, 48, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.ser_font = QtGui.QComboBox(self.groupBox_3)
        self.ser_font.setGeometry(QtCore.QRect(71, 21, 81, 20))
        self.ser_font.setObjectName(_fromUtf8("ser_font"))
        self.groupBox_4 = QtGui.QGroupBox(serial)
        self.groupBox_4.setGeometry(QtCore.QRect(310, 240, 181, 111))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.ser_cancel = QtGui.QPushButton(self.groupBox_4)
        self.ser_cancel.setGeometry(QtCore.QRect(10, 70, 75, 23))
        self.ser_cancel.setObjectName(_fromUtf8("ser_cancel"))
        self.ser_load = QtGui.QPushButton(self.groupBox_4)
        self.ser_load.setGeometry(QtCore.QRect(100, 30, 75, 23))
        self.ser_load.setObjectName(_fromUtf8("ser_load"))
        self.ser_save = QtGui.QPushButton(self.groupBox_4)
        self.ser_save.setGeometry(QtCore.QRect(10, 30, 75, 23))
        self.ser_save.setObjectName(_fromUtf8("ser_save"))
        self.ser_finish = QtGui.QPushButton(self.groupBox_4)
        self.ser_finish.setGeometry(QtCore.QRect(100, 70, 75, 23))
        self.ser_finish.setObjectName(_fromUtf8("ser_finish"))

        self.retranslateUi(serial)
        QtCore.QMetaObject.connectSlotsByName(serial)

    def retranslateUi(self, serial):
        serial.setWindowTitle(_translate("serial", "串口配置", None))
        self.groupBox.setTitle(_translate("serial", "基本设置", None))
        self.label.setText(_translate("serial", "端口", None))
        self.label_2.setText(_translate("serial", "波特率", None))
        self.label_3.setText(_translate("serial", "数据位数", None))
        self.label_4.setText(_translate("serial", "停止位", None))
        self.label_7.setText(_translate("serial", "校验位", None))
        self.groupBox_2.setTitle(_translate("serial", "流控制", None))
        self.ser_dtr.setText(_translate("serial", "DTR/DSR", None))
        self.ser_rts.setText(_translate("serial", "RTS/CTS", None))
        self.ser_xon.setText(_translate("serial", "XON/XOFF", None))
        self.groupBox_3.setTitle(_translate("serial", "色彩选择", None))
        self.label_6.setText(_translate("serial", "背景色", None))
        self.label_5.setText(_translate("serial", "字体色彩", None))
        self.ser_cancel.setText(_translate("serial", "取消", None))
        self.ser_load.setText(_translate("serial", "读取设置", None))
        self.ser_save.setText(_translate("serial", "保存设置", None))
        self.ser_finish.setText(_translate("serial", "完成", None))

