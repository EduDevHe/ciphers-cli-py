from ciphers_cli_py.cesar_cipher import CesarCipher
import pytest


def test_class_cesar_chipher():
    instance = CesarCipher("Hello World", 3)
    assert isinstance(instance, CesarCipher)
    
def test_invalid_message():
    with pytest.raises(ValueError, match = 'Message value must be string'):
        CesarCipher(1,3)


def test_invalid_shift():
    with pytest.raises(ValueError, match='Shift value must be positive'):
        CesarCipher("hello", -3)
    
    with pytest.raises(ValueError, match='Shift value must be integer'):
        CesarCipher("hello","World")

def test_encrypt():
    cipher = CesarCipher("hello", 3)
    encrypted = cipher.encrypt()
    print(encrypted)
    assert encrypted == "khoor", f"Esperado 'khoor', mas obteve {encrypted}"

def test_decrypt():
    cipher = CesarCipher("khoor", 3)
    decrypted = cipher.decrypt()
    assert decrypted == "hello", f"Esperado 'hello', mas obteve {decrypted}"

def test_encrypt_with_spaces():
    cipher = CesarCipher("hello world", 3)
    encrypted = cipher.encrypt()
    assert encrypted == "khoor zruog", f"Esperado 'khoor zruog', mas obteve {encrypted}"

def test_decrypt_with_spaces():
    cipher = CesarCipher("khoor zruog", 3)
    decrypted = cipher.decrypt()
    assert decrypted == "hello world", f"Esperado 'hello world', mas obteve {decrypted}"

