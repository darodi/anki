# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/fields.ui'
#
# Created: Fri Jun 14 23:31:52 2013
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(412, 352)
        Dialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fieldList = QtGui.QListWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldList.sizePolicy().hasHeightForWidth())
        self.fieldList.setSizePolicy(sizePolicy)
        self.fieldList.setMinimumSize(QtCore.QSize(50, 60))
        self.fieldList.setObjectName("fieldList")
        self.horizontalLayout.addWidget(self.fieldList)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.fieldAdd = QtGui.QPushButton(Dialog)
        self.fieldAdd.setObjectName("fieldAdd")
        self.verticalLayout_3.addWidget(self.fieldAdd)
        self.fieldDelete = QtGui.QPushButton(Dialog)
        self.fieldDelete.setObjectName("fieldDelete")
        self.verticalLayout_3.addWidget(self.fieldDelete)
        self.fieldRename = QtGui.QPushButton(Dialog)
        self.fieldRename.setObjectName("fieldRename")
        self.verticalLayout_3.addWidget(self.fieldRename)
        self.fieldPosition = QtGui.QPushButton(Dialog)
        self.fieldPosition.setObjectName("fieldPosition")
        self.verticalLayout_3.addWidget(self.fieldPosition)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self._2 = QtGui.QGridLayout()
        self._2.setObjectName("_2")
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self._2.addWidget(self.label_5, 0, 0, 1, 1)
        self.fontFamily = QtGui.QFontComboBox(Dialog)
        self.fontFamily.setMinimumSize(QtCore.QSize(0, 25))
        self.fontFamily.setObjectName("fontFamily")
        self._2.addWidget(self.fontFamily, 0, 1, 1, 1)
        self.rtl = QtGui.QCheckBox(Dialog)
        self.rtl.setObjectName("rtl")
        self._2.addWidget(self.rtl, 3, 1, 1, 1)
        self.fontSize = QtGui.QSpinBox(Dialog)
        self.fontSize.setMinimum(5)
        self.fontSize.setMaximum(300)
        self.fontSize.setObjectName("fontSize")
        self._2.addWidget(self.fontSize, 0, 2, 1, 1)
        self.sticky = QtGui.QCheckBox(Dialog)
        self.sticky.setObjectName("sticky")
        self._2.addWidget(self.sticky, 2, 1, 1, 1)
        self.label_18 = QtGui.QLabel(Dialog)
        self.label_18.setObjectName("label_18")
        self._2.addWidget(self.label_18, 1, 0, 1, 1)
        self.sortField = QtGui.QRadioButton(Dialog)
        self.sortField.setObjectName("sortField")
        self._2.addWidget(self.sortField, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self._2)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Help)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.fieldList, self.fieldAdd)
        Dialog.setTabOrder(self.fieldAdd, self.fieldDelete)
        Dialog.setTabOrder(self.fieldDelete, self.fieldRename)
        Dialog.setTabOrder(self.fieldRename, self.fieldPosition)
        Dialog.setTabOrder(self.fieldPosition, self.fontFamily)
        Dialog.setTabOrder(self.fontFamily, self.fontSize)
        Dialog.setTabOrder(self.fontSize, self.sortField)
        Dialog.setTabOrder(self.sortField, self.sticky)
        Dialog.setTabOrder(self.sticky, self.rtl)
        Dialog.setTabOrder(self.rtl, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Fields"))
        self.fieldAdd.setText(_("Add"))
        self.fieldDelete.setText(_("Delete"))
        self.fieldRename.setText(_("Rename"))
        self.fieldPosition.setText(_("Reposition"))
        self.label_5.setText(_("Editing Font"))
        self.rtl.setText(_("Reverse text direction (RTL)"))
        self.sticky.setText(_("Remember last input when adding"))
        self.label_18.setText(_("Options"))
        self.sortField.setText(_("Sort by this field in the browser"))

import icons_rc
