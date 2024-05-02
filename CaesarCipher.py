"""
Caesar cipher
    is a straightforward and historical encryption technique that falls under
    the category of symmetric ciphers. The cipher involves shifting each
    letter in the plaintext by a fixed number of positions down the alphabet.

Algorithm description
    Key
        The Caesar cipher uses a fixed shift value to encrypt and decrypt
        messages. The key represents the number of positions each letter of
        the plaintext is shifted in the alphabet.

    Work Principles
        Encryption:
            - For each letter in the plaintext, shift it forward in the
              alphabet by the fixed key.
            - Wrap around to the beginning of the alphabet if the shift goes
              beyond 'Z' (for uppercase) or 'z' (for lowercase).
            - Non-alphabetic characters remain unchanged.
        Decryption:
            - To decrypt, shift each letter in the ciphertext backward in
              the alphabet by the fixed key.
            - Wrap around to the end of the alphabet if the shift goes
              before 'A' (for uppercase) or 'a' (for lowercase).
            - Non-alphabetic characters remain unchanged.
"""


class CaesarCipher:
    """Caesar Cipher technique implementation"""
    def __init__(self, key):
        self.key = key

    def encrypt(self, msg):
        msg_encripted = ''

        for char in msg:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                msg_encripted += chr((ord(char) - start + self.key) % 26 + start)  # noqa
            else:
                msg_encripted += char
        return msg_encripted

    def decrypt(self, msg_encripted):
        msg = ''

        for char in msg_encripted:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                msg += chr((ord(char) - start - self.key) % 26 + start)  # noqa
            else:
                msg += char
        return msg


if __name__ == '__main__':
    message = "1WORLD2"
    key = 5

    cipher = CaesarCipher(key)
    encrypted_msg = cipher.encrypt(message)
    decrypted_msg = cipher.decrypt(encrypted_msg)

    assert message == decrypted_msg, "Error: Cipher process did not work!"

    print(f"""
    Message: {message}
    Encripted: {encrypted_msg}
    Decripted: {decrypted_msg}
    """)
