from .base import EncryptionBase
from helpers.cryptology import *

class AtbashCipher(EncryptionBase):

    def encrypt(self, message:str) -> str:
        '''
        Supports uppercase.
        :param message: Plain Text
        :return: Cipher text
        '''
        result = ''
        for char in message:
            if char.isalpha():
                if char.islower():
                    result += chr(ord('z') - (ord(char) - ord('a')))
                elif char.isupper():
                    result += chr(ord('Z') - (ord(char) - ord('A')))
            else:
                result += char
        return result


    def decrypt(self, message:str) -> str:
        '''
        Supports uppercase.
        :param message: Cipher Text
        :return: Plain Text
        '''
        return self.encrypt(message) # Atbash encryption and decryption are the same
