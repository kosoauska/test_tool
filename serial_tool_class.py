import sys
import os
import socket
import serial
from  PyQt4   import QtCore , QtGui


#private
from serial_tool import Ui_serial
from local     import _fromUtf8
bund = ["4800" , "9600" , "14400" , "19200" ,"38400"  , "115200"]
data = ["5" , "6" , "7" , "8"]
stop = ["1" , "1.5" , "2"]
pair = ["None" , "Odd" , "Even" , "Mark" , "Space"]
pair_value = [serial.PARITY_NONE , serial.PARITY_ODD , serial.PARITY_EVEN , serial.PARITY_MARK  , serial.PARITY_SPACE]

class serial_main_windows(QtGui.QWidget ,  Ui_serial):
    def __init__(self, parent=None):
        super(serial_main_windows , self).__init__(parent)
        self.setupUi(self)
        self.serial_set={"com" : "COM0" , "boud": "38400" , "data" : "8" , "stop" : "1" , "pair" : "None"}
        self.serial_init()
        self.connect(self.ser_save , QtCore.SIGNAL('clicked()'), self.ser_save_click)
        self.connect(self.ser_load , QtCore.SIGNAL('clicked()'), self.ser_load_click)
        self.connect(self.ser_finish , QtCore.SIGNAL('clicked()'), self.ser_finish_click)
        self.connect(self.ser_cancel , QtCore.SIGNAL('clicked()'), self.ser_cancel_click)

    def serial_init(self):
        for i in range(0 , 15):
            self.ser_port.addItem("COM" + str(i))
        self.ser_buad.addItems(bund)
        self.ser_bits.addItems(data)
        self.ser_stop.addItems(stop)
        self.ser_pari.addItems(pair)
        self.ser_bits.setCurrentIndex(3)
        for i in range(0 , 15):
            try:
                serial.Serial("COM" + str(i))
            except serial.SerialException:
                pass
            else:
                self.ser_port.setCurrentIndex(i)
                serial.Serial.close()
                break

    def ser_save_click(self):
        pass

    def ser_load_click(self):

        pass

    def ser_finish_click(self):
        self.serial_set["com"] = "COM" + str(self.ser_port.currentIndex())
        self.serial_set["boud"] = bund[self.ser_buad.currentIndex()]
        self.serial_set["data"] = data[self.ser_bits.currentIndex()]
        self.serial_set["stop"] = stop[self.ser_stop.currentIndex()]
        self.serial_set["pair"] = pair_value[self.ser_pari.currentIndex()]
        print(self.serial_set)
        try:
            serial.Serial(self.serial_set["com"])
        except serial.SerialException:
            reply = QtGui.QMessageBox.warning(self,
                    "警告" ,
                    "串口打开失败" ,
                    QtGui.QMessageBox.Yes ,
                    )

    def ser_cancel_click(self):
        pass




if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mw = serial_main_windows()
    mw.show()
    sys.exit(app.exec_())
