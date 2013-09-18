# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/profiles.ui'
#
# Created: Fri Sep 13 18:19:46 2013
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(352, 283)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/anki.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.profiles = QtGui.QListWidget(Dialog)
        self.profiles.setObjectName("profiles")
        self.verticalLayout_2.addWidget(self.profiles)
        self.passLabel = QtGui.QLabel(Dialog)
        self.passLabel.setObjectName("passLabel")
        self.verticalLayout_2.addWidget(self.passLabel)
        self.passEdit = QtGui.QLineEdit(Dialog)
        self.passEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passEdit.setObjectName("passEdit")
        self.verticalLayout_2.addWidget(self.passEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.login = QtGui.QPushButton(Dialog)
        self.login.setObjectName("login")
        self.verticalLayout.addWidget(self.login)
        self.add = QtGui.QPushButton(Dialog)
        self.add.setObjectName("add")
        self.verticalLayout.addWidget(self.add)
        self.rename = QtGui.QPushButton(Dialog)
        self.rename.setObjectName("rename")
        self.verticalLayout.addWidget(self.rename)
        self.delete_2 = QtGui.QPushButton(Dialog)
        self.delete_2.setObjectName("delete_2")
        self.verticalLayout.addWidget(self.delete_2)
        self.quit = QtGui.QPushButton(Dialog)
        self.quit.setObjectName("quit")
        self.verticalLayout.addWidget(self.quit)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.profiles, self.passEdit)
        Dialog.setTabOrder(self.passEdit, self.login)
        Dialog.setTabOrder(self.login, self.add)
        Dialog.setTabOrder(self.add, self.rename)
        Dialog.setTabOrder(self.rename, self.delete_2)
        Dialog.setTabOrder(self.delete_2, self.quit)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Profiles"))
        self.label_2.setText(_("Profile:"))
        self.passLabel.setText(_("Password:"))
        self.login.setText(_("Open"))
        self.add.setText(_("Add"))
        self.rename.setText(_("Rename"))
        self.delete_2.setText(_("Delete"))
        self.quit.setText(_("Quit"))

import icons_rc
