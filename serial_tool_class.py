import sys
import os
import socket
import serial
from  PyQt4   import QtCore , QtGui


#private
from serial_tool import  Ui_serial
from config      import  config_class
from local     import    _fromUtf8

baud = ["4800" , "9600" , "14400" , "19200" , "38400"  , "115200"]
data = ["5" , "6" , "7" , "8"]
stop = ["1" , "1.5" , "2"]
pair = ["None" , "Odd" , "Even" , "Mark" , "Space"]
colr = ["WHITE" , "BLACK" , "RED" , "GREEN" , "ORANGE"]
pair_value = [serial.PARITY_NONE , serial.PARITY_ODD , serial.PARITY_EVEN , serial.PARITY_MARK  , serial.PARITY_SPACE]

class serial_main_windows(QtGui.QWidget ,  Ui_serial):
    def __init__(self, callback=None , parent=None):
        super(serial_main_windows , self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("serial set")
        self.serial_set = {"com" : "COM0" , "baud": "1" , "data" : "1" , "stop" : "1" , "pair" : "None" ,
                           "bc" : "WHITE" , "fc" : "BLACK" , "DTR" : "0" , "RTS" : "0" , "XON" :  "0"}
        self.serial_init()
        self.callback = callback
        self.serial_config_list.clear()
        self.serial_config_title =[u"端口", u"波特率", u"数据位数" , u"停止位" , u"校验位" , u"背景色", u"字体色" ]
        self.serial_config_list.setColumnCount(len(self.serial_config_title))
        self.serial_config_list.setHorizontalHeaderLabels(self.serial_config_title)
        self.serial_config_list.setShowGrid(False)
        self.serial_config_list.resizeRowsToContents()
        self.serial_config_list.setSelectionBehavior(QtGui.QTableWidget.SelectRows)
#TODO  load config info

# SIGNAL
        self.connect(self.ser_save , QtCore.SIGNAL('clicked()'), self.ser_save_click)
        self.connect(self.ser_load , QtCore.SIGNAL('clicked()'), self.ser_load_click)
        self.connect(self.ser_finish , QtCore.SIGNAL('clicked()'), self.ser_finish_click)
        self.connect(self.ser_cancel , QtCore.SIGNAL('clicked()'), self.ser_cancel_click)
        self.connect(self.ser_select , QtCore.SIGNAL('clicked()'), self.ser_select_click)


    def serial_init(self):
        for i in range(0 , 15):
            self.ser_port.addItem("COM" + str(i))
        self.ser_baud.addItems(baud)
        self.ser_bits.addItems(data)
        self.ser_stop.addItems(stop)
        self.ser_pair.addItems(pair)
        self.ser_bits.setCurrentIndex(3)
        for i in range(0 , 15):
            try:
                serial.Serial("COM" + str(i))
            except serial.SerialException:
                pass
            else:
                self.ser_port.setCurrentIndex(i)
                break

    def ser_save_click(self):
        self.serial_config_handler = config_class(path = r".\config\serial_conf.ini")
        self.serial_set["com"] =  self.ser_port.currentText()
        self.serial_set["baud"] = self.ser_baud.currentText()
        self.serial_set["data"] = self.ser_bits.currentText()
        self.serial_set["stop"] = self.ser_stop.currentText()
        self.serial_set["pair"] = self.ser_pair.currentText()
        self.serial_config_handler.add_section(self.serial_set["com"])
        self.serial_config_handler.set(self.serial_set["com"] , "com"  , self.serial_set["com"])
        self.serial_config_handler.set(self.serial_set["com"] , "baud" , self.serial_set["baud"])
        self.serial_config_handler.set(self.serial_set["com"] , "data" , self.serial_set["data"])
        self.serial_config_handler.set(self.serial_set["com"] , "stop" , self.serial_set["stop"])
        self.serial_config_handler.set(self.serial_set["com"] , "pair" , self.serial_set["pair"])
        self.serial_config_handler.set(self.serial_set["com"] , "bc"   , self.serial_set["bc"])
        self.serial_config_handler.set(self.serial_set["com"] , "fc"   , self.serial_set["fc"])
        self.serial_config_handler.set(self.serial_set["com"] , "DTR" , self.serial_set["DTR"])
        self.serial_config_handler.set(self.serial_set["com"] , "RTS" , self.serial_set["RTS"])
        self.serial_config_handler.set(self.serial_set["com"] , "XON" , self.serial_set["XON"])


    def ser_select_click(self):
        try:
            select_row = self.serial_config_list.currentRow()
            self.serial_set["com"] =  self.serial_config_list.item(select_row , 0).text()
            self.serial_set["baud"] = self.serial_config_list.item(select_row , 1).text()
            self.serial_set["data"] = self.serial_config_list.item(select_row , 2).text()
            self.serial_set["stop"] = self.serial_config_list.item(select_row , 3).text()
            self.serial_set["pair"] = self.serial_config_list.item(select_row , 4).text()
            self.serial_set["fc"] = self.serial_config_list.item(select_row , 5).text()
            self.serial_set["bc"] = self.serial_config_list.item(select_row , 6).text()
        except Exception as e:
            print("ser select exception: %s " % e)

        try:
            temp = self.ser_port.findText(self.serial_set["com"])
            self.ser_port.setCurrentIndex(temp)
            temp = self.ser_baud.findText(self.serial_set["baud"])
            self.ser_baud.setCurrentIndex(temp)
            temp = self.ser_bits.findText(self.serial_set["data"])
            self.ser_bits.setCurrentIndex(temp)
            temp = self.ser_stop.findText(self.serial_set["stop"])
            self.ser_stop.setCurrentIndex(temp)
            temp = self.ser_pair.findText(self.serial_set["pair"])
            self.ser_pair.setCurrentIndex(temp)
#TODO color
        except Exception as e:
            print("set index exception: %s " % e)

    def ser_load_click(self):
        self.serial_config_handler = config_class(path= r".\config\serial_conf.ini")
        section_list = self.serial_config_handler.list_section()
        section_cnt  = self.serial_config_handler.get_section_number()
        self.serial_config_list.setSelectionBehavior(QtGui.QTableWidget.SelectRows)
        self.serial_config_list.setRowCount(section_cnt)
        for i in range(0 , section_cnt):
            config_data = self.serial_config_handler.get_all(section_list[i])
            self.serial_config_list.setItem(i, 0 , QtGui.QTableWidgetItem(_fromUtf8(config_data[0][1])))
            self.serial_config_list.setItem(i, 1 , QtGui.QTableWidgetItem(_fromUtf8(config_data[1][1])))
            self.serial_config_list.setItem(i, 2 , QtGui.QTableWidgetItem(_fromUtf8(config_data[2][1])))
            self.serial_config_list.setItem(i, 3 , QtGui.QTableWidgetItem(_fromUtf8(config_data[3][1])))
            self.serial_config_list.setItem(i, 4 , QtGui.QTableWidgetItem(_fromUtf8(config_data[4][1])))
            self.serial_config_list.setItem(i, 5 , QtGui.QTableWidgetItem(_fromUtf8(config_data[5][1])))
            self.serial_config_list.setItem(i, 6 , QtGui.QTableWidgetItem(_fromUtf8(config_data[6][1])))
        self.serial_config_list.setSortingEnabled(False)
        self.serial_config_list.sortItems(0)
        self.serial_config_list.setSelectionBehavior(1)
        self.serial_config_list.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.serial_config_list.setFocusPolicy(QtCore.Qt.NoFocus)

    def ser_finish_click(self):
        self.serial_set["com"] = "COM" + str(self.ser_port.currentIndex())
        self.serial_set["baud"] = baud[self.ser_buad.currentIndex()]
        self.serial_set["data"] = data[self.ser_bits.currentIndex()]
        self.serial_set["stop"] = stop[self.ser_stop.currentIndex()]
        self.serial_set["pair"] = pair_value[self.ser_pair.currentIndex()]
        try:
            self.serial_handler = serial.Serial(self.serial_set["com"])
        except serial.SerialException:
            reply = QtGui.QMessageBox.warning(self,
                    "警告" ,
                    "串口打开失败" ,
                    QtGui.QMessageBox.Yes ,
                    )
        else:
            if  self.callback != None:
                self.callback(self.serial_set)
            self.close()

    def ser_cancel_click(self):
        pass


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mw = serial_main_windows()
    mw.show()
    sys.exit(app.exec_())
