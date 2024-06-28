from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64encode


def zero_pad(data, block_size):
    padding_len = (block_size - len(data) % block_size) % block_size
    return data + b'\x00' * padding_len


def crypto_encode(ori_data, iv):
    key = b'1234567887654321'
    ivv = iv.encode('utf-8')

    padded_data = zero_pad(ori_data.encode('utf-8'), 16)

    cipher = Cipher(algorithms.AES(key), modes.CBC(ivv),
                    backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    return b64encode(encrypted_data).decode('utf-8')
