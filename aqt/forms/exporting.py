# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/exporting.ui'
#
# Created: Fri Jun 14 23:31:52 2013
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ExportDialog(object):
    def setupUi(self, ExportDialog):
        ExportDialog.setObjectName("ExportDialog")
        ExportDialog.resize(295, 202)
        self.vboxlayout = QtGui.QVBoxLayout(ExportDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.label = QtGui.QLabel(ExportDialog)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.format = QtGui.QComboBox(ExportDialog)
        self.format.setObjectName("format")
        self.gridlayout.addWidget(self.format, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(ExportDialog)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.deck = QtGui.QComboBox(ExportDialog)
        self.deck.setObjectName("deck")
        self.gridlayout.addWidget(self.deck, 1, 1, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.includeSched = QtGui.QCheckBox(ExportDialog)
        self.includeSched.setChecked(True)
        self.includeSched.setObjectName("includeSched")
        self.vboxlayout1.addWidget(self.includeSched)
        self.includeMedia = QtGui.QCheckBox(ExportDialog)
        self.includeMedia.setChecked(True)
        self.includeMedia.setObjectName("includeMedia")
        self.vboxlayout1.addWidget(self.includeMedia)
        self.includeTags = QtGui.QCheckBox(ExportDialog)
        self.includeTags.setChecked(True)
        self.includeTags.setObjectName("includeTags")
        self.vboxlayout1.addWidget(self.includeTags)
        self.vboxlayout.addLayout(self.vboxlayout1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(ExportDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(ExportDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ExportDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ExportDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ExportDialog)
        ExportDialog.setTabOrder(self.format, self.deck)
        ExportDialog.setTabOrder(self.deck, self.includeSched)
        ExportDialog.setTabOrder(self.includeSched, self.includeMedia)
        ExportDialog.setTabOrder(self.includeMedia, self.includeTags)
        ExportDialog.setTabOrder(self.includeTags, self.buttonBox)

    def retranslateUi(self, ExportDialog):
        ExportDialog.setWindowTitle(_("Export"))
        self.label.setText(_("<b>Export format</b>:"))
        self.label_2.setText(_("<b>Include</b>:"))
        self.includeSched.setText(_("Include scheduling information"))
        self.includeMedia.setText(_("Include media"))
        self.includeTags.setText(_("Include tags"))

