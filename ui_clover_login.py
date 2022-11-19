# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clover_login.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import Resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(930, 500)
        self.LoginScreen = QWidget(Dialog)
        self.LoginScreen.setObjectName(u"LoginScreen")
        self.LoginScreen.setGeometry(QRect(0, 0, 930, 500))
        self.LoginScreen.setStyleSheet(u"")
        self.usrnmfield = QLineEdit(self.LoginScreen)
        self.usrnmfield.setObjectName(u"usrnmfield")
        self.usrnmfield.setGeometry(QRect(532, 180, 311, 50))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usrnmfield.sizePolicy().hasHeightForWidth())
        self.usrnmfield.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(25)
        font.setBold(False)
        self.usrnmfield.setFont(font)
        self.usrnmfield.setAcceptDrops(False)
        self.usrnmfield.setStyleSheet(u"QLineEdit {\n"
"    padding-left: 0.4em;\n"
"    border-radius: 12.5px;\n"
"    font-weight: 100;\n"
"}")
        self.usrnmfield.setMaxLength(20)
        self.usrnmfield.setFrame(True)
        self.usrnmfield.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.usrnmfield.setClearButtonEnabled(True)
        self.pwdfield = QLineEdit(self.LoginScreen)
        self.pwdfield.setObjectName(u"pwdfield")
        self.pwdfield.setGeometry(QRect(532, 245, 311, 51))
        self.pwdfield.setFont(font)
        self.pwdfield.setAcceptDrops(False)
        self.pwdfield.setStyleSheet(u"QLineEdit {\n"
"    padding-left: 0.4em;\n"
"    border-radius: 12.5px;\n"
"    font-weight: 100;\n"
"}")
        self.pwdfield.setMaxLength(20)
        self.pwdfield.setEchoMode(QLineEdit.Password)
        self.pwdfield.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.pwdfield.setClearButtonEnabled(True)
        self.loginbutton = QPushButton(self.LoginScreen)
        self.loginbutton.setObjectName(u"loginbutton")
        self.loginbutton.setGeometry(QRect(532, 310, 150, 50))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.loginbutton.setFont(font1)
        self.loginbutton.setStyleSheet(u"")
        self.signupbutton = QPushButton(self.LoginScreen)
        self.signupbutton.setObjectName(u"signupbutton")
        self.signupbutton.setGeometry(QRect(692, 310, 150, 50))
        self.signupbutton.setFont(font1)
        self.signupbutton.setStyleSheet(u"")
        self.alertbox = QLabel(self.LoginScreen)
        self.alertbox.setObjectName(u"alertbox")
        self.alertbox.setGeometry(QRect(532, 390, 291, 31))
        self.bg = QLabel(self.LoginScreen)
        self.bg.setObjectName(u"bg")
        self.bg.setGeometry(QRect(0, 0, 930, 500))
        self.bg.setPixmap(QPixmap(u":/Images/rsrc/clover_login_bg_v1.png"))
        self.bg.setScaledContents(False)
        self.label = QLabel(self.LoginScreen)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(613, 99, 151, 71))
        font2 = QFont()
        font2.setFamilies([u"Kollektif"])
        font2.setPointSize(60)
        font2.setBold(True)
        self.label.setFont(font2)
        self.bg.raise_()
        self.pwdfield.raise_()
        self.loginbutton.raise_()
        self.signupbutton.raise_()
        self.alertbox.raise_()
        self.usrnmfield.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Clover | Login", None))
        self.usrnmfield.setPlaceholderText(QCoreApplication.translate("Dialog", u"username", None))
        self.pwdfield.setPlaceholderText(QCoreApplication.translate("Dialog", u"password", None))
        self.loginbutton.setText(QCoreApplication.translate("Dialog", u"LOGIN", None))
        self.signupbutton.setText(QCoreApplication.translate("Dialog", u"SIGNUP", None))
        self.alertbox.setText("")
        self.bg.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Login", None))
    # retranslateUi

