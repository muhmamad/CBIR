from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from searchImage import SearchImages
import os
from CBIR import MNISTImage, searchImages

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(576, 600)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 40, 521, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.loadButton = QtWidgets.QPushButton(Form)
        self.loadButton.setGeometry(QtCore.QRect(180, 180, 221, 81))
        self.loadButton.setObjectName("loadButton")
        self.searchButton = QtWidgets.QPushButton(Form)
        self.searchButton.setGeometry(QtCore.QRect(180, 300, 221, 81))
        self.searchButton.setObjectName("searchButton")
        self.image = QtWidgets.QLabel(Form)
        self.image.setGeometry(QtCore.QRect(260, 380, 250, 221))
        self.image.setObjectName("image")

        self.loadButton.clicked.connect(self.loadImage)
        self.searchButton.clicked.connect(self.searchImage)

        self.imagePath = None

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        path_0 = "./MNIST_DS/0"
        path_1 = "./MNIST_DS/1"
        path_2 = "./MNIST_DS/2"
        path_3 = "./MNIST_DS/3"
        path_4 = "./MNIST_DS/4"
        path_5 = "./MNIST_DS/5"
        path_6 = "./MNIST_DS/6"
        path_7 = "./MNIST_DS/7"
        path_8 = "./MNIST_DS/8"
        path_9 = "./MNIST_DS/9"
        paths = {"0":path_0, "1":path_1, "2":path_2,"3":path_3, 
                "4":path_4, "5":path_5, "6":path_6, "7":path_7, 
                "8":path_8, "9":path_9}
        
        self.imageDataset = {}
        # imagePaths = []
        for k,v in paths.items():
            for img in os.listdir(v):
                x = os.path.join(v, img)
                # imagePaths.append(x)
                self.imageDataset[x] = MNISTImage(x, k)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Content-Based Information Retrieval"))
        self.loadButton.setText(_translate("Form", "Load Image"))
        self.searchButton.setText(_translate("Form", "Search Image"))
        self.image.setText(_translate("Form", ""))

    def loadImage(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(None,'Single File','',"Image files (*.jpg *.png)")
        filePath = fileName[0]
        pixmap = QtGui.QPixmap(filePath)
        PIXMAP = pixmap.scaled(64, 64)

        self.imagePath = filePath
        self.image.setPixmap(PIXMAP)

    def searchImage(self):
        image = MNISTImage(self.imagePath)
        x = searchImages(list(self.imageDataset.values()), image)
        # print(len(x))
        self.w = SearchImages(x)
        self.w.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    cbir = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(cbir)
    cbir.show()
    sys.exit(app.exec_())
