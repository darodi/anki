# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/stats.ui'
#
# Created: Fri Jun 14 23:32:08 2013
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(607, 556)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.web = QtWebKit.QWebView(Dialog)
        self.web.setUrl(QtCore.QUrl("about:blank"))
        self.web.setObjectName("web")
        self.verticalLayout.addWidget(self.web)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setMargin(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groups = QtGui.QRadioButton(self.groupBox_2)
        self.groups.setChecked(True)
        self.groups.setObjectName("groups")
        self.horizontalLayout_2.addWidget(self.groups)
        self.all = QtGui.QRadioButton(self.groupBox_2)
        self.all.setObjectName("all")
        self.horizontalLayout_2.addWidget(self.all)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.month = QtGui.QRadioButton(self.groupBox)
        self.month.setChecked(True)
        self.month.setObjectName("month")
        self.horizontalLayout.addWidget(self.month)
        self.year = QtGui.QRadioButton(self.groupBox)
        self.year.setObjectName("year")
        self.horizontalLayout.addWidget(self.year)
        self.life = QtGui.QRadioButton(self.groupBox)
        self.life.setObjectName("life")
        self.horizontalLayout.addWidget(self.life)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Statistics"))
        self.groups.setText(_("deck"))
        self.all.setText(_("collection"))
        self.month.setText(_("1 month"))
        self.year.setText(_("1 year"))
        self.life.setText(_("deck life"))

from PyQt4 import QtWebKit
