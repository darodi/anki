# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/modelopts.ui'
#
# Created: Fri Sep 13 18:19:40 2013
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(276, 323)
        Dialog.setWindowTitle("")
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.qtabwidget = QtGui.QTabWidget(Dialog)
        self.qtabwidget.setObjectName("qtabwidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.latexHeader = QtGui.QTextEdit(self.tab)
        self.latexHeader.setTabChangesFocus(True)
        self.latexHeader.setObjectName("latexHeader")
        self.verticalLayout.addWidget(self.latexHeader)
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.latexFooter = QtGui.QTextEdit(self.tab)
        self.latexFooter.setTabChangesFocus(True)
        self.latexFooter.setObjectName("latexFooter")
        self.verticalLayout.addWidget(self.latexFooter)
        self.qtabwidget.addTab(self.tab, "")
        self.verticalLayout_2.addWidget(self.qtabwidget)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Help)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.qtabwidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.qtabwidget, self.buttonBox)
        Dialog.setTabOrder(self.buttonBox, self.latexHeader)
        Dialog.setTabOrder(self.latexHeader, self.latexFooter)

    def retranslateUi(self, Dialog):
        self.label_6.setText(_("Header"))
        self.label_7.setText(_("Footer"))
        self.qtabwidget.setTabText(self.qtabwidget.indexOf(self.tab), _("LaTeX"))

