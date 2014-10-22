# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sub-EventUIFinal.ui'
#
# Created: Thu Apr 17 13:27:03 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(595, 456)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 10, 256, 192))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget.addItem("Hello")
        self.listWidget.addItem("World!")
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 60, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 595, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionStart = QtGui.QAction(MainWindow)
        self.actionStart.setObjectName(_fromUtf8("actionStart"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionChoose_File = QtGui.QAction(MainWindow)
        self.actionChoose_File.setObjectName(_fromUtf8("actionChoose_File"))
        self.menuFile.addAction(self.actionStart)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionChoose_File)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addItem)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.actionStart.setText(_translate("MainWindow", "Start", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionChoose_File.setText(_translate("MainWindow", "Choose File", None))
        
    def addItem(self):
		self.listWidget.addItem(str(self.listWidget.currentRow()))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

