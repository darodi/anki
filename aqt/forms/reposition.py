# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/reposition.ui'
#
# Created: Fri Jun 14 23:32:04 2013
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(272, 229)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.start = QtGui.QSpinBox(Dialog)
        self.start.setMinimum(-20000000)
        self.start.setMaximum(200000000)
        self.start.setProperty("value", 0)
        self.start.setObjectName("start")
        self.gridLayout.addWidget(self.start, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.step = QtGui.QSpinBox(Dialog)
        self.step.setMinimum(1)
        self.step.setMaximum(10000)
        self.step.setObjectName("step")
        self.gridLayout.addWidget(self.step, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.randomize = QtGui.QCheckBox(Dialog)
        self.randomize.setObjectName("randomize")
        self.verticalLayout.addWidget(self.randomize)
        self.shift = QtGui.QCheckBox(Dialog)
        self.shift.setChecked(True)
        self.shift.setObjectName("shift")
        self.verticalLayout.addWidget(self.shift)
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
        Dialog.setTabOrder(self.start, self.step)
        Dialog.setTabOrder(self.step, self.randomize)
        Dialog.setTabOrder(self.randomize, self.shift)
        Dialog.setTabOrder(self.shift, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Reposition New Cards"))
        self.label_2.setText(_("Start position:"))
        self.label_3.setText(_("Step:"))
        self.randomize.setText(_("Randomize order"))
        self.shift.setText(_("Shift position of existing cards"))

