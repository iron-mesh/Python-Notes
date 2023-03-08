# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InputStringListDesignedqoUWru.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(470, 335)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(Form)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        font = QFont()
        font.setPointSize(9)
        self.listWidget.setFont(font)

        self.horizontalLayout.addWidget(self.listWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.add_btn = QPushButton(Form)
        self.add_btn.setObjectName(u"add_btn")

        self.verticalLayout.addWidget(self.add_btn)

        self.edit_btn = QPushButton(Form)
        self.edit_btn.setObjectName(u"edit_btn")

        self.verticalLayout.addWidget(self.edit_btn)

        self.delete_btn = QPushButton(Form)
        self.delete_btn.setObjectName(u"delete_btn")

        self.verticalLayout.addWidget(self.delete_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 36, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.moveup_btn = QPushButton(Form)
        self.moveup_btn.setObjectName(u"moveup_btn")

        self.verticalLayout.addWidget(self.moveup_btn)

        self.movedown_btn = QPushButton(Form)
        self.movedown_btn.setObjectName(u"movedown_btn")

        self.verticalLayout.addWidget(self.movedown_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"Hello", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0438\u0432\u0435\u0442", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.add_btn.setText(QCoreApplication.translate("Form", u"Add", None))
        self.edit_btn.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.delete_btn.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.moveup_btn.setText(QCoreApplication.translate("Form", u"\u2b9d", None))
        self.movedown_btn.setText(QCoreApplication.translate("Form", u"\u2b9f", None))
    # retranslateUi

