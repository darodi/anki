# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/reschedule.ui'
#
# Created: Fri Sep 13 18:19:48 2013
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(325, 144)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.asNew = QtGui.QRadioButton(Dialog)
        self.asNew.setChecked(True)
        self.asNew.setObjectName("asNew")
        self.verticalLayout_2.addWidget(self.asNew)
        self.asRev = QtGui.QRadioButton(Dialog)
        self.asRev.setObjectName("asRev")
        self.verticalLayout_2.addWidget(self.asRev)
        self.rangebox = QtGui.QWidget(Dialog)
        self.rangebox.setEnabled(False)
        self.rangebox.setObjectName("rangebox")
        self.verticalLayout = QtGui.QVBoxLayout(self.rangebox)
        self.verticalLayout.setContentsMargins(20, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtGui.QLabel(self.rangebox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.min = QtGui.QSpinBox(self.rangebox)
        self.min.setMaximum(9999)
        self.min.setObjectName("min")
        self.gridLayout.addWidget(self.min, 0, 0, 1, 1)
        self.max = QtGui.QSpinBox(self.rangebox)
        self.max.setMaximum(9999)
        self.max.setObjectName("max")
        self.gridLayout.addWidget(self.max, 0, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.rangebox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.rangebox)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QObject.connect(self.asRev, QtCore.SIGNAL("toggled(bool)"), self.rangebox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.asNew, self.asRev)
        Dialog.setTabOrder(self.asRev, self.min)
        Dialog.setTabOrder(self.min, self.max)
        Dialog.setTabOrder(self.max, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Reschedule"))
        self.asNew.setText(_("Place at end of new card queue"))
        self.asRev.setText(_("Place in review queue with interval between:"))
        self.label_3.setText(_("~"))
        self.label_4.setText(_("days"))

