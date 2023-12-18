# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogMain.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QSizePolicy, QSpacerItem, QStackedWidget,
    QWidget)

from qfluentwidgets import (ComboBox, LineEdit, PushButton, SpinBox,
    TextEdit, ToolButton)
import images_rc
import images_rc

class Ui_DialogMain(object):
    def setupUi(self, DialogMain):
        if not DialogMain.objectName():
            DialogMain.setObjectName(u"DialogMain")
        DialogMain.resize(602, 489)
        icon = QIcon()
        icon.addFile(u":/img/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        DialogMain.setWindowIcon(icon)
        DialogMain.setStyleSheet(u"\n"
"QTextEdit{\n"
"	font-size:16pt\n"
"}\n"
"QLabel{\n"
"font-size:16pt;\n"
"color:rgb(60,60,60)\n"
"}\n"
"\n"
"#lblTitle_caesar, #lblTitle_vigenere, #lblTitle_vernam {\n"
"font-weight:600;\n"
"font-style:italic\n"
"}")
        self.gridLayout_3 = QGridLayout(DialogMain)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 45, -1, -1)
        self.stackCipherParameters = QStackedWidget(DialogMain)
        self.stackCipherParameters.setObjectName(u"stackCipherParameters")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackCipherParameters.sizePolicy().hasHeightForWidth())
        self.stackCipherParameters.setSizePolicy(sizePolicy)
        self.stackCipherParameters.setStyleSheet(u"#stackCipherParameters {\n"
"background-color:#f4f4f4;\n"
"border-radius:20px;\n"
"}")
        self.page_parameters_caesar = QWidget()
        self.page_parameters_caesar.setObjectName(u"page_parameters_caesar")
        self.gridLayout_5 = QGridLayout(self.page_parameters_caesar)
        self.gridLayout_5.setSpacing(10)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 2, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 4, 2, 1, 1)

        self.frame_2 = QFrame(self.page_parameters_caesar)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lblTitle_caesar = QLabel(self.frame_2)
        self.lblTitle_caesar.setObjectName(u"lblTitle_caesar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lblTitle_caesar.sizePolicy().hasHeightForWidth())
        self.lblTitle_caesar.setSizePolicy(sizePolicy2)
        self.lblTitle_caesar.setStyleSheet(u"")
        self.lblTitle_caesar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_8.addWidget(self.lblTitle_caesar, 0, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_6, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_2, 0, 0, 2, 6)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 3, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 3, 5, 1, 1)

        self.label_2 = QLabel(self.page_parameters_caesar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_2, 3, 2, 1, 1)

        self.parameters_caesar_key = SpinBox(self.page_parameters_caesar)
        self.parameters_caesar_key.setObjectName(u"parameters_caesar_key")
        self.parameters_caesar_key.setValue(1)

        self.gridLayout_5.addWidget(self.parameters_caesar_key, 3, 3, 1, 1)

        self.stackCipherParameters.addWidget(self.page_parameters_caesar)
        self.page_parameters_vigenere = QWidget()
        self.page_parameters_vigenere.setObjectName(u"page_parameters_vigenere")
        self.gridLayout_6 = QGridLayout(self.page_parameters_vigenere)
        self.gridLayout_6.setSpacing(10)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.txt_parameters_vigenere_key = LineEdit(self.page_parameters_vigenere)
        self.txt_parameters_vigenere_key.setObjectName(u"txt_parameters_vigenere_key")

        self.gridLayout_6.addWidget(self.txt_parameters_vigenere_key, 3, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.frame = QFrame(self.page_parameters_vigenere)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lblTitle_vigenere = QLabel(self.frame)
        self.lblTitle_vigenere.setObjectName(u"lblTitle_vigenere")
        sizePolicy2.setHeightForWidth(self.lblTitle_vigenere.sizePolicy().hasHeightForWidth())
        self.lblTitle_vigenere.setSizePolicy(sizePolicy2)
        self.lblTitle_vigenere.setStyleSheet(u"")
        self.lblTitle_vigenere.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_7.addWidget(self.lblTitle_vigenere, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_5, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame, 0, 0, 1, 4)

        self.label_3 = QLabel(self.page_parameters_vigenere)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_3, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_2, 4, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 3, 3, 1, 1)

        self.stackCipherParameters.addWidget(self.page_parameters_vigenere)
        self.page_parameters_vernam = QWidget()
        self.page_parameters_vernam.setObjectName(u"page_parameters_vernam")
        self.gridLayout_11 = QGridLayout(self.page_parameters_vernam)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_3 = QFrame(self.page_parameters_vernam)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lblTitle_vernam = QLabel(self.frame_3)
        self.lblTitle_vernam.setObjectName(u"lblTitle_vernam")
        sizePolicy2.setHeightForWidth(self.lblTitle_vernam.sizePolicy().hasHeightForWidth())
        self.lblTitle_vernam.setSizePolicy(sizePolicy2)
        self.lblTitle_vernam.setStyleSheet(u"")
        self.lblTitle_vernam.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_10.addWidget(self.lblTitle_vernam, 0, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_8, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_3, 0, 0, 1, 4)

        self.verticalSpacer_7 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_7, 1, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(43, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_8, 2, 0, 1, 1)

        self.label_4 = QLabel(self.page_parameters_vernam)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_4, 2, 1, 1, 1)

        self.txt_parameters_vernam_key = LineEdit(self.page_parameters_vernam)
        self.txt_parameters_vernam_key.setObjectName(u"txt_parameters_vernam_key")

        self.gridLayout_11.addWidget(self.txt_parameters_vernam_key, 2, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(43, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_7, 2, 3, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_9, 3, 1, 1, 1)

        self.stackCipherParameters.addWidget(self.page_parameters_vernam)

        self.gridLayout_3.addWidget(self.stackCipherParameters, 1, 2, 1, 1)

        self.widget = QWidget(DialogMain)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.txtCipherInput = TextEdit(self.widget)
        self.txtCipherInput.setObjectName(u"txtCipherInput")

        self.gridLayout.addWidget(self.txtCipherInput, 2, 0, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 50))
        self.gridLayout_9 = QGridLayout(self.widget_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)

        self.gridLayout_9.addWidget(self.label, 0, 0, 1, 1)

        self.cmbAlgorithm = ComboBox(self.widget_2)
        self.cmbAlgorithm.setObjectName(u"cmbAlgorithm")
        self.cmbAlgorithm.setIconSize(QSize(32, 32))

        self.gridLayout_9.addWidget(self.cmbAlgorithm, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 0, 1, 2, 1)

        self.widCipherOutput = QWidget(DialogMain)
        self.widCipherOutput.setObjectName(u"widCipherOutput")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widCipherOutput.sizePolicy().hasHeightForWidth())
        self.widCipherOutput.setSizePolicy(sizePolicy4)
        self.widCipherOutput.setMinimumSize(QSize(0, 0))
        self.gridLayout_2 = QGridLayout(self.widCipherOutput)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, 0, 9, 0)
        self.lblResultTitle = QLabel(self.widCipherOutput)
        self.lblResultTitle.setObjectName(u"lblResultTitle")
        self.lblResultTitle.setStyleSheet(u"font-size:16pt;\n"
"color:rgb(90, 90, 90)")

        self.gridLayout_2.addWidget(self.lblResultTitle, 1, 0, 1, 1)

        self.txtCipherOutput = TextEdit(self.widCipherOutput)
        self.txtCipherOutput.setObjectName(u"txtCipherOutput")
        self.txtCipherOutput.setReadOnly(True)

        self.gridLayout_2.addWidget(self.txtCipherOutput, 2, 0, 1, 2)

        self.btnCopyResult = ToolButton(self.widCipherOutput)
        self.btnCopyResult.setObjectName(u"btnCopyResult")
        self.btnCopyResult.setMinimumSize(QSize(0, 48))
        self.btnCopyResult.setMaximumSize(QSize(48, 48))
        self.btnCopyResult.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/img/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCopyResult.setIcon(icon1)
        self.btnCopyResult.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.btnCopyResult, 2, 2, 1, 1)

        self.btnReplaceInputOutput = ToolButton(self.widCipherOutput)
        self.btnReplaceInputOutput.setObjectName(u"btnReplaceInputOutput")
        self.btnReplaceInputOutput.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/img/replace.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnReplaceInputOutput.setIcon(icon2)
        self.btnReplaceInputOutput.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.btnReplaceInputOutput, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.widCipherOutput, 3, 0, 1, 3)

        self.widget_3 = QWidget(DialogMain)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 50))
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(20)
        self.btnDecrypt = PushButton(self.widget_3)
        self.btnDecrypt.setObjectName(u"btnDecrypt")
        self.btnDecrypt.setMinimumSize(QSize(250, 40))
        self.btnDecrypt.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/img/text.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDecrypt.setIcon(icon3)
        self.btnDecrypt.setIconSize(QSize(24, 24))

        self.gridLayout_4.addWidget(self.btnDecrypt, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 0, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.btnEncrpyt = PushButton(self.widget_3)
        self.btnEncrpyt.setObjectName(u"btnEncrpyt")
        self.btnEncrpyt.setMinimumSize(QSize(250, 40))
        self.btnEncrpyt.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/img/cipher.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEncrpyt.setIcon(icon4)
        self.btnEncrpyt.setIconSize(QSize(24, 24))

        self.gridLayout_4.addWidget(self.btnEncrpyt, 0, 2, 1, 1)


        self.gridLayout_3.addWidget(self.widget_3, 2, 1, 1, 2)


        self.retranslateUi(DialogMain)

        self.stackCipherParameters.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(DialogMain)
    # setupUi

    def retranslateUi(self, DialogMain):
        DialogMain.setWindowTitle(QCoreApplication.translate("DialogMain", u"NextCrypt | Emre Demircan @github/emrecpp", None))
        self.lblTitle_caesar.setText(QCoreApplication.translate("DialogMain", u"Caesar Parameters", None))
        self.label_2.setText(QCoreApplication.translate("DialogMain", u"Key:", None))
        self.lblTitle_vigenere.setText(QCoreApplication.translate("DialogMain", u"Vigenere Parameters", None))
        self.label_3.setText(QCoreApplication.translate("DialogMain", u"Key:", None))
        self.lblTitle_vernam.setText(QCoreApplication.translate("DialogMain", u"Vernam Parameters", None))
        self.label_4.setText(QCoreApplication.translate("DialogMain", u"Key:", None))
        self.txtCipherInput.setPlaceholderText(QCoreApplication.translate("DialogMain", u"Enter your text...", None))
        self.label.setText(QCoreApplication.translate("DialogMain", u"Algorithm:", None))
        self.lblResultTitle.setText(QCoreApplication.translate("DialogMain", u"Result", None))
#if QT_CONFIG(tooltip)
        self.btnCopyResult.setToolTip(QCoreApplication.translate("DialogMain", u"Copy the result", None))
#endif // QT_CONFIG(tooltip)
        self.btnCopyResult.setText("")
#if QT_CONFIG(tooltip)
        self.btnReplaceInputOutput.setToolTip(QCoreApplication.translate("DialogMain", u"Swap the input and output", None))
#endif // QT_CONFIG(tooltip)
        self.btnReplaceInputOutput.setText("")
        self.btnDecrypt.setText(QCoreApplication.translate("DialogMain", u"Decrypt", None))
        self.btnEncrpyt.setText(QCoreApplication.translate("DialogMain", u"Encrypt", None))
    # retranslateUi

