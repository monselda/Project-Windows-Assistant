# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'db_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from main_API import host, passwd, database, user



try:
    #mysql connector and cursor
    mydb = mysql.connector.connect(
        host=host, 
        user=user, 
        password=passwd, 
        database=database,
        # Important!!!
        auth_plugin='mysql_native_password'
        # Important!!!
        )
    mycursor = mydb.cursor(buffered=True)
except:
    print("Please add your credentials to main_mysql_cred.")



class Db_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(628, 190)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.command = QtWidgets.QLineEdit(self.centralwidget)
        self.command.setGeometry(QtCore.QRect(140, 30, 471, 31))
        self.command.setStatusTip("")
        self.command.setPlaceholderText("")
        self.command.setObjectName("command")
        self.response = QtWidgets.QLineEdit(self.centralwidget)
        self.response.setGeometry(QtCore.QRect(140, 80, 471, 31))
        self.response.setStatusTip("")
        self.response.setPlaceholderText("")
        self.response.setObjectName("response")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 71, 16))
        self.label_3.setObjectName("label_3")
        self.db_save = QtWidgets.QPushButton(self.centralwidget)
        self.db_save.setGeometry(QtCore.QRect(520, 120, 93, 28))
        self.db_save.setObjectName("db_save")

        self.db_save.clicked.connect(self.db)
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Data"))
        self.label_2.setText(_translate("MainWindow", "COMMAND:"))
        self.label_3.setText(_translate("MainWindow", "RESPONSE:"))
        self.db_save.setText(_translate("MainWindow", "SAVE"))

    
    def db(self):
        get_command = self.command.text()
        get_response = self.response.text()

        try:
            mycursor.execute("""INSERT INTO commands(command, response) VALUES(%s, %s)""", (get_command, get_response))
            mydb.commit()
        finally:
            mydb.close()        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Db_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
