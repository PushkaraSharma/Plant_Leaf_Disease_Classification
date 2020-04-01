from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QPushButton, QFileDialog , QLabel, QTextEdit
#import sys
#from PyQt5.QtGui import QPixmap
from for_segmentation import image_pp_segmentation
import cv2
import predicting_image
from second_window import Ui_SecondWindow

class Ui_MainWindow(object):

    def openWindow(self,path):
        print("Inside openWindow")
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow(path)
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Main Window")
        MainWindow.resize(493, 594)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("background-color:rgb(170, 255, 127)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 100, 411, 411))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color:white;\n"
"border-radius:14px;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(50, 80, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(78, 227, 37);\n"
"color:white;\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(250, 50, 101, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("assets//plain-white-background.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 190, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(78, 227, 37);\n"
"color:white;\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 302, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:rgb(78, 227, 37);\n"
"color:white;\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 10, 81, 71))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("assets//FAVPNG_leaf-cartoon-animation-clip-art_FuqtZv9c.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 530, 161, 21))
        self.label_4.setStyleSheet("color:rgb(0, 175, 0);")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 493, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Plant Leaf Disease Classification"))
        self.label.setText(_translate("MainWindow", "Plant Leaf Disease Detection And Classification"))
        self.pushButton.setText(_translate("MainWindow", "Choose Image"))
        self.pushButton_2.setText(_translate("MainWindow", "Preprocessing and Segmentation"))
        self.pushButton_3.setText(_translate("MainWindow", "Prediction"))
        self.label_4.setText(_translate("MainWindow", "Designed by:- Pushkara & Pankaj"))

        global  path
        global check
        check = 0
        path = ''
        self.pushButton.clicked.connect(self.choose)
        self.pushButton_2.clicked.connect(self.preprocess)
        self.pushButton_3.clicked.connect(self.predict)

    def choose(self):
        global  path
        fname = QFileDialog.getOpenFileName()
        path = fname[0]
        self.label_2.setPixmap(QtGui.QPixmap(path))


    def preprocess(self):
        global check

        print(path)
        if(path==''):
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Warning')
            msg.setText('Please Choose Image')
            # msg.setIcon(QWidget.QMessageBox.Warning)
            x = msg.exec_()

        else:
            check = 1
            self.openWindow(path)
           # processed_image, clustered_image, hsv, blur, before_pp = image_pp_segmentation(path)
           # cv2.imshow('Original_Image', before_pp)
           # cv2.imshow('After Removing Noise', blur)
           # cv2.imshow('HSV ColorSpace', hsv)
           # cv2.imshow('Clustered Image', clustered_image)
           # cv2.imshow('Final Output', processed_image)

    def predict(self,):
        global  path
        global check
        if(check==1):
            processed_image, clustered_image, hsv, blur, before_pp =   image_pp_segmentation(path)
            image = cv2.resize(processed_image,(64,64))
            output = predicting_image.predict_image(image)
            check = 0
        elif(path=='') :
            output = 'Please Choose Image'
        else:
            output = 'Please Preprocess Image'

        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('Prediction')
        msg.setText(output)
        x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
