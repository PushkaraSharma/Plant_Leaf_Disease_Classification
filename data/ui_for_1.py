# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_for_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QPushButton, QFileDialog , QLabel, QTextEdit
import sys
from PyQt5.QtGui import QPixmap
from for_segmentation import image_pp_segmentation
import cv2
import predicting_image

class Ui_MainWindow(object):



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 600)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 120, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 220, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 340, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 30, 351, 41))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Choose Image"))
        self.pushButton_2.setText(_translate("MainWindow", "Image Preprocessing and Segmentation"))
        self.pushButton_3.setText(_translate("MainWindow", "Prediction"))
        self.label.setText(_translate("MainWindow", "Plant Leaf Disease Detection and Classification"))

        self.pushButton.clicked.connect(self.choose)
        self.pushButton_2.clicked.connect(self.preprocess)
        self.pushButton_3.clicked.connect(self.predict)

    def choose(self):
        global  path
        fname = QFileDialog.getOpenFileName()
        path = fname[0]
        pixmap = QPixmap(path)
        self.label.setPixmap(QPixmap(pixmap))
        self.resize(pixmap.width(),pixmap.height())
        #print(path)


    def preprocess(self):
        global check
        check = 1
        print(path)
        processed_image,clustered_image,hsv,blur,before_pp = image_pp_segmentation(path)
        cv2.imshow('Original_Image', before_pp)
        cv2.imshow('After Removing Noise', blur)
        cv2.imshow('HSV ColorSpace', hsv)
        cv2.imshow('Clustered Image', clustered_image)
        cv2.imshow('Final Output', processed_image )

    def predict(self,):
        global check
        if(check==1):
            processed_image, clustered_image, hsv, blur, before_pp =   image_pp_segmentation(path)
            image = cv2.resize(processed_image,(64,64))
            output = predicting_image.predict_image(image)
            check = 0
        else:
            output = 'Please Preprocess'

        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('Predicted Class')
        msg.setText(output)
        msg.setIcon(QWidget.QMessageBox.Warning)
        x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
