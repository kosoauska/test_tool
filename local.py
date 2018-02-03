import os
from PyQt4 import QtCore, QtGui

try:
    type(_fromUtf8)
except NameError:
    try:
        _fromUtf8 = QtCore.QString.fromUtf8
    except AttributeError:
        def _fromUtf8(s):
            return s