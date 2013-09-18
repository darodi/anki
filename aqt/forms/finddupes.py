# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/finddupes.ui'
#
# Created: Fri Sep 13 18:19:35 2013
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(531, 345)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.fields = QtGui.QComboBox(Dialog)
        self.fields.setObjectName("fields")
        self.gridLayout.addWidget(self.fields, 1, 2, 1, 2)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.search = QtGui.QLineEdit(Dialog)
        self.search.setObjectName("search")
        self.gridLayout.addWidget(self.search, 2, 2, 1, 2)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.webView = QtWebKit.QWebView(self.frame)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.verticalLayout.addWidget(self.webView)
        self.verticalLayout_2.addWidget(self.frame)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.fields, self.webView)
        Dialog.setTabOrder(self.webView, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Find Duplicates"))
        self.label_2.setText(_("Optional limit:"))
        self.label.setText(_("Look in field:"))

from PyQt4 import QtWebKit
