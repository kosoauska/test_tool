
import sys
import os
import socket
from  PyQt4   import QtCore , QtGui


#private
from sata_tool import Ui_main_window
from local     import _fromUtf8



class MainWindow(QtGui.QWidget ,  Ui_main_window):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.init_device_list()

    def init_device_list(self):
        from disk_info import device_info
        disk_handler = device_info().list_disk()
        self.device_list.clear()
        self.title=[u"盘符", u"卷标", u"接口",u"工作模式", u"厂商", u"PID/VID" , u"序列号"]
        self.device_list.setColumnCount(len(self.title))
        self.device_list.setHorizontalHeaderLabels(self.title)
        self.device_list.setShowGrid(False)
        self.device_list.resizeRowsToContents()
        self.device_list.setSelectionBehavior(QtGui.QTableWidget.SelectRows)
        self.device_list.setRowCount(len(disk_handler))
        print(disk_handler)
        print(disk_handler[0][0])
        for i in range(len(disk_handler)):
            #            disk = str(self.disk_info[0][0][0])
            #            if disk == "C":
            #                del self.disk_info[0]
            #                continue
            self.device_list.setItem(i, 0 , QtGui.QTableWidgetItem(str(disk_handler[i][0])))
            self.device_list.setItem(i, 1 , QtGui.QTableWidgetItem(_fromUtf8(disk_handler[i][1])))
            self.device_list.setItem(i, 2 , QtGui.QTableWidgetItem(_fromUtf8(disk_handler[i][3])))
            self.device_list.setItem(i, 3 , QtGui.QTableWidgetItem(_fromUtf8(disk_handler[i][5])))
            self.device_list.setItem(i, 4 , QtGui.QTableWidgetItem(_fromUtf8(disk_handler[i][2])))
        self.device_list.setSortingEnabled(False)
        self.device_list.sortItems(0)
        self.device_list.setSelectionBehavior(1)
        self.device_list.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.device_list.setFocusPolicy(QtCore.Qt.NoFocus)

    def  main_config(self):
        pass

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())