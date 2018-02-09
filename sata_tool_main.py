import sys
import os
import socket
import serial
from  PyQt4         import QtCore , QtGui



#private
from sata_tool           import Ui_main_window
from local               import _fromUtf8
from serial_tool_class   import serial_main_windows


class MainWindow(QtGui.QWidget ,  Ui_main_window):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("sata test tool")
        self.init_device_list()
        self.connect(self.serial_set ,  QtCore.SIGNAL('clicked()'),   self.ser_port_click)
        self.serial_handler = serial_main_windows(callback = self.serial_recv)



# serial set
    def ser_port_click(self):
        self.serial_handler.show()
        self.connect(self.serial_handler , QtCore.SIGNAL("transfer_father") , self , QtCore.SLOT("serial_recv"))

    def serial_recv(self , serial_content):
        print(serial_content)

    def init_device_list(self):
        from disk_info import device_info
        disk_handler = device_info().list_disk()
        self.device_list.clear()
        self.title=[u"盘符", u"卷标", u"接口" , u"容量" , u"文件系统" , u"厂商", u"序列号" ]
        self.device_list.setColumnCount(len(self.title))
        self.device_list.setHorizontalHeaderLabels(self.title)
        self.device_list.setShowGrid(False)
        self.device_list.resizeRowsToContents()
        self.device_list.setSelectionBehavior(QtGui.QTableWidget.SelectRows)
        self.device_list.setRowCount(len(disk_handler))
        print(disk_handler)
        for i in range(len(disk_handler)):
            self.device_list.setItem(i, 0 , QtGui.QTableWidgetItem(_fromUtf8(disk_handler[i][0])))
            self.device_list.setItem(i, 1 , QtGui.QTableWidgetItem(_fromUtf8(disk_handler[i][1])))
            self.device_list.setItem(i, 2 , QtGui.QTableWidgetItem(_fromUtf8(disk_handler[i][2])))
            self.device_list.setItem(i, 3 , QtGui.QTableWidgetItem(str(disk_handler[i][3]) + ' GB'))
            self.device_list.setItem(i, 4 , QtGui.QTableWidgetItem(_fromUtf8(disk_handler[i][4])))
            self.device_list.setItem(i, 5 , QtGui.QTableWidgetItem(_fromUtf8(disk_handler[i][5])))
        self.device_list.setSortingEnabled(False)
        self.device_list.sortItems(0)
        self.device_list.setSelectionBehavior(1)
        self.device_list.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.device_list.setFocusPolicy(QtCore.Qt.NoFocus)
#TODO



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
