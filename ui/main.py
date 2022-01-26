# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainqkaqzE.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
                               QHBoxLayout, QHeaderView, QLabel, QLineEdit,
                               QMainWindow, QMenuBar, QPushButton, QSizePolicy,
                               QSpacerItem, QStatusBar, QToolButton, QTreeWidget,
                               QTreeWidgetItem, QWidget, QTreeView)

class Ui_My_App(object):
    def setupUi(self, My_App):
        if not My_App.objectName():
            My_App.setObjectName(u"My_App")
        My_App.resize(823, 655)
        self.centralwidget = QWidget(My_App)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(9, 9, 501, 481))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.my_treeView = QTreeView(self.frame_4)
        self.my_treeView.setObjectName(u"my_treeWidget")
        self.my_treeView.setGeometry(QRect(10, 10, 461, 461))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(291, 9, 523, 594))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 276, 212))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(290, 10, 222, 181))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.name_LE = QLineEdit(self.frame_2)
        self.name_LE.setObjectName(u"name_LE")

        self.horizontalLayout_4.addWidget(self.name_LE)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(155, 0))

        self.horizontalLayout.addWidget(self.comboBox)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.photo_LE = QLineEdit(self.frame_2)
        self.photo_LE.setObjectName(u"photo_LE")

        self.horizontalLayout_3.addWidget(self.photo_LE)

        self.toolButton = QToolButton(self.frame_2)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_3.addWidget(self.toolButton)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(110, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(45, 22))

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 0, 1, 1)

        My_App.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(My_App)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 823, 22))
        My_App.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(My_App)
        self.statusbar.setObjectName(u"statusbar")
        My_App.setStatusBar(self.statusbar)

        self.retranslateUi(My_App)

        QMetaObject.connectSlotsByName(My_App)
    # setupUi

    def retranslateUi(self, My_App):
        My_App.setWindowTitle(QCoreApplication.translate("My_App", u"MainWindow", None))
        ___qtreewidgetitem = self.my_treeView.header()
        #___qtreewidgetitem.setText(3, QCoreApplication.translate("My_App", u"Ab", None));
        #___qtreewidgetitem.setText(2, QCoreApplication.translate("My_App", u"Nome", None));
        #.setText(1, QCoreApplication.translate("My_App", u"ID", None));
        #___qtreewidgetitem.setText(0, QCoreApplication.translate("My_App", u"Check", None));
        self.label.setText(QCoreApplication.translate("My_App", u"Nome", None))
        self.name_LE.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("My_App", u"Gender", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("My_App", u"Male", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("My_App", u"Female", None))

        self.label_3.setText(QCoreApplication.translate("My_App", u"Photo", None))
        self.toolButton.setText(QCoreApplication.translate("My_App", u"...", None))
        self.pushButton.setText(QCoreApplication.translate("My_App", u"Submit", None))
    # retranslateUi

