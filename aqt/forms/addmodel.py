# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/addmodel.ui'
#
# Created: Fri Sep 13 18:19:10 2013
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(285, 269)
        self.vboxlayout = QtGui.QVBoxLayout(Dialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.models = QtGui.QListWidget(self.groupBox)
        self.models.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.models.setTabKeyNavigation(True)
        self.models.setObjectName("models")
        self.vboxlayout1.addWidget(self.models)
        self.vboxlayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Add Note Type"))

