class EncryptionBase(object):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabets_english_upperinner = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" # for Caesar cipher

    def encrypt(self, plain_text:str):
        pass
    def decrypt(self, cipher_text:str):
        pass

    def alphabetsEnglishLength(self) -> int:
        return 26