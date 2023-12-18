# Author: Emre Demircan (github:@emrecpp)
from enum import Enum, IntEnum
class AlgorithmTypes(IntEnum):
    CAESAR   = 1
    VIGENERE = 2
    ATBASH   = 3
    VERNAM   = 4


    def toHumandReadableName(self):
        if self == AlgorithmTypes.CAESAR:
            return "Caesar Cipher"
        elif self == AlgorithmTypes.VIGENERE:
            return "Vigenere Cipher"
        elif self == AlgorithmTypes.ATBASH:
            return "Atbash Cipher"
        elif self == AlgorithmTypes.VERNAM:
            return "Vernam Cipher"
        else:
            raise Exception("Unknown Algorithm Type")