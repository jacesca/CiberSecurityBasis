"""
XOR Algorithm
    is a straightforward encryption method that relies on the XOR operation, a
    binary operation that produces an output based on the differences between
    corresponding bits of the text and some specified binary key.
    This algorithm is symmetric that means there is one key for both encryption
    and decryption.
Algorithm implementation
    Encryption Process:
        The encryption process involves XORing each bit of the plaintext with
        the corresponding bit of the key.
        If the bits are the same, the resultis 0; if different, the result
        is 1.
        This process is iterated for each bit in the plaintext, producing the
        ciphertext.
    Decryption Process:
        Decryption is a mirror image of encryption.
        XORing the ciphertext with the same key used for encryption restores
        the original plaintext.
        The XOR operation is symmetric; XORing twicewith the same value yields
        the initial value.
    Variable-Length Keys:
        In some XOR-based encryption implementations, the key's length may
        differ from that of the plaintext.
        To accommodate this, the key is repeated cyclically to match the
        plaintext's length.
        This repetition ensures a consistent XOR operation throughout the
        entire message, maintaining the algorithm's integrity.
"""


class XorCipher():
    """XOR cipher implementation"""
    def __init__(self, key):
        self.key = key
        self.binary_key = ''.join(format(ord(char), '08b') for char in key)
        self.len_binary_key = len(self.binary_key)

    def _xor_algorithm(self, binary_msg):
        len_binary_msg = len(binary_msg)

        repeated_key = (self.binary_key * (len_binary_msg // self.len_binary_key + 1))[:len_binary_msg]  # noqa

        binary_encoded = ''.join(
                                str(int(bit_char) ^ int(bit_key))
                                for bit_char, bit_key
                                in zip(binary_msg, repeated_key)
                            )
        return binary_encoded

    def encrypt(self, msg):
        binary_msg = ''.join(format(ord(char), '08b') for char in msg)
        binary_encoded = self._xor_algorithm(binary_msg)
        return binary_encoded

    def decrypt(self, msg_encoded):
        binary_decoded = self._xor_algorithm(msg_encoded)
        msg_decoded = ''.join(
                            chr(int(binary_decoded[i:i+8], 2))
                            for i
                            in range(0, len(binary_decoded), 8)
                         )
        return msg_decoded


if __name__ == '__main__':
    message = 'Hello, this is a XOR encoding.'
    key = 'secretkey'

    cipher = XorCipher(key)
    encrypted_msg = cipher.encrypt(message)
    decrypted_msg = cipher.decrypt(encrypted_msg)

    assert message == decrypted_msg, "Error: Cipher process did not work!"

    print(f"""
    Message: {message}
    Encripted: {encrypted_msg}
    Decripted: {decrypted_msg}
    """)
