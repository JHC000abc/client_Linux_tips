# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author  : v_jiaohaicheng@baidu.com
@des     :

"""
import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt
from gui.ctrl.ctrl_start import StartWin
from qt_material import apply_stylesheet



if __name__ == "__main__":
    root_path = os.getcwd()
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    try:
        apply_stylesheet(app, theme="dark_teal.xml")
    except:
        pass
    Form = StartWin()
    Form.show()
    sys.exit(app.exec_())