from .base import EncryptionBase
from helpers.cryptology import *

class CaesarCipher(EncryptionBase):

    upperandlowercase:bool # default only upper case
    target_alphabet:str

    def __init__(self, upperandlowercase:bool=False):
        super().__init__()
        self.upperandlowercase = upperandlowercase
        self.target_alphabet = self.alphabets_english_upperinner if upperandlowercase else self.alphabets
        
    def get_cipherletter(self, new_key, letter):
        if letter in self.target_alphabet:
            return self.target_alphabet[new_key]
        else:
            return letter

    def encrypt(self, key:int, message:str) -> str:
        '''
        Supports upper & lower case.
        :param key:
        :param message:
        :return: Cipher Text
        '''
        result = ""
        if not self.upperandlowercase:
            message = message.upper()

        for letter in message:
            new_key = (self.target_alphabet.find(letter) + key) % len(self.target_alphabet)
            result = result + self.get_cipherletter(new_key, letter)

        return result

    def decrypt(self, key:int, message:str) -> str:
        '''
        Supports upper & lower case.
        :param key:
        :param message:
        :return: Plain Text
        '''
        result = ""
        if not self.upperandlowercase:
            message = message.upper()

        for letter in message:
            new_key = (self.target_alphabet.find(letter) - key) % len(self.target_alphabet)
            result = result + self.get_cipherletter(new_key, letter)

        return result