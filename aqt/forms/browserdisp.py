# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/browserdisp.ui'
#
# Created: Fri Jun 14 23:31:42 2013
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(412, 241)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.qfmt = QtGui.QLineEdit(Dialog)
        self.qfmt.setObjectName("qfmt")
        self.verticalLayout.addWidget(self.qfmt)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.afmt = QtGui.QLineEdit(Dialog)
        self.afmt.setObjectName("afmt")
        self.verticalLayout.addWidget(self.afmt)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.font = QtGui.QFontComboBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.font.sizePolicy().hasHeightForWidth())
        self.font.setSizePolicy(sizePolicy)
        self.font.setObjectName("font")
        self.horizontalLayout.addWidget(self.font)
        self.fontSize = QtGui.QSpinBox(Dialog)
        self.fontSize.setMinimum(6)
        self.fontSize.setObjectName("fontSize")
        self.horizontalLayout.addWidget(self.fontSize)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.qfmt, self.afmt)
        Dialog.setTabOrder(self.afmt, self.font)
        Dialog.setTabOrder(self.font, self.fontSize)
        Dialog.setTabOrder(self.fontSize, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Browser Appearance"))
        self.label.setText(_("Override front template:"))
        self.label_2.setText(_("Override back template:"))
        self.label_3.setText(_("Override font:"))

