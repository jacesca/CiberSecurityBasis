"""
Password hashing
    is a security measure that protects user passwords by converting them into
    a hashed, irreversible format. Hashing is a one-way cryptographic function
    that transforms plaintext passwords into a fixed-length string of
    characters, making it challenging for attackers to reverse-engineer the
    original password.
    Hashing is used on the Application Layer of the OSI model as a defense
    against attacks that aim to compromise user credentials and gain
    unauthorized access to systems or sensitive information.

Steps in Password Hashing
    User Registration:
        When a user creates an account or changes their password, the
        plaintext password is hashed.
    Hash Storage:
        The hashed password is stored in the database.
    Authentication:
        During login, the entered password is hashed, and the generated hash
        is compared with the stored hash. If they match, the authentication
        is successful.
Hashing is often used in pair with salting. Salting involves adding a unique,
random value (salt) to each password before hashing. This ensures that even
if two users have the same password, their hashed representations will be
different due to the unique salt.

How is hashing done?
    To understand hashing we first have to consider concept of hash function.
    At its core, a hash function is a deterministic algorithm that takes input
    data and produces a fixed-size string of characters, commonly referred to
    as a hash value or hash code.

The Hashing Process
    Input Data Selection:
        The process begins by selecting the input data - any piece of
        information that requires protection. In our case it is a password.
    Application of the Hash Function:
        The chosen hash function is applied to the input data. This involves
        the algorithm processing the data to generate a unique hash value.
    Hash Value Output:
        The computed hash value serves as the output of the hashing process -
        a string of characters with a fixed length.
    Salting usage:
        If we want to use salting, we combine a special generated salt with our
        input data before hashing.
"""


def simple_hash(input_string, size):
    hash_value = 0

    # Add the aschi value of each char
    for char in input_string:
        hash_value += ord(char)

    hash_value = hash_value % size
    return hash_value


if __name__ == '__main__':
    input_string = 'Element'
    size = 9

    result = simple_hash(input_string, size)
    print(f"The hash value for '{input_string}' is {result}")
