# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/preview.ui'
#
# Created: Fri Jun 14 23:32:02 2013
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(335, 282)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.frontPrevBox = QtGui.QVBoxLayout(self.groupBox)
        self.frontPrevBox.setMargin(0)
        self.frontPrevBox.setObjectName("frontPrevBox")
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.backPrevBox = QtGui.QVBoxLayout(self.groupBox_2)
        self.backPrevBox.setMargin(0)
        self.backPrevBox.setObjectName("backPrevBox")
        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.groupBox.setTitle(_("Front Preview"))
        self.groupBox_2.setTitle(_("Back Preview"))

