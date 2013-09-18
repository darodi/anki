# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/taglimit.ui'
#
# Created: Fri Sep 13 18:19:54 2013
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(361, 394)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.activeCheck = QtGui.QCheckBox(Dialog)
        self.activeCheck.setObjectName("activeCheck")
        self.verticalLayout.addWidget(self.activeCheck)
        self.activeList = QtGui.QListWidget(Dialog)
        self.activeList.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.activeList.sizePolicy().hasHeightForWidth())
        self.activeList.setSizePolicy(sizePolicy)
        self.activeList.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.activeList.setObjectName("activeList")
        self.verticalLayout.addWidget(self.activeList)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.inactiveList = QtGui.QListWidget(Dialog)
        self.inactiveList.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.inactiveList.sizePolicy().hasHeightForWidth())
        self.inactiveList.setSizePolicy(sizePolicy)
        self.inactiveList.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.inactiveList.setObjectName("inactiveList")
        self.verticalLayout.addWidget(self.inactiveList)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QObject.connect(self.activeCheck, QtCore.SIGNAL("toggled(bool)"), self.activeList.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Selective Study"))
        self.activeCheck.setText(_("Require one or more of these tags:"))
        self.label.setText(_("Select tags to exclude:"))

