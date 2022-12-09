# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Spaceship Control PanelNnDCYT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 599)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.gui_lang_label = QLabel(self.centralwidget)
        self.gui_lang_label.setObjectName(u"gui_lang_label")
        font = QFont()
        font.setPointSize(12)
        self.gui_lang_label.setFont(font)
        self.gui_lang_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.gui_lang_label)

        self.comboBox_language = QComboBox(self.centralwidget)
        self.comboBox_language.setObjectName(u"comboBox_language")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_language.sizePolicy().hasHeightForWidth())
        self.comboBox_language.setSizePolicy(sizePolicy)
        self.comboBox_language.setFont(font)

        self.horizontalLayout.addWidget(self.comboBox_language)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.greeting_label = QLabel(self.centralwidget)
        self.greeting_label.setObjectName(u"greeting_label")
        font1 = QFont()
        font1.setPointSize(19)
        self.greeting_label.setFont(font1)
        self.greeting_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.greeting_label)

        self.verticalSpacer_2 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setEnabled(True)

        self.verticalLayout.addWidget(self.listView)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.destination_label = QLabel(self.centralwidget)
        self.destination_label.setObjectName(u"destination_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.destination_label.sizePolicy().hasHeightForWidth())
        self.destination_label.setSizePolicy(sizePolicy1)
        self.destination_label.setFont(font)
        self.destination_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.destination_label)

        self.destination_comboBox = QComboBox(self.centralwidget)
        self.destination_comboBox.addItem("")
        self.destination_comboBox.addItem("")
        self.destination_comboBox.addItem("")
        self.destination_comboBox.addItem("")
        self.destination_comboBox.addItem("")
        self.destination_comboBox.addItem("")
        self.destination_comboBox.setObjectName(u"destination_comboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.destination_comboBox.sizePolicy().hasHeightForWidth())
        self.destination_comboBox.setSizePolicy(sizePolicy2)
        self.destination_comboBox.setFont(font)

        self.horizontalLayout_2.addWidget(self.destination_comboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.watchstars_checkBox = QCheckBox(self.centralwidget)
        self.watchstars_checkBox.setObjectName(u"watchstars_checkBox")
        font2 = QFont()
        font2.setPointSize(14)
        self.watchstars_checkBox.setFont(font2)

        self.verticalLayout.addWidget(self.watchstars_checkBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.compute_pushButton = QPushButton(self.centralwidget)
        self.compute_pushButton.setObjectName(u"compute_pushButton")
        sizePolicy2.setHeightForWidth(self.compute_pushButton.sizePolicy().hasHeightForWidth())
        self.compute_pushButton.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setPointSize(13)
        self.compute_pushButton.setFont(font3)
        self.compute_pushButton.setStyleSheet(u"padding:10px")

        self.horizontalLayout_3.addWidget(self.compute_pushButton)

        self._pushButton_2 = QPushButton(self.centralwidget)
        self._pushButton_2.setObjectName(u"_pushButton_2")
        sizePolicy2.setHeightForWidth(self._pushButton_2.sizePolicy().hasHeightForWidth())
        self._pushButton_2.setSizePolicy(sizePolicy2)
        self._pushButton_2.setFont(font3)
        self._pushButton_2.setAutoFillBackground(False)
        self._pushButton_2.setStyleSheet(u"padding:10px;\n"
"background-color: rgb(0, 255, 0);")

        self.horizontalLayout_3.addWidget(self._pushButton_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.gui_lang_label.setText(QCoreApplication.translate("MainWindow", u"\u042f\u0437\u044b\u043a \u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441\u0430", None))
        self.greeting_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0432\u0435\u0442, \u0437\u0435\u043c\u043b\u044f\u043d\u0438\u043d", None))
        self.destination_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u043d\u043a\u0442 \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
        self.destination_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0435\u043c\u043b\u044f", None))
        self.destination_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041b\u0443\u043d\u0430", None))
        self.destination_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0441", None))
        self.destination_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u0438\u0441\u0442\u043e", None))
        self.destination_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0415\u0432\u0440\u043e\u043f\u0430", None))
        self.destination_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0413\u0430\u043d\u0438\u043c\u0435\u0434", None))

        self.watchstars_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0432 \u043f\u043e\u043b\u0435\u0442\u0435 \u043d\u0430 \u0437\u0432\u0435\u0437\u0434\u044b", None))
        self.compute_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u043b\u043e\u0436\u0438\u0442\u044c \u043c\u0430\u0440\u0448\u0440\u0443\u0442", None))
        self._pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0437\u0432\u0435\u0437\u0434\u043e\u043b\u0435\u0442", None))
    # retranslateUi

