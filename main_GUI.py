# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from db_gui import Db_Window
from main_API import get_audio, main, main_write



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(616, 456)
        MainWindow.setMinimumSize(QtCore.QSize(616, 456))
        MainWindow.setMaximumSize(QtCore.QSize(616, 456))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("main_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.user_display = QtWidgets.QTextEdit(self.centralwidget)
        self.user_display.setGeometry(QtCore.QRect(20, 40, 471, 301))
        self.user_display.setReadOnly(True)
        self.user_display.setObjectName("user_display")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 55, 16))
        self.label_2.setObjectName("label_2")
        self.user_input = QtWidgets.QLineEdit(self.centralwidget)
        self.user_input.setGeometry(QtCore.QRect(20, 380, 471, 31))
        self.user_input.setObjectName("user_input")
        self.user_input.setPlaceholderText("Input your text here.")
        self.sendBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sendBtn.setGeometry(QtCore.QRect(510, 370, 91, 51))
        self.sendBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("send.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sendBtn.setIcon(icon1)
        self.sendBtn.setIconSize(QtCore.QSize(40, 40))
        self.sendBtn.setObjectName("sendBtn")

        #add signal to checkbox
        self.sendBtn.clicked.connect(self.changeContent)
        self.sendBtn.setToolTip("Send")
        self.sendBtnShortcut = QtWidgets.QShortcut(
                            QtGui.QKeySequence(QtCore.Qt.Key_Return), self.sendBtn, self.changeContent)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 350, 101, 21))
        self.label_3.setObjectName("label_3")
        self.micBtn = QtWidgets.QPushButton(self.centralwidget)
        self.micBtn.setGeometry(QtCore.QRect(510, 170, 91, 61))
        self.micBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("mic.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.micBtn.setIcon(icon2)
        self.micBtn.setIconSize(QtCore.QSize(40, 40))
        self.micBtn.setCheckable(False)
        self.micBtn.setDefault(False)
        self.micBtn.setObjectName("micBtn")

        #add signal to checkbox
        self.micBtn.clicked.connect(self.listen)
        self.micBtn.setToolTip("Press SPACE to talk")
        self.shortcut = QtWidgets.QShortcut(
                            QtGui.QKeySequence(QtCore.Qt.Key_Space), self.micBtn, self.listen)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Windows Assistant"))
        self.label_2.setText(_translate("MainWindow", "USER:"))
        self.sendBtn.setStatusTip(_translate("MainWindow", "Send"))
        self.label_3.setText(_translate("MainWindow", "USER INPUT:"))

    
    def otherwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Db_Window()
        self.ui.setupUi(self.window)
        self.window.show()


    def listen(self):
        print("Assistant: Listening...")
        said = get_audio()
        self.user_display.append("User: " + said)
        if "add command" in said:
            self.otherwindow()
        else:
            main(said)


    def changeContent(self):
        userInput = self.user_input.text()
        self.user_display.append("User: " + userInput)
        self.user_input.clear()
        
        if "add command" in userInput:
            self.otherwindow()
            
        else:
            main_write(userInput)
 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
