# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/about.ui'
#
# Created: Fri Sep 13 18:19:05 2013
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(410, 664)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(About.sizePolicy().hasHeightForWidth())
        About.setSizePolicy(sizePolicy)
        self.vboxlayout = QtGui.QVBoxLayout(About)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName("vboxlayout")
        self.label = QtWebKit.QWebView(About)
        self.label.setUrl(QtCore.QUrl("about:blank"))
        self.label.setObjectName("label")
        self.vboxlayout.addWidget(self.label)
        self.buttonBox = QtGui.QDialogButtonBox(About)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(About)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), About.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), About.reject)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(_("About Anki"))

from PyQt4 import QtWebKit
import icons_rc
