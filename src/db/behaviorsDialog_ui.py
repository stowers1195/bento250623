# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'behaviorsDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *  # type: ignore
from qtpy.QtGui import *  # type: ignore
from qtpy.QtWidgets import *  # type: ignore


class Ui_BehaviorsDialog(object):
    def setupUi(self, BehaviorsDialog):
        if not BehaviorsDialog.objectName():
            BehaviorsDialog.setObjectName(u"BehaviorsDialog")
        BehaviorsDialog.resize(583, 1027)
        self.verticalLayout = QVBoxLayout(BehaviorsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.buttonsHorizontalLayout = QHBoxLayout()
        self.buttonsHorizontalLayout.setObjectName(u"buttonsHorizontalLayout")
        self.hideInactiveBehaviorsCheckBox = QCheckBox(BehaviorsDialog)
        self.hideInactiveBehaviorsCheckBox.setObjectName(u"hideInactiveBehaviorsCheckBox")
        self.hideInactiveBehaviorsCheckBox.setChecked(False)

        self.buttonsHorizontalLayout.addWidget(self.hideInactiveBehaviorsCheckBox)

        self.addBehaviorPushButton = QPushButton(BehaviorsDialog)
        self.addBehaviorPushButton.setObjectName(u"addBehaviorPushButton")

        self.buttonsHorizontalLayout.addWidget(self.addBehaviorPushButton)


        self.verticalLayout.addLayout(self.buttonsHorizontalLayout)

        self.behaviorsTableView = QTableView(BehaviorsDialog)
        self.behaviorsTableView.setObjectName(u"behaviorsTableView")
        self.behaviorsTableView.setAlternatingRowColors(True)
        self.behaviorsTableView.setTextElideMode(Qt.ElideNone)
        self.behaviorsTableView.setSortingEnabled(True)
        self.behaviorsTableView.horizontalHeader().setProperty("showSortIndicator", True)
        self.behaviorsTableView.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.behaviorsTableView)

        self.buttonBox = QDialogButtonBox(BehaviorsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(BehaviorsDialog)
        self.buttonBox.accepted.connect(BehaviorsDialog.accept)
        self.buttonBox.rejected.connect(BehaviorsDialog.reject)

        QMetaObject.connectSlotsByName(BehaviorsDialog)
    # setupUi

    def retranslateUi(self, BehaviorsDialog):
        BehaviorsDialog.setWindowTitle(QCoreApplication.translate("BehaviorsDialog", u"Behaviors", None))
        self.hideInactiveBehaviorsCheckBox.setText(QCoreApplication.translate("BehaviorsDialog", u"Hide inactive behaviors", None))
        self.addBehaviorPushButton.setText(QCoreApplication.translate("BehaviorsDialog", u"Add New Behavior", None))
    # retranslateUi

