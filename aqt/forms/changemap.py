# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/changemap.ui'
#
# Created: Fri Jun 14 23:31:44 2013
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ChangeMap(object):
    def setupUi(self, ChangeMap):
        ChangeMap.setObjectName("ChangeMap")
        ChangeMap.resize(391, 360)
        self.vboxlayout = QtGui.QVBoxLayout(ChangeMap)
        self.vboxlayout.setObjectName("vboxlayout")
        self.label = QtGui.QLabel(ChangeMap)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.vboxlayout.addWidget(self.label)
        self.fields = QtGui.QListWidget(ChangeMap)
        self.fields.setObjectName("fields")
        self.vboxlayout.addWidget(self.fields)
        self.buttonBox = QtGui.QDialogButtonBox(ChangeMap)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(ChangeMap)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ChangeMap.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ChangeMap.reject)
        QtCore.QObject.connect(self.fields, QtCore.SIGNAL("doubleClicked(QModelIndex)"), ChangeMap.accept)
        QtCore.QMetaObject.connectSlotsByName(ChangeMap)

    def retranslateUi(self, ChangeMap):
        ChangeMap.setWindowTitle(_("Import"))
        self.label.setText(_("Target field:"))

