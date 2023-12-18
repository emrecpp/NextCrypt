# -*- coding: utf-8 -*-
# Author: Emre Demircan (github:@emrecpp)

from helpers.cryptology.caesar import CaesarCipher
from helpers.cryptology.vigenere import VigenereCipher
from helpers.cryptology.atbash import AtbashCipher
from helpers.cryptology.vernam import VernamCipher
import helpers.gui_animation as gui_animation
from qfluentwidgets import InfoBar, InfoBarPosition, ToolTip, ToolTipPosition, ToolTipFilter
from imports import *
from Enums import AlgorithmTypes

class GUIBind(QObject):
    def init(self, window):
        self.window = window
        ui.btnEncrpyt.clicked.connect(self.EncryptClicked)
        ui.btnDecrypt.clicked.connect(self.DecryptClicked)
        ui.btnCopyResult.clicked.connect(self.CopyResultClicked)
        ui.btnReplaceInputOutput.clicked.connect(self.ReplaceInputOutputClicked)
        ui.txtCipherInput.setAcceptRichText(False)
        ui.cmbAlgorithm.currentTextChanged.connect(self.cmbAlgorithmTextChanged)
        ui.widCipherOutput.setVisible(False)

        ui.btnCopyResult.installEventFilter(ToolTipFilter(ui.btnCopyResult, showDelay=500))
        ui.btnReplaceInputOutput.installEventFilter(ToolTipFilter(ui.btnReplaceInputOutput, showDelay=500))

        ui.stackCipherParameters.setCurrentWidget(ui.page_parameters_caesar)

        self.LoadData()

        self.cipher_caesar = CaesarCipher(upperandlowercase=False) # only upper case
        self.cipher_vigenere = VigenereCipher()
        self.cipher_atbash = AtbashCipher()
        self.cipher_vernam = VernamCipher()


    def LoadData(self):
        for algorithm in AlgorithmTypes:
            ui.cmbAlgorithm.addItem(algorithm.toHumandReadableName(), QIcon(f':/img/cryptography/{algorithm.name}.png'), userData=algorithm)

    def EncryptClicked(self):
        input:str = ui.txtCipherInput.toPlainText().strip()
        if not input:
            InfoBar.error(title="Error", content="Input is empty!", isClosable=True, position=InfoBarPosition.TOP, duration=3000, parent=main)
            return
        if self.getSelectedAlgorithm() == AlgorithmTypes.CAESAR:
            key = ui.parameters_caesar_key.value()
            result = self.cipher_caesar.encrypt(key, input)
            if not self.cipher_caesar.upperandlowercase:
                ui.txtCipherInput.setText(input.upper())
        elif self.getSelectedAlgorithm() == AlgorithmTypes.VIGENERE:
            ui.txtCipherInput.setText(input.upper()) # vigenere only supports upper case so in the GUI, user should know that.
            key = ui.txt_parameters_vigenere_key.text().strip()
            if not key:
                InfoBar.error(title="Error", content="Key is empty!", isClosable=True, position=InfoBarPosition.TOP, duration=3000, parent=main)
                return
            result = self.cipher_vigenere.encrypt(key, input)
        elif self.getSelectedAlgorithm() == AlgorithmTypes.ATBASH:
            result = self.cipher_atbash.encrypt(input)
        elif self.getSelectedAlgorithm() == AlgorithmTypes.VERNAM:
            ui.txtCipherInput.setText(input.upper())  # vernam only supports upper case so in the GUI, user should know that.
            ui.txt_parameters_vernam_key.setText(ui.txt_parameters_vernam_key.text().upper())
            key = ui.txt_parameters_vernam_key.text().strip()
            result = self.cipher_vernam.encrypt(key, input)
            if not result:
                return
        else:
            raise Exception("Unknown Algorithm Type")

        ui.txtCipherOutput.setText(result)
        ui.lblResultTitle.setText(f"<font style='font-weight:600'>Result of Encryption</font> ({self.getSelectedAlgorithm().toHumandReadableName()})")

        firstTime:bool = not ui.widCipherOutput.isVisible()
        ui.widCipherOutput.setVisible(True)

        if firstTime: # first time show so use "move" animate
            gui_animation.aniMove(ui.widCipherOutput, duration=1000, startY=self.window.height()+50)
        else: # already showing, so use "fade" animate
            gui_animation.fadeOut(ui.widCipherOutput, duration=100, hideit=False)

    def DecryptClicked(self):
        input: str = ui.txtCipherInput.toPlainText().strip()
        if not input:
            InfoBar.error(title="Error", content="Input is empty!", isClosable=True, position=InfoBarPosition.TOP,
                          duration=3000, parent=main)
            return


        if self.getSelectedAlgorithm() == AlgorithmTypes.CAESAR:
            key = ui.parameters_caesar_key.value()
            result = self.cipher_caesar.decrypt(key, input) # plainText
            if not self.cipher_caesar.upperandlowercase:
                ui.txtCipherInput.setText(input.upper())
        elif self.getSelectedAlgorithm() == AlgorithmTypes.VIGENERE:
            ui.txtCipherInput.setText(input.upper()) # vigenere only supports upper case so in the GUI, user should know that.
            key = ui.txt_parameters_vigenere_key.text().strip()
            if not key:
                InfoBar.error(title="Error", content="Key is empty!", isClosable=True, position=InfoBarPosition.TOP, duration=3000, parent=main)
                return
            result = self.cipher_vigenere.decrypt(key, input)
        elif self.getSelectedAlgorithm() == AlgorithmTypes.ATBASH:
            result = self.cipher_atbash.decrypt(input)
        elif self.getSelectedAlgorithm() == AlgorithmTypes.VERNAM:
            ui.txtCipherInput.setText(input.upper())  # vernam only supports upper case so in the GUI, user should know that.
            ui.txt_parameters_vernam_key.setText(ui.txt_parameters_vernam_key.text().upper())
            key = ui.txt_parameters_vernam_key.text().strip()
            result = self.cipher_vernam.decrypt(key, input)
            if not result:
                return
        else:
            raise Exception("Unknown Algorithm Type")
        ui.txtCipherOutput.setText(result)
        ui.lblResultTitle.setText(f"<font style='font-weight:600'>Result of Decryption</font> ({self.getSelectedAlgorithm().toHumandReadableName()})")
        firstTime:bool = not ui.widCipherOutput.isVisible()
        ui.widCipherOutput.setVisible(True)

        if firstTime: # first time show so use "move" animate
            gui_animation.aniMove(ui.widCipherOutput, duration=1000, startY=self.window.height()+50)
        else: # already showing, so use "fade" animate
            gui_animation.fadeOut(ui.widCipherOutput, duration=100, hideit=False)


    def CopyResultClicked(self):
        import pyperclip
        pyperclip.copy(ui.txtCipherOutput.toPlainText())
        InfoBar.success(title="Success", content="Result copied.", isClosable=True, position=InfoBarPosition.TOP, duration=3000, parent=main)
    def ReplaceInputOutputClicked(self):
        input, output = ui.txtCipherInput.toPlainText(), ui.txtCipherOutput.toPlainText()
        ui.txtCipherInput.setText(output)
        ui.txtCipherOutput.setText(input)

    def cmbAlgorithmTextChanged(self, currentText:str):
        if currentText == AlgorithmTypes.CAESAR.toHumandReadableName():
            ui.stackCipherParameters.setCurrentWidget(ui.page_parameters_caesar)
            ui.stackCipherParameters.setVisible(True)
            gui_animation.aniMove(ui.stackCipherParameters, duration=1000, startX=self.window.width()+50)
        elif currentText == AlgorithmTypes.VIGENERE.toHumandReadableName():
            ui.stackCipherParameters.setCurrentWidget(ui.page_parameters_vigenere)
            ui.stackCipherParameters.setVisible(True)
            gui_animation.aniMove(ui.stackCipherParameters, duration=1000, startX=self.window.width()+50)
        elif currentText == AlgorithmTypes.ATBASH.toHumandReadableName():
            ui.stackCipherParameters.setVisible(False)
        elif currentText == AlgorithmTypes.VERNAM.toHumandReadableName():
            ui.stackCipherParameters.setCurrentWidget(ui.page_parameters_vernam)
            ui.stackCipherParameters.setVisible(True)
            gui_animation.aniMove(ui.stackCipherParameters, duration=1000, startX=self.window.width()+50)

    def getSelectedAlgorithm(self) -> AlgorithmTypes:
        return ui.cmbAlgorithm.currentData()

