# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_seq_conv_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialogButtonBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QSizePolicy,
    QSpinBox, QStatusBar, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(413, 343)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.seq_dir_LB = QLabel(self.frame)
        self.seq_dir_LB.setObjectName(u"seq_dir_LB")

        self.horizontalLayout.addWidget(self.seq_dir_LB)

        self.seq_dir_LE = QLineEdit(self.frame)
        self.seq_dir_LE.setObjectName(u"seq_dir_LE")

        self.horizontalLayout.addWidget(self.seq_dir_LE)

        self.seq_dir_TB = QToolButton(self.frame)
        self.seq_dir_TB.setObjectName(u"seq_dir_TB")

        self.horizontalLayout.addWidget(self.seq_dir_TB)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.out_dir_LB = QLabel(self.frame)
        self.out_dir_LB.setObjectName(u"out_dir_LB")

        self.horizontalLayout_2.addWidget(self.out_dir_LB)

        self.out_dir_LE = QLineEdit(self.frame)
        self.out_dir_LE.setObjectName(u"out_dir_LE")

        self.horizontalLayout_2.addWidget(self.out_dir_LE)

        self.out_dir_TB = QToolButton(self.frame)
        self.out_dir_TB.setObjectName(u"out_dir_TB")

        self.horizontalLayout_2.addWidget(self.out_dir_TB)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.fps_LB = QLabel(self.frame)
        self.fps_LB.setObjectName(u"fps_LB")

        self.horizontalLayout_3.addWidget(self.fps_LB)

        self.fps_spinbox = QSpinBox(self.frame)
        self.fps_spinbox.setObjectName(u"fps_spinbox")
        self.fps_spinbox.setMaximum(999)
        self.fps_spinbox.setValue(24)

        self.horizontalLayout_3.addWidget(self.fps_spinbox)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.res_LB = QLabel(self.frame)
        self.res_LB.setObjectName(u"res_LB")

        self.horizontalLayout_4.addWidget(self.res_LB)

        self.res_spinBox_width = QSpinBox(self.frame)
        self.res_spinBox_width.setObjectName(u"res_spinBox_width")
        self.res_spinBox_width.setMinimum(1)
        self.res_spinBox_width.setMaximum(9999)
        self.res_spinBox_width.setValue(1920)

        self.horizontalLayout_4.addWidget(self.res_spinBox_width)

        self.res_spinBox_height = QSpinBox(self.frame)
        self.res_spinBox_height.setObjectName(u"res_spinBox_height")
        self.res_spinBox_height.setMinimum(1)
        self.res_spinBox_height.setMaximum(9999)
        self.res_spinBox_height.setValue(1080)

        self.horizontalLayout_4.addWidget(self.res_spinBox_height)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.def_res_CB = QCheckBox(self.frame)
        self.def_res_CB.setObjectName(u"def_res_CB")

        self.gridLayout_2.addWidget(self.def_res_CB, 4, 0, 1, 1)

        self.save_reset_buttonBox = QDialogButtonBox(self.frame)
        self.save_reset_buttonBox.setObjectName(u"save_reset_buttonBox")
        self.save_reset_buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Reset|QDialogButtonBox.Save)

        self.gridLayout_2.addWidget(self.save_reset_buttonBox, 5, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 413, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.seq_dir_LB.setText(QCoreApplication.translate("MainWindow", u"Sequece Folder : ", None))
        self.seq_dir_TB.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.out_dir_LB.setText(QCoreApplication.translate("MainWindow", u"Output Path: ", None))
        self.out_dir_TB.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.fps_LB.setText(QCoreApplication.translate("MainWindow", u"FPS :", None))
        self.res_LB.setText(QCoreApplication.translate("MainWindow", u"Resolution:", None))
        self.def_res_CB.setText(QCoreApplication.translate("MainWindow", u"Default Resolution", None))
    # retranslateUi

