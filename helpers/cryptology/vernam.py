from .base import EncryptionBase
from helpers.cryptology import *
from qfluentwidgets import InfoBar, InfoBarPosition
from imports import main

class VernamCipher(EncryptionBase):

    def checkParametersRight(self, key:str, text:str):
        if len(key) != len(text):
            InfoBar.error(title="Error", content="Key and text should be of same length.", isClosable=True,
                          position=InfoBarPosition.TOP,
                          duration=3000, parent=main)
            return False

        if not text.isalpha():
            InfoBar.error(title="Error", content="It should be composed solely of letters!", isClosable=True,
                          position=InfoBarPosition.TOP,
                          duration=3000, parent=main)
            return False
        return True

    def encrypt(self, key:str, plaintext:str) -> str:
        if not self.checkParametersRight(key, plaintext):
            return ""

        plaintext = plaintext.upper()
        key = key.upper()

        ciphertext = ""
        for i in range(len(plaintext)):
            plaintext_char = ord(plaintext[i]) - ord('A')
            key_char = ord(key[i % len(key)]) - ord('A')
            encrypted_char = chr((plaintext_char + key_char) % 26 + ord('A'))
            ciphertext += encrypted_char

        return ciphertext

    def decrypt(self, key:str, ciphertext:str) -> str:
        if not self.checkParametersRight(key, ciphertext):
            return ""

        ciphertext = ciphertext.upper()
        key = key.upper()

        plaintext = ""
        for i in range(len(ciphertext)):
            ciphertext_char = ord(ciphertext[i]) - ord('A')
            key_char = ord(key[i % len(key)]) - ord('A')
            decrypted_char = chr((ciphertext_char - key_char) % 26 + ord('A'))
            plaintext += decrypted_char

        return plaintext