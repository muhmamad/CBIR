import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QDialog, QApplication,QMainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
import os
import math

class Ui_Dialog(object):
    def setupUi(self, Dialog, images):
        Dialog.setObjectName("Dialog")
        Dialog.resize(328, 147)
        self.verticalLayout = QtWidgets.QGridLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        # print(images)
        rows = 0
        cols = 0

        for file in images:
            # print(file)
            pixmap = QtGui.QPixmap(file)
            PIXMAP = pixmap.scaled(64, 64)
            if not pixmap.isNull():
                label = QtWidgets.QLabel(pixmap=PIXMAP)
                self.verticalLayout.addWidget(label,rows,cols)
                cols+=1
                if cols==4:
                    cols = 0
                    rows += 1

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


class SearchImages(QDialog):
    def __init__(self, images, parent=None):
        super().__init__(parent)
        # print(len(images))
        self.ui = Ui_Dialog()
        self.ui.setupUi(self, images)

