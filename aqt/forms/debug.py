# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/debug.ui'
#
# Created: Fri Sep 13 18:19:25 2013
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(643, 580)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text = QtGui.QPlainTextEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.text.sizePolicy().hasHeightForWidth())
        self.text.setSizePolicy(sizePolicy)
        self.text.setMaximumSize(QtCore.QSize(16777215, 100))
        self.text.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.text.setObjectName("text")
        self.verticalLayout.addWidget(self.text)
        self.log = QtGui.QPlainTextEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.log.sizePolicy().hasHeightForWidth())
        self.log.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.log.setFont(font)
        self.log.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.log.setReadOnly(True)
        self.log.setObjectName("log")
        self.verticalLayout.addWidget(self.log)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Debug Console"))

