from .base import EncryptionBase
from helpers.cryptology import *

class VigenereCipher(EncryptionBase):

    def encrypt(self, key:str, plaintext:str) -> str:
        '''
        Only Supports upper case.
        :param key:
        :param plaintext:
        :return: Cipher Text
        '''
        plaintext = plaintext.upper()
        key_length = len(key)
        key_as_int = [ord(i) for i in key]
        plaintext_int = [ord(i) for i in plaintext]
        ciphertext = ''
        for i in range(len(plaintext_int)):
            value = (plaintext_int[i] + key_as_int[i % key_length]) % self.alphabetsEnglishLength()
            ciphertext += chr(value + 65)
        return ciphertext

    def decrypt(self, key:str, ciphertext:str) -> str:
        '''
        Only supports upper case.
        :param key:
        :param ciphertext:
        :return: Plain Text
        '''
        ciphertext = ciphertext.upper()
        key_length = len(key)
        key_as_int = [ord(i) for i in key]
        ciphertext_int = [ord(i) for i in ciphertext]
        plaintext = ''
        for i in range(len(ciphertext_int)):
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % self.alphabetsEnglishLength()
            plaintext += chr(value + 65)
        return plaintext