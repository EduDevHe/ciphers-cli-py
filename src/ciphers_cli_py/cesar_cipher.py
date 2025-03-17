LATIN_ALPHABET =  'abcdefghijklmnopqrstuvwxyz'

class CesarCipher:

    def __init__(self, message, shift) -> None:
        if not type(message) is str:
            raise ValueError('Message value must be string')

        if not type(shift) is int:
            raise ValueError('Shift value must be integer')

        if shift < 0:
            raise ValueError('Shift value must be positive')

        self.message = message 
        self.shift = shift
        self.result = ''

    def _cipher(self, message, shift, direction = 1):
        result = ''
        for char in message.lower():
            if char in LATIN_ALPHABET:
                new_index = (LATIN_ALPHABET.index(char) + (shift * direction)) % len(LATIN_ALPHABET)
                result += LATIN_ALPHABET[new_index]       
            else:
                result += char

        return result

    def encrypt(self):
        return self._cipher(self.message,self.shift)
    
    def decrypt(self):
        return self._cipher(self.message, self.shift, -1)
        

