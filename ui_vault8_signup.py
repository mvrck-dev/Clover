# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vault8_signup.ui'
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
        Dialog.resize(850, 530)
        self.SignUpScreen = QWidget(Dialog)
        self.SignUpScreen.setObjectName(u"SignUpScreen")
        self.SignUpScreen.setGeometry(QRect(0, 0, 850, 530))
        self.SignUpScreen.setStyleSheet(u"")
        self.usrnmfield = QLineEdit(self.SignUpScreen)
        self.usrnmfield.setObjectName(u"usrnmfield")
        self.usrnmfield.setGeometry(QRect(510, 120, 311, 50))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usrnmfield.sizePolicy().hasHeightForWidth())
        self.usrnmfield.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(23)
        font.setBold(False)
        self.usrnmfield.setFont(font)
        self.usrnmfield.setAcceptDrops(False)
        self.usrnmfield.setAutoFillBackground(False)
        self.usrnmfield.setStyleSheet(u"")
        self.usrnmfield.setMaxLength(20)
        self.usrnmfield.setFrame(True)
        self.usrnmfield.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.usrnmfield.setClearButtonEnabled(True)
        self.emailfield = QLineEdit(self.SignUpScreen)
        self.emailfield.setObjectName(u"emailfield")
        self.emailfield.setGeometry(QRect(510, 179, 311, 51))
        self.emailfield.setFont(font)
        self.emailfield.setAcceptDrops(False)
        self.emailfield.setStyleSheet(u"")
        self.emailfield.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.emailfield.setMaxLength(50)
        self.emailfield.setEchoMode(QLineEdit.Normal)
        self.emailfield.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.emailfield.setClearButtonEnabled(True)
        self.pwdfield = QLineEdit(self.SignUpScreen)
        self.pwdfield.setObjectName(u"pwdfield")
        self.pwdfield.setGeometry(QRect(510, 239, 311, 51))
        self.pwdfield.setFont(font)
        self.pwdfield.setAcceptDrops(False)
        self.pwdfield.setStyleSheet(u"")
        self.pwdfield.setMaxLength(20)
        self.pwdfield.setEchoMode(QLineEdit.Password)
        self.pwdfield.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.pwdfield.setClearButtonEnabled(True)
        self.cnfpwdfield = QLineEdit(self.SignUpScreen)
        self.cnfpwdfield.setObjectName(u"cnfpwdfield")
        self.cnfpwdfield.setGeometry(QRect(510, 300, 311, 51))
        self.cnfpwdfield.setFont(font)
        self.cnfpwdfield.setAcceptDrops(False)
        self.cnfpwdfield.setStyleSheet(u"")
        self.cnfpwdfield.setMaxLength(20)
        self.cnfpwdfield.setEchoMode(QLineEdit.Password)
        self.cnfpwdfield.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.cnfpwdfield.setClearButtonEnabled(True)
        self.bg = QLabel(self.SignUpScreen)
        self.bg.setObjectName(u"bg")
        self.bg.setGeometry(QRect(0, 0, 851, 531))
        self.bg.setPixmap(QPixmap(u":/Images/rsrc/vault8_login_wrapper_v0.1.png"))
        self.bg.setScaledContents(True)
        self.signupbutton = QPushButton(self.SignUpScreen)
        self.signupbutton.setObjectName(u"signupbutton")
        self.signupbutton.setGeometry(QRect(510, 368, 310, 50))
        font1 = QFont()
        font1.setPointSize(15)
        self.signupbutton.setFont(font1)
        self.signupbutton.setStyleSheet(u"")
        self.alertbox = QLabel(self.SignUpScreen)
        self.alertbox.setObjectName(u"alertbox")
        self.alertbox.setGeometry(QRect(520, 430, 291, 31))
        self.returnbtn = QPushButton(self.SignUpScreen)
        self.returnbtn.setObjectName(u"returnbtn")
        self.returnbtn.setGeometry(QRect(505, 60, 50, 50))
        self.returnbtn.setStyleSheet(u"#returnbtn{border-radius: 25px; background-color: #00000000;}")
        icon = QIcon()
        icon.addFile(u":/Icons/rsrc/return_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.returnbtn.setIcon(icon)
        self.returnbtn.setIconSize(QSize(35, 35))
        self.bg.raise_()
        self.pwdfield.raise_()
        self.usrnmfield.raise_()
        self.signupbutton.raise_()
        self.alertbox.raise_()
        self.emailfield.raise_()
        self.cnfpwdfield.raise_()
        self.returnbtn.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Vault8 | SignUp", None))
        self.usrnmfield.setPlaceholderText(QCoreApplication.translate("Dialog", u"username", None))
        self.emailfield.setPlaceholderText(QCoreApplication.translate("Dialog", u"email", None))
        self.pwdfield.setPlaceholderText(QCoreApplication.translate("Dialog", u"password", None))
        self.cnfpwdfield.setPlaceholderText(QCoreApplication.translate("Dialog", u"confirm password", None))
        self.bg.setText("")
        self.signupbutton.setText(QCoreApplication.translate("Dialog", u"CREATE ACCOUNT", None))
        self.alertbox.setText("")
        self.returnbtn.setText("")
    # retranslateUi

