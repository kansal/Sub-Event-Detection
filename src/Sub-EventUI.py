# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sub-Event.ui'
#
# Created: Thu Apr 17 10:39:42 2014
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

class Ui_subEvent(object):
	def setupUi(self, subEvent):
		subEvent.setObjectName(_fromUtf8("subEvent"))
        subEvent.resize(638, 477)
        self.label = QtGui.QLabel(subEvent)
        self.label.setGeometry(QtCore.QRect(120, 0, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(subEvent)
        self.line.setGeometry(QtCore.QRect(-20, 440, 661, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.widget = QtGui.QWidget(subEvent)
        self.widget.setGeometry(QtCore.QRect(100, 110, 471, 54))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setPlaceholderText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.browse = QtGui.QPushButton(self.widget)
        self.browse.setObjectName(_fromUtf8("browse"))
        self.horizontalLayout.addWidget(self.browse)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radioButton = QtGui.QRadioButton(self.widget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.widget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.verticalLayout.addWidget(self.radioButton_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(subEvent)
        QtCore.QObject.connect(self.browse, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ShowFileDialog)
        QtCore.QMetaObject.connectSlotsByName(subEvent)
    
	def retranslateUi(self, subEvent):
		subEvent.setWindowTitle(_translate("subEvent", "Sub-Event ", None))
		self.label.setText(_translate("subEvent", "Sub-Event Detection from Twitter", None))
		self.browse.setText(_translate("subEvent", "Browse", None))
		self.radioButton.setText(_translate("subEvent", "Raw File", None))
		self.radioButton_2.setText(_translate("subEvent", "Filtered Tweets", None))
	
	def ShowFileDialog(self):
		self.lineEdit.setText(QFileDialog.getOpenFileName())


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    subEvent = QtGui.QDialog()
    ui = Ui_subEvent()
    print subEvent
    ui.setupUi(subEvent)
    subEvent.show()
    sys.exit(app.exec_())

