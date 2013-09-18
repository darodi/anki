# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/addcards.ui'
#
# Created: Fri Sep 13 18:19:06 2013
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(453, 366)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/list-add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setContentsMargins(12, 6, 12, 12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.modelArea = QtGui.QWidget(Dialog)
        self.modelArea.setMinimumSize(QtCore.QSize(0, 10))
        self.modelArea.setObjectName("modelArea")
        self.horizontalLayout.addWidget(self.modelArea)
        self.deckArea = QtGui.QWidget(Dialog)
        self.deckArea.setObjectName("deckArea")
        self.horizontalLayout.addWidget(self.deckArea)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.fieldsArea = QtGui.QWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.fieldsArea.sizePolicy().hasHeightForWidth())
        self.fieldsArea.setSizePolicy(sizePolicy)
        self.fieldsArea.setAutoFillBackground(True)
        self.fieldsArea.setObjectName("fieldsArea")
        self.verticalLayout.addWidget(self.fieldsArea)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.NoButton)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Add"))

