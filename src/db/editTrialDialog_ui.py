# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editTrialDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from widgets.deleteableViews import DeleteableTableView
from widgets.deleteableViews import DeleteableTreeWidget


class Ui_EditTrialDialog(object):
    def setupUi(self, EditTrialDialog):
        if not EditTrialDialog.objectName():
            EditTrialDialog.setObjectName(u"EditTrialDialog")
        EditTrialDialog.resize(833, 541)
        self.verticalLayout = QVBoxLayout(EditTrialDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.generalInfoHorizontalLayout = QHBoxLayout()
        self.generalInfoHorizontalLayout.setObjectName(u"generalInfoHorizontalLayout")
        self.trialNumLabel = QLabel(EditTrialDialog)
        self.trialNumLabel.setObjectName(u"trialNumLabel")
        self.trialNumLabel.setMinimumSize(QSize(103, 0))

        self.generalInfoHorizontalLayout.addWidget(self.trialNumLabel)

        self.trialNumLineEdit = QLineEdit(EditTrialDialog)
        self.trialNumLineEdit.setObjectName(u"trialNumLineEdit")

        self.generalInfoHorizontalLayout.addWidget(self.trialNumLineEdit)

        self.trialStartTimeLabel = QLabel(EditTrialDialog)
        self.trialStartTimeLabel.setObjectName(u"trialStartTimeLabel")

        self.generalInfoHorizontalLayout.addWidget(self.trialStartTimeLabel)

        self.trialDateTimeEdit = QDateTimeEdit(EditTrialDialog)
        self.trialDateTimeEdit.setObjectName(u"trialDateTimeEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trialDateTimeEdit.sizePolicy().hasHeightForWidth())
        self.trialDateTimeEdit.setSizePolicy(sizePolicy)

        self.generalInfoHorizontalLayout.addWidget(self.trialDateTimeEdit)

        self.stimulusLabel = QLabel(EditTrialDialog)
        self.stimulusLabel.setObjectName(u"stimulusLabel")

        self.generalInfoHorizontalLayout.addWidget(self.stimulusLabel)

        self.stimulusLineEdit = QLineEdit(EditTrialDialog)
        self.stimulusLineEdit.setObjectName(u"stimulusLineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stimulusLineEdit.sizePolicy().hasHeightForWidth())
        self.stimulusLineEdit.setSizePolicy(sizePolicy1)

        self.generalInfoHorizontalLayout.addWidget(self.stimulusLineEdit)


        self.verticalLayout.addLayout(self.generalInfoHorizontalLayout)

        self.videosHorizontalLayout = QHBoxLayout()
        self.videosHorizontalLayout.setObjectName(u"videosHorizontalLayout")
        self.videosLabel = QLabel(EditTrialDialog)
        self.videosLabel.setObjectName(u"videosLabel")
        self.videosLabel.setMinimumSize(QSize(103, 0))
        self.videosLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.videosHorizontalLayout.addWidget(self.videosLabel)

        self.videosTreeWidget = DeleteableTreeWidget(EditTrialDialog)
        self.videosTreeWidget.setObjectName(u"videosTreeWidget")
        self.videosTreeWidget.setAlternatingRowColors(False)
        self.videosTreeWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.videosTreeWidget.setTextElideMode(Qt.ElideMiddle)
        self.videosTreeWidget.setExpandsOnDoubleClick(False)
        self.videosTreeWidget.setColumnCount(0)

        self.videosHorizontalLayout.addWidget(self.videosTreeWidget)

        self.videosSearchVerticalLayout = QVBoxLayout()
        self.videosSearchVerticalLayout.setObjectName(u"videosSearchVerticalLayout")
        self.videosSearchPushButton = QPushButton(EditTrialDialog)
        self.videosSearchPushButton.setObjectName(u"videosSearchPushButton")

        self.videosSearchVerticalLayout.addWidget(self.videosSearchPushButton)

        self.addPosePushButton = QPushButton(EditTrialDialog)
        self.addPosePushButton.setObjectName(u"addPosePushButton")

        self.videosSearchVerticalLayout.addWidget(self.addPosePushButton)

        self.videoPoseDeleteButton = QPushButton(EditTrialDialog)
        self.videoPoseDeleteButton.setObjectName(u"videoPoseDeleteButton")

        self.videosSearchVerticalLayout.addWidget(self.videoPoseDeleteButton)

        self.videosSearchVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.videosSearchVerticalLayout.addItem(self.videosSearchVerticalSpacer)


        self.videosHorizontalLayout.addLayout(self.videosSearchVerticalLayout)


        self.verticalLayout.addLayout(self.videosHorizontalLayout)

        self.annotationsHorizontalLayout = QHBoxLayout()
        self.annotationsHorizontalLayout.setObjectName(u"annotationsHorizontalLayout")
        self.annotationsLabel = QLabel(EditTrialDialog)
        self.annotationsLabel.setObjectName(u"annotationsLabel")
        self.annotationsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.annotationsHorizontalLayout.addWidget(self.annotationsLabel)

        self.annotationsTableView = DeleteableTableView(EditTrialDialog)
        self.annotationsTableView.setObjectName(u"annotationsTableView")

        self.annotationsHorizontalLayout.addWidget(self.annotationsTableView)

        self.annotationsSearchVerticalLayout = QVBoxLayout()
        self.annotationsSearchVerticalLayout.setObjectName(u"annotationsSearchVerticalLayout")
        self.annotationsSearchPushButton = QPushButton(EditTrialDialog)
        self.annotationsSearchPushButton.setObjectName(u"annotationsSearchPushButton")

        self.annotationsSearchVerticalLayout.addWidget(self.annotationsSearchPushButton)

        self.annotationsDeleteButton = QPushButton(EditTrialDialog)
        self.annotationsDeleteButton.setObjectName(u"annotationsDeleteButton")

        self.annotationsSearchVerticalLayout.addWidget(self.annotationsDeleteButton)

        self.annotationsSearchVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.annotationsSearchVerticalLayout.addItem(self.annotationsSearchVerticalSpacer)


        self.annotationsHorizontalLayout.addLayout(self.annotationsSearchVerticalLayout)


        self.verticalLayout.addLayout(self.annotationsHorizontalLayout)

        self.neuralsHorizontalLayout = QHBoxLayout()
        self.neuralsHorizontalLayout.setObjectName(u"neuralsHorizontalLayout")
        self.neuralsLabel = QLabel(EditTrialDialog)
        self.neuralsLabel.setObjectName(u"neuralsLabel")
        self.neuralsLabel.setMinimumSize(QSize(103, 0))
        self.neuralsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.neuralsHorizontalLayout.addWidget(self.neuralsLabel)

        self.neuralsTableView = DeleteableTableView(EditTrialDialog)
        self.neuralsTableView.setObjectName(u"neuralsTableView")

        self.neuralsHorizontalLayout.addWidget(self.neuralsTableView)

        self.neuralsSearchVerticalLayout = QVBoxLayout()
        self.neuralsSearchVerticalLayout.setObjectName(u"neuralsSearchVerticalLayout")
        self.neuralsSearchPushButton = QPushButton(EditTrialDialog)
        self.neuralsSearchPushButton.setObjectName(u"neuralsSearchPushButton")

        self.neuralsSearchVerticalLayout.addWidget(self.neuralsSearchPushButton)

        self.neuralsDeleteButton = QPushButton(EditTrialDialog)
        self.neuralsDeleteButton.setObjectName(u"neuralsDeleteButton")

        self.neuralsSearchVerticalLayout.addWidget(self.neuralsDeleteButton)

        self.neuralsSearchVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.neuralsSearchVerticalLayout.addItem(self.neuralsSearchVerticalSpacer)


        self.neuralsHorizontalLayout.addLayout(self.neuralsSearchVerticalLayout)


        self.verticalLayout.addLayout(self.neuralsHorizontalLayout)

        self.audiosHorizontalLayout = QHBoxLayout()
        self.audiosHorizontalLayout.setObjectName(u"audiosHorizontalLayout")
        self.audiosLabel = QLabel(EditTrialDialog)
        self.audiosLabel.setObjectName(u"audiosLabel")
        self.audiosLabel.setEnabled(True)
        self.audiosLabel.setMinimumSize(QSize(103, 0))
        self.audiosLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.audiosHorizontalLayout.addWidget(self.audiosLabel)

        self.audiosTreeView = QTreeView(EditTrialDialog)
        self.audiosTreeView.setObjectName(u"audiosTreeView")
        self.audiosTreeView.setEnabled(True)

        self.audiosHorizontalLayout.addWidget(self.audiosTreeView)

        self.audiosSearchVerticalLayout = QVBoxLayout()
        self.audiosSearchVerticalLayout.setObjectName(u"audiosSearchVerticalLayout")
        self.audiosSearchPushButton = QPushButton(EditTrialDialog)
        self.audiosSearchPushButton.setObjectName(u"audiosSearchPushButton")
        self.audiosSearchPushButton.setEnabled(True)

        self.audiosSearchVerticalLayout.addWidget(self.audiosSearchPushButton)

        self.audiosDeleteButton = QPushButton(EditTrialDialog)
        self.audiosDeleteButton.setObjectName(u"audiosDeleteButton")

        self.audiosSearchVerticalLayout.addWidget(self.audiosDeleteButton)

        self.audiosSearchVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.audiosSearchVerticalLayout.addItem(self.audiosSearchVerticalSpacer)


        self.audiosHorizontalLayout.addLayout(self.audiosSearchVerticalLayout)


        self.verticalLayout.addLayout(self.audiosHorizontalLayout)

        self.othersHorizontalLayout = QHBoxLayout()
        self.othersHorizontalLayout.setObjectName(u"othersHorizontalLayout")
        self.othersLabel = QLabel(EditTrialDialog)
        self.othersLabel.setObjectName(u"othersLabel")
        self.othersLabel.setEnabled(True)
        self.othersLabel.setMinimumSize(QSize(103, 0))
        self.othersLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.othersHorizontalLayout.addWidget(self.othersLabel)

        self.othersTableView = DeleteableTableView(EditTrialDialog)
        self.othersTableView.setObjectName(u"othersTableView")
        self.othersTableView.setEnabled(True)

        self.othersHorizontalLayout.addWidget(self.othersTableView)

        self.othersSearchVerticalLayout = QVBoxLayout()
        self.othersSearchVerticalLayout.setObjectName(u"othersSearchVerticalLayout")
        self.othersSearchPushButton = QPushButton(EditTrialDialog)
        self.othersSearchPushButton.setObjectName(u"othersSearchPushButton")
        self.othersSearchPushButton.setEnabled(True)

        self.othersSearchVerticalLayout.addWidget(self.othersSearchPushButton)

        self.othersDeleteButton = QPushButton(EditTrialDialog)
        self.othersDeleteButton.setObjectName(u"othersDeleteButton")

        self.othersSearchVerticalLayout.addWidget(self.othersDeleteButton)

        self.othersSearchVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.othersSearchVerticalLayout.addItem(self.othersSearchVerticalSpacer)


        self.othersHorizontalLayout.addLayout(self.othersSearchVerticalLayout)


        self.verticalLayout.addLayout(self.othersHorizontalLayout)

        self.buttonBox = QDialogButtonBox(EditTrialDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)

        self.retranslateUi(EditTrialDialog)
        self.buttonBox.accepted.connect(EditTrialDialog.accept)
        self.buttonBox.rejected.connect(EditTrialDialog.reject)

        QMetaObject.connectSlotsByName(EditTrialDialog)
    # setupUi

    def retranslateUi(self, EditTrialDialog):
        EditTrialDialog.setWindowTitle(QCoreApplication.translate("EditTrialDialog", u"Add or Edit Trial", None))
        self.trialNumLabel.setText(QCoreApplication.translate("EditTrialDialog", u"Trial Num: ", None))
        self.trialStartTimeLabel.setText(QCoreApplication.translate("EditTrialDialog", u"Trial Start Time: ", None))
        self.stimulusLabel.setText(QCoreApplication.translate("EditTrialDialog", u"Stimulus: ", None))
        self.videosLabel.setText(QCoreApplication.translate("EditTrialDialog", u"Video Files: ", None))
        self.videosSearchPushButton.setText(QCoreApplication.translate("EditTrialDialog", u"Search...", None))
        self.addPosePushButton.setText(QCoreApplication.translate("EditTrialDialog", u"Add Pose...", None))
        self.videoPoseDeleteButton.setText(QCoreApplication.translate("EditTrialDialog", u"Delete", None))
        self.annotationsLabel.setText(QCoreApplication.translate("EditTrialDialog", u"Annotation Files: ", None))
        self.annotationsSearchPushButton.setText(QCoreApplication.translate("EditTrialDialog", u"Search...", None))
        self.annotationsDeleteButton.setText(QCoreApplication.translate("EditTrialDialog", u"Delete", None))
        self.neuralsLabel.setText(QCoreApplication.translate("EditTrialDialog", u"Neural Files: ", None))
        self.neuralsSearchPushButton.setText(QCoreApplication.translate("EditTrialDialog", u"Search...", None))
        self.neuralsDeleteButton.setText(QCoreApplication.translate("EditTrialDialog", u"Delete", None))
        self.audiosLabel.setText(QCoreApplication.translate("EditTrialDialog", u"Audio Files: ", None))
        self.audiosSearchPushButton.setText(QCoreApplication.translate("EditTrialDialog", u"Search...", None))
        self.audiosDeleteButton.setText(QCoreApplication.translate("EditTrialDialog", u"Delete", None))
        self.othersLabel.setText(QCoreApplication.translate("EditTrialDialog", u"Other Files: ", None))
        self.othersSearchPushButton.setText(QCoreApplication.translate("EditTrialDialog", u"Search...", None))
        self.othersDeleteButton.setText(QCoreApplication.translate("EditTrialDialog", u"Delete", None))
    # retranslateUi

